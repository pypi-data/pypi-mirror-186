__author__ = "Brendon Taylor"
__email__ = "nuke@lanslide.com.au"
__status__ = "Production"

"""
Used to handle communication with the WebSocket.
The WebSockerMessage class handles any messages received on this hosts' channel.
"""

import asyncio
import docker
from lsquery.query import Query
import socket
from datetime import timedelta
import websocket
from datetime import datetime
from decouple import config
from lsquery.server import Server
import json
import pytz
import ssl
import time
import threading


class WebSocket:
    """
    RECONNECT_TIMEOUT: Default timeout before the websocket attempts to auto reconnect
    ws: Connection to our Websocket
    ws_message: Reference to our WebsocketMessage
    timeout: Timeout for the websocket
    channel: The channel we are using for the websocket
    """
    RECONNECT_TIMEOUT = 10
    ws = None
    ws_message = None
    timeout = None
    channel = None

    def __init__(self, timeout: int = RECONNECT_TIMEOUT):
        """
        :param timeout: Timeout for the websocket
        """
        WebSocket.ws_message = WebSocketMessage()
        WebSocket.timeout = timeout
        WebSocket.channel = socket.gethostname()
        WebSocket.connect_websocket()

    @classmethod
    def connect_websocket(cls) -> None:
        websocket_url = 'wss://{}:6001/app/{}/my-websocket'.format(config('WEBSOCKET_HOST'),
                                                                   config('WEBSOCKET_APP_KEY'))
        cls.ws = websocket.WebSocketApp(websocket_url,
                                        on_open=cls.on_open,
                                        on_message=cls.on_message,
                                        on_error=cls.on_error,
                                        on_close=cls.on_close)

        wst = threading.Thread(target=cls.ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE}))
        wst.daemon = True
        wst.start()

    @classmethod
    def process_message(cls, message: str) -> None:
        """
        Handles incoming messages received from the websocket server
        :param message: The incoming message
        """
        message_obj = json.loads(message)
        event = message_obj['event']
        print(message)

        try:
            data = json.loads(message_obj['data'])
        except KeyError:
            data = None

        response = None
        if event == 'portal:new-server':
            response = cls.ws_message.new_server(data)
        elif event == 'portal:get-servers':
            response = cls.ws_message.get_servers(data[0], data[1])
        elif event == 'portal:perform-action':
            response = cls.ws_message.perform_action(data['container_id'], data['action'])
        elif event == 'portal:mcrcon':
            response = cls.ws_message.mcrcon(data[0], data[1], data[2])

        if response:
            print(response)
            cls.ws.send(json.dumps(response))

    @classmethod
    def on_open(cls, ws: websocket) -> None:
        """
        :param ws: The connection to our websocket
        """
        # Subscribe to our websocket channel
        ws.send('{"event":"pusher:subscribe","data":{"auth":"","channel":"' + cls.channel + '"}}')

    @classmethod
    def on_message(cls, ws: websocket, message: str) -> None:
        """
        :param ws: The connection to our websocket
        :param message: The incoming message
        """
        cls.process_message(message)

    @classmethod
    def on_error(cls, ws: websocket, error: str) -> None:
        """
        :param ws: The connection to our websocket
        :param error: The corresponding error message
        """

        if "Caused by NewConnectionError" in str(error):
            #            Server.docker_client = None
            response = {'channel': WebSocket.channel,
                        'event': 'portal:error',
                        'error': 'Can not connect to docker',
                        }
            print(response)
            cls.ws.send(json.dumps(response))
        else:
            print("[ws_error]", error)

    @classmethod
    def on_close(cls, ws: websocket, close_status_code: int, close_msg: str) -> None:
        """
        :param ws: The connection to our websocket
        :param close_status_code: The status code of why the connection was closed
        :param close_msg: The message suggesting why the connection was closed
        """
        print("Retry : %s" % time.ctime())
        time.sleep(cls.timeout)
        cls.connect_websocket()


class WebSocketMessage:
    """
    server: Instance of our docker server
    """
    server = None

    def __init__(self) -> None:
        WebSocketMessage.server = Server()

    @classmethod
    def perform_action(cls, container_id: str, action: str) -> dict:
        """
        :param container_id: The full ID of the docker container
        :param action: The action we wish to perform
        :return: A dictionary containing the response from the server
        """
        error = container = None

        try:
            cls.server.perform_action(container_id, action)
            if action != 'remove':
                container = cls.get_container(container_id, None)
        except docker.errors.NotFound as e:
            error = "Container not found"
        except docker.errors.APIError as e:
            error = 'API Error: ' + str(e)

        return {
            'channel': WebSocket.channel,
            'event': 'portal:action-response',
            'container': container,
            'error': error,
            'reference': container_id,
            'action': action
        }

    @classmethod
    def get_ip(cls, container: 'Container', network: str = None) -> str:
        """
        Attempts to get the IP address from a running container
        :param container: The docker container object returned from the API
        :param network: The network the container is running on
        :return: The IP address
        """
        if network is None:
            networks = container.attrs['NetworkSettings']['Networks']
            if len(networks) > 0:
                network = next(iter(networks))

        ip = None
        if network is not None:
            if network in ['host', 'bridge']:
                ip = Server.DOCKER_HOST_IP
            else:
                ip = container.attrs['NetworkSettings']['Networks'][network]['IPAddress']

        return ip

    @classmethod
    def new_server(cls, data: list) -> dict:
        """
        Attempts to spin up a new docker server
        :param data: The image, container_name, environment and docker network
        :return: A dictionary containing the response from the server
        """
        error = container = None

        try:
            container = cls.server.run(image=data['docker_image'],
                                       name=data['container_name'],
                                       environment=data['environment'],
                                       network=data['docker_network'])

            total_seconds = None
            # Attempt to calculate how long the server has been running (only seconds at this point)
            if container.attrs['State']['Running']:
                total_seconds = cls.get_time_elapsed(container.attrs['State']['StartedAt']).total_seconds()

            container = {'id': container.id,
                         'name': container.name,
                         'ip': cls.get_ip(container, data['docker_network']),
                         'elapsed': total_seconds,
                         'status': container.status,
                         'image': data['docker_image'],
                         'network': data['docker_network']
                         }

        except docker.errors.NotFound as e:
            # The image or network was not found
            error = str(e)
        except docker.errors.APIError as e:
            # General docker API error
            error = 'API Error: ' + str(e)
        except docker.errors.DockerException:
            # Issues connecting to the docker host
            error = 'Could not connect to Docker'

        return {
            'channel': WebSocket.channel,
            'event': 'portal:server-created',
            'error': error,
            'container': container,
            'reference': data['server_id']
        }

    @classmethod
    def get_time_elapsed(cls, timestamp) -> timedelta:
        """
        :param timestamp: The timestamp when the docker container was started.
        :return: The number of seconds the docker container has been running.
        """
        fmt = '%Y-%m-%dT%H:%M:%S'
        timezone = pytz.timezone(config('TIMEZONE'))
        local_time = timezone.localize(datetime.now())

        tstamp1 = datetime.strptime(timestamp[0:19:1], fmt)
        tstamp1 = tstamp1 + local_time.utcoffset()
        tstamp2 = datetime.strptime(datetime.now().strftime(fmt), fmt)

        return tstamp1 - tstamp2 if tstamp1 > tstamp2 else tstamp2 - tstamp1

    @classmethod
    def get_container(cls, container_id: str, port: int) -> dict:
        """
        Attempt to get the details of a running container
        :param container_id: The full ID of the docker container
        :param port: The port of the running container (used for getting stats)
        :return: The dictionary response from the docker host
        """
        container = cls.server.get_server(container_id)

        total_seconds = None
        stats = None
        ip = None

        # Attempt to get stats of any running containers
        if container.attrs['State']['Running'] and not container.attrs['State']['Paused']:
            ip = cls.get_ip(container)
            total_seconds = cls.get_time_elapsed(container.attrs['State']['StartedAt']).total_seconds()

            result = container.exec_run("cat stats.json")
            # If the local server has generated stats
            if result.exit_code == 0:
                # Able to get stats from container
                decoded = result.output.decode("utf-8")
                decoded = decoded.replace("\'", '"')
                stats = json.loads(decoded)
            else:
                try:
                    image = container.image.tags[0]
                    # If it's a supported game, attempt to query the stats
                    if Query.SUPPORTED_IMAGES[image] and port is not None:
                        game = Query.SUPPORTED_IMAGES[image]
                        stats = asyncio.run(Query.process_game(game['protocol'], game['response'], ip, port, timeout=1))
                except KeyError:
                    pass

        return {'ip': ip,
                'elapsed': total_seconds,
                'stats': stats,
                'status': container.status
                }

    @classmethod
    def mcrcon(cls, reference, container_id: str, command: str) -> dict:
        """
        :param reference: Reference for this MC Rcon message
        :param container_id: The container ID to query
        :param command: The command we wish to execute
        :return:
        """
        container = cls.server.get_server(container_id)
        error = response = None

        # Only attempt on running containers
        if container.attrs['State']['Running'] and not container.attrs['State']['Paused']:
            envs = container.attrs['Config']['Env']
            rcon_password = 'DEFAULT_ADMIN_PASSWORD'
            for env in envs:
                if 'RCON_PASSWORD' in env:
                    key, rcon_password = env.split('=')
                    break

            result = container.exec_run('mcrcon -c -p "{}" "{}"'.format(rcon_password, command))
            response = result.output.decode("utf-8")
        else:
            error = 'Container not running'

        return {
            'channel': WebSocket.channel,
            'event': 'portal:mcrcon-response',
            'response': response,
            'error': error,
            'reference': reference,
            'command': command
        }


    @classmethod
    # Removed port
    def get_servers(cls, containers: list[str], ports: list[int]) -> dict:
        """
        Attempt to get the details of these containers with their corresponding game ports
        :param containers: A list of containers full IDs
        :param ports: A list of ports (for stats)
        :return: The list of server details
        """
        error = container = None
        servers = []

        for key, container_id in enumerate(containers):
            try:
                try:
                    port = ports[key]
                except KeyError:
                    port = None

                container = cls.get_container(container_id, port)
            except docker.errors.NotFound as e:
                error = "Container not found"
            except docker.errors.APIError as e:
                error = 'API Error: ' + str(e)
            except Exception as e:
                error = str(e)

            servers.append({
                'error': error,
                'container': container,
                'reference': container_id
            })

        return {
            'channel': WebSocket.channel,
            'event': 'portal:get-servers',
            'servers': servers,
        }
