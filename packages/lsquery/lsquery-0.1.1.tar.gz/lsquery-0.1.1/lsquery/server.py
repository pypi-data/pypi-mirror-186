__author__ = "Brendon Taylor"
__email__ = "nuke@lanslide.com.au"
__status__ = "Production"

"""
This class represents a docker game server.
It will use the Docker API to interact for docker.
"""

import docker
from decouple import config
import re


class Server:
    """
    FACT_SS_SRC: Factorio Server Settings Source file (local file system)
    FACT_SS_DEST: Factorio Server Settings Destination file (docker file system)
    FACT_RCON_FILE: Location of the rcon password file (docker file system)
    """
    FACT_SS_SRC = "/opt/factorio/data/server-settings.example.json"
    FACT_SS_DEST = "/factorio/config/server-settings.json"
    FACT_RCON_FILE = "/factorio/config/rconpw"

    """
    DOCKER_HOST_PROTOCOL: The protocol of the docker host connection.
    DOCKER_HOST_IP: The IP address of the docker host connection.
    DOCKER_HOST_PORT: The port of the docker host connection.
    """
    DOCKER_HOST_PROTOCOL = None
    DOCKER_HOST_IP = None
    DOCKER_HOST_PORT = None

    """
    client: Our docker client
    """
    docker_client = None

    def __init__(self):
        """
        Initialise our docker server settings and connection to our docker client.
        """
        matches = re.findall(r'^(.*):\/\/(.*):(.*)$', config('DOCKER_HOST'))
        # Save host details if present
        if len(matches) == 1:
            Server.DOCKER_HOST_PROTOCOL, Server.DOCKER_HOST_IP, Server.DOCKER_HOST_PORT = matches[0]

        Server.docker_client = docker.DockerClient(base_url=config('DOCKER_HOST'))

    @classmethod
    def perform_action(cls, container_id: str, action: str) -> None:
        """
        :param container_id: ID of the container
        :param action: action to perform
        :raises docker.errors.APIError: If the server returns an error
        """
        container_obj = cls.get_server(container_id)
        if action == 'remove':
            container_obj.remove(v=True, force=True)
        elif hasattr(container_obj, action) and callable(func := getattr(container_obj, action)):
            func()

    @classmethod
    def run(cls, image: str, name: str = None, environment: dict = None, network: str = None,
            publish_all_ports: bool = True, detach: bool = True, tty: bool = True) -> 'Container':
        """
        :param image: Name of the image
        :param name: Container name
        :param environment: Environment variables
        :param network: Network to use
        :param publish_all_ports: Whether to publish all ports to the docker host
        :param detach: Whether to detach from the running container
        :return: the created container
        :raises docker.errors.NotFound: One of the resources couldn't be found [image or network]
        :raises docker.errors.APIError: If the server returns an error
        """
        # Check the image exists
        if image is not None:
            try:
                cls.docker_client.images.get(image)
            except docker.errors.ImageNotFound:
                raise docker.errors.NotFound(f'Image "{image}" not found')

        # Check the network exists
        if network is not None:
            try:
                cls.docker_client.networks.get(network)
            except docker.errors.NotFound:
                raise docker.errors.NotFound(f'Network "{network}" not found')

        # Check the container name is not in use
        if name is not None:
            try:
                cls.docker_client.containers.get(name)
            except docker.errors.NotFound:
                pass
            else:
                raise docker.errors.APIError(f'Container name "/{name}" already in use')

        # Attach volumes
        volumes = {}
        if 'VOLUMES' in environment and environment['VOLUMES'] is not None:
            for volume in environment['VOLUMES'].split(','):
                src_path, dest_path = volume.split(':')
                volumes[src_path] = {'bind': dest_path, 'mode': 'rw'}

        entry = None

        if 'factorio' in image:
            is_public = str(environment['PUBLIC']).lower() if 'PUBLIC' in environment else 'false'
            # Save the RCON password to the rcon file
            rcon_command = "echo $RCON_PASSWORD" if 'RCON_PASSWORD' in environment else 'pwgen 15 1'

            # Save our Factorio configuration to our server settings file
            entry = f"/bin/sh -c 'mkdir -p /factorio/config && cp {cls.FACT_SS_SRC} {cls.FACT_SS_DEST} && "
            entry += r'sed -i -E "s|(\"name\": \").*\"|\1$INSTANCE_NAME\"|" ' + cls.FACT_SS_DEST + ' && '
            entry += r'sed -i -E "s|(\"description\": \").*\"|\1$INSTANCE_DESCRIPTION\"|" ' + cls.FACT_SS_DEST + ' && '
            entry += r'sed -i -E "s|(\"username\": \").*\"|\1$USERNAME\"|" ' + cls.FACT_SS_DEST + ' && '
            entry += r'sed -i -E "s|(\"token\": \").*\"|\1$TOKEN\"|" ' + cls.FACT_SS_DEST + ' && '
            entry += r'sed -i -E "s|(\"public\": ).*,|\1' + is_public + r',|" ' + cls.FACT_SS_DEST + ' && '
            entry += rcon_command + ' > ' + cls.FACT_RCON_FILE + ' && '
            entry += "exec /docker-entrypoint.sh'"

        hostname = environment['HOSTNAME'] if 'HOSTNAME' in environment else None

        # The CS:GO surf image requires a MariaDB database
        if 'csgo-surf' in image:
            mariadb = cls.get_server('mariadb')
            mariadb.start()

        return cls.docker_client.containers.run(
            image=image,
            name=name,
            hostname=hostname,
            environment=environment,
            network=network,
            publish_all_ports=publish_all_ports,
            detach=detach,
            entrypoint=entry,
            tty=tty,
            volumes=volumes)

    @classmethod
    def get_server(cls, container_id: str) -> 'Container':
        """
        :param container_id: ID of the container
        :return: the container object
        :raises docker.errors.ImageNotFound – If the container does not exist.
        :raises docker.errors.APIError – If the server returns an error.
        """
        return cls.docker_client.containers.get(container_id)


if __name__ == '__main__':
    server = Server()
    container = server.run('ioquake3')
    print(container.name)
    print(container.status)
