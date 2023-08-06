import asyncio
import logging
import secrets
import falcon
import rapidjson
from time import time
from falcon import media
from websockets.exceptions import ConnectionClosedError

import falcon.asgi

from .rate_limiter import get_rate_limiter
from . import __version__
from .config import Config
from .errors import AuthenticationError


class Client:
    def __init__(self, ws, req, rate_limiter=None, log=None):
        self.ws = ws
        self.remote_addr = req.remote_addr
        self.id = f'{req.remote_addr}-{secrets.token_hex(2)}'
        self.log = log
        self.log.info(f'Accepted {self.id} from Origin: {req.get_header("origin")}')
        self.running = True
        self.subscription_queue = asyncio.Queue()
        self.send_task = None
        self.sent = 0
        self.rate_limiter = rate_limiter

    def validate_message(self, message):
        if not isinstance(message, list):
            return False
        if len(message) < 2:
            return False
        if message[0] not in ('EVENT', 'REQ', 'CLOSE', 'AUTH'):
            return False
        return True

    async def send_subscriptions(self):
        subscription_queue = self.subscription_queue
        ws = self.ws

        sent = 0
        self.log.debug("%s waiting for subs", self.id)
        while self.running and ws.ready:
            try:
                sub_id, event = await subscription_queue.get()
                if event is not None:
                    message = f'["EVENT", "{sub_id}", {event}]'
                else:
                    # done with stored events
                    message = f'["EOSE", "{sub_id}"]'
                await ws.send_text(message)
                self.log.debug("SENT: %s", message)
                self.sent += len(message)
            except (falcon.WebSocketDisconnected, ConnectionClosedError):
                break
            except asyncio.CancelledError:
                break
            except Exception:
                self.log.exception("subs")

    async def start(self, storage):
        ws = self.ws
        client_id = self.id
        remote_addr = self.remote_addr

        auth_token = {}

        if storage.authenticator.is_enabled:
            await ws.send_media(["AUTH", client_id])

        while ws.ready:
            try:
                message = await ws.receive_media()
                if not self.validate_message(message):
                    continue

                self.log.debug("RECEIVED: %s", message)
                command = message[0]

                if self.rate_limiter and self.rate_limiter.is_limited(remote_addr, message):
                    if command == 'EVENT':
                        response = ["OK", message[1]["id"], False, 'rate-limited: slow down']
                    else:
                        response = ["NOTICE", "rate-limited"]
                    await ws.send_media(response)
                    continue
                if command == 'REQ':
                    sub_id = str(message[1])
                    if self.send_task is None:
                        self.send_task = asyncio.create_task(self.send_subscriptions())
                        await asyncio.sleep(0)
                    await storage.subscribe(client_id, sub_id, message[2:], self.subscription_queue, auth_token=auth_token)
                elif command == 'CLOSE':
                    sub_id = str(message[1])
                    await storage.unsubscribe(client_id, sub_id)
                elif command == 'EVENT':
                    try:
                        event, result = await storage.add_event(message[1], auth_token=auth_token)
                    except Exception as e:
                        self.log.error(str(e))
                        result = False
                        reason = str(e)
                        eventid = ''
                    else:
                        eventid = event.id
                        reason = '' if result else 'duplicate: exists'
                        self.log.info("%s added %s from %s", client_id, event.id, event.pubkey)
                    await ws.send_media(['OK', eventid, result, reason])
                elif command == 'AUTH':
                    auth_token = await storage.authenticator.authenticate(message[1], challenge=client_id)
            except AuthenticationError as e:
                self.log.warning("Auth error. %s token:%s", str(e), auth_token)
                await ws.send_media(["NOTICE", str(e)])
            except (falcon.WebSocketDisconnected, ConnectionClosedError):
                break
            except rapidjson.JSONDecodeError:
                self.log.debug("json decoding")
                continue

    async def stop(self):
        self.running = False
        if self.send_task:
            self.send_task.cancel()
            try:
                await self.send_task
            except asyncio.CancelledError:
                pass

    def __str__(self):
        return self.id


class BaseResource:
    def __init__(self, storage):
        self.storage = storage
        self.log = logging.getLogger(__name__)


class NostrAPI(BaseResource):
    """
    Handles nostr websocket interface
    """
    def __init__(self, storage, rate_limiter=None):
        super().__init__(storage)
        self.connections = 0
        self.rate_limiter = rate_limiter

    async def on_get(self, req: falcon.Request, resp: falcon.Response):
        if req.accept == 'application/nostr+json':
            supported_nips = [1, 2, 5, 9, 11, 12, 15, 20, 26, 40]
            if Config.authentication.get('enabled'):
                supported_nips.append(42)
            metadata = {
                'name': Config.relay_name,
                'description': Config.relay_description,
                'pubkey': Config.sysop_pubkey,
                'contact': Config.sysop_contact,
                'supported_nips': supported_nips,
                'software': 'https://code.pobblelabs.org/fossil/nostr_relay',
                'version': __version__,
            }
            resp.media = metadata
        elif Config.redirect_homepage:
            raise falcon.HTTPFound(Config.redirect_homepage)
        else:
            resp.text = 'try using a nostr client :-)'
        resp.append_header('Access-Control-Allow-Origin', '*')
        resp.append_header('Access-Control-Allow-Headers', '*')
        resp.append_header('Access-Control-Allow-Methods', '*')

    async def on_websocket(self, req: falcon.Request, ws: falcon.asgi.WebSocket):
        if Config.origin_blacklist:
            origin = str(req.get_header('origin')).lower()
            if origin in Config.origin_blacklist:
                self.log.warning("Blocked origin %s from connecting", origin)
                await ws.close(code=1008)
                return

        try:
            await ws.accept()
            self.connections += 1
            start = time()

        except falcon.WebSocketDisconnected:
            return

        client = Client(ws, req, rate_limiter=self.rate_limiter, log=self.log)

        try:
            await client.start(self.storage)
        except Exception:
            self.log.exception("client loop")
        finally:
            await client.stop()
            await self.storage.unsubscribe(client.id)
            self.connections -= 1
            self.rate_limiter.cleanup()
            duration = time() - start
            self.log.info('Done {}. Sent: {:,} Bytes. Duration: {:.0f} Seconds'.format(client, client.sent, duration))


class NostrStats(BaseResource):
    async def on_get(self, req: falcon.Request, resp: falcon.Response):
        resp.media = await self.storage.get_stats()


class ViewEventResource(BaseResource):
    async def on_get(self, req: falcon.Request, resp: falcon.Response, event_id: str):
        try:
            event = await self.storage.get_event(event_id)
        except ValueError:
            raise falcon.HTTPNotFound
        except Exception:
            self.log.exception('get-event')
        if event:
            resp.media = event
        else:
            raise falcon.HTTPNotFound


class NostrIDP(BaseResource):
    """
    Serve /.well-known/nostr.json
    """
    async def on_get(self, req: falcon.Request, resp: falcon.Response):
        name = req.params.get('name', '')
        domain = req.host
        if name:
            identifier = f'{name}@{domain}'
        else:
            identifier = ''
        try:
            resp.media = await self.storage.get_identified_pubkey(identifier, domain=domain)
        except Exception:
            self.log.exception('idp')
        # needed for web clients
        resp.append_header('Access-Control-Allow-Origin', '*')
        resp.append_header('Access-Control-Allow-Headers', '*')
        resp.append_header('Access-Control-Allow-Methods', '*')


class SetupMiddleware:
    def __init__(self, storage):
        self.storage = storage

    async def process_startup(self, scope, event):
        import random
        if Config.DEBUG:
            asyncio.get_running_loop().set_debug(True)
        await self.storage.setup()

    async def process_shutdown(self, scope, event):
        await self.storage.optimize()
        await self.storage.close()



def create_app(conf_file=None, storage=None):
    import os
    import os.path
    import logging, logging.config
    from functools import partial

    Config.load(conf_file)
    if Config.DEBUG:
        print(Config)

    if Config.logging:
        logging.config.dictConfig(Config.logging)
    else:
        logging.basicConfig(format='%(asctime)s %(name)s %(levelname)s %(message)s', level=logging.DEBUG if Config.DEBUG else logging.INFO)

    from .storage import get_storage
    store = storage or get_storage()

    rate_limiter = get_rate_limiter(Config)

    json_handler = media.JSONHandlerWS(
        dumps=partial(
            rapidjson.dumps,
            ensure_ascii=False
        ),
        loads=rapidjson.loads,
    )

    logging.info("Starting version %s", __version__)
    app = falcon.asgi.App(middleware=SetupMiddleware(store))
    app.add_route('/', NostrAPI(store, rate_limiter=rate_limiter))
    app.add_route('/stats/', NostrStats(store))
    app.add_route('/e/{event_id}', ViewEventResource(store))
    app.add_route('/.well-known/nostr.json', NostrIDP(store))
    app.ws_options.media_handlers[falcon.WebSocketPayloadType.TEXT] = json_handler
    
    return app


def run_with_gunicorn(conf_file=None):
    """
    Run the app using gunicorn's ASGIApplication
    """
    app = create_app(conf_file)
    
    from gunicorn.app.base import Application

    class ASGIApplication(Application):
        def load_config(self):
            import sys
            if sys.implementation.name == 'pypy':
                worker_class = 'uvicorn.workers.UvicornH11Worker'
            else:
                worker_class = 'uvicorn.workers.UvicornWorker'
            self.cfg.set('worker_class', worker_class)
            for k, v in Config.gunicorn.items():
                self.cfg.set(k.lower(), v)

        def load(self):
            return app

    ASGIApplication().run()


def run_with_uvicorn(conf_file=None, in_thread=False):
    """
    Run the app using uvicorn.
    Optionally, start the server in a daemon thread
    """
    import uvicorn

    app = create_app(conf_file)

    options = dict(Config.gunicorn)
    if 'bind' in options:
        bind = options.pop('bind')
        options['port'] = int(bind.split(':')[1])
    if 'loglevel' in options:
        options['log_level'] = options.pop('loglevel')

    uv_config = uvicorn.Config(app, **options)
    server = uvicorn.Server(uv_config)

    if in_thread:
        import threading

        thr = threading.Thread(target=server.run, daemon=True)
        thr.start()
    else:
        server.run()



