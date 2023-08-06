__author__ = "Brendon Taylor"
__email__ = "nuke@lanslide.com.au"
__status__ = "Production"

"""
Using the opengsq (Open Game Server Query) module we attempt to get the stats for a particular game host.
Most of this will be done with a local python script on each server, this is the backup option.
"""

import asyncio
from opengsq.protocols.ase import ASE
from opengsq.protocols.minecraft import Minecraft
from opengsq.protocols.quake3 import Quake3
from opengsq.protocols import Source


class Query:
    ASE_RESPONSE: list[str] = ['gamename', 'hostname', 'map', 'password', 'maxplayers']
    MINECRAFT_RESPONSE: list[str] = ['description', 'players', 'version']
    QUAKE3_RESPONSE: list[str] = ['sv_maxclients', 'g_humanplayers', 'clients', 'mapname', 'hostname']
    SOURCE_RESPONSE: list[str] = ['Name', 'Map', 'Players', 'MaxPlayers', 'GamePort']

    SUPPORTED_IMAGES: dict = {
        '7days:latest': {'protocol': Source, 'response': SOURCE_RESPONSE},
        'csgo-ar:latest': {'protocol': Source, 'response': SOURCE_RESPONSE},
        'csgo-bots:latest': {'protocol': Source, 'response': SOURCE_RESPONSE},
        'csgo-comp:latest': {'protocol': Source, 'response': SOURCE_RESPONSE},
        'csgo-dm:latest': {'protocol': Source, 'response': SOURCE_RESPONSE},
        'csgo-surf:latest': {'protocol': Source, 'response': SOURCE_RESPONSE},
        'csgo-wingman:latest': {'protocol': Source, 'response': SOURCE_RESPONSE},
        'hl2:latest': {'protocol': Source, 'response': SOURCE_RESPONSE},
        'ioquake3:latest': {'protocol': Quake3, 'response': QUAKE3_RESPONSE},
        'itzg/minecraft-server:latest': {'protocol': Minecraft, 'response': MINECRAFT_RESPONSE}
    }

    @classmethod
    def __process_info(cls, response: dict, response_keys: list[str]) -> dict:
        """
        :param response: The response received from the game server.
        :param response_keys: The keys we wish to keep from the response.
        :return: A dictionary containing our new "processed" response
        """
        result = {}
        for tag in response_keys:
            result[tag] = response[tag]
        return result

    @classmethod
    async def process_game(cls, protocol: callable, response_keys: list[str], address: str, query_port: int, timeout: float = 5.0) -> dict:
        """
        :param protocol: The function we'll use to query the game server.
        :param response_keys: The keys we wish to keep from the response.
        :param address: The IP address of the server host.
        :param query_port: The port of the server host.
        :param timeout: The query timeout before a Timeout error will be returned.
        :return:
        """
        try:
            response = protocol(address=address, query_port=query_port, timeout=timeout)
            if protocol in [ASE, Minecraft]:
                response = await response.get_status()
            else:
                response = await response.get_info()
            return cls.__process_info(response=response, response_keys=response_keys)
        except asyncio.exceptions.TimeoutError:
            return {'Error': 'Timeout'}


if __name__ == '__main__':
    pass
    # 7 days [WORKING]
    # print(asyncio.run(Query.process_game(Source, Query.SOURCE_RESPONSE, '192.168.1.129', 26900, timeout=1)))
    # CS:GO [WORKING]
    # print(asyncio.run(Query.process_game(Source, Query.SOURCE_RESPONSE, '192.168.1.130', 27015, timeout=1)))
    # Factorio
    # print(asyncio.run(Query.process_game(ASE, Query.ASE_RESPONSE, '192.168.1.129', 34197, timeout=10)))
    # HL2 [WORKING]
    # print(asyncio.run(Query.process_game(Source, Query.SOURCE_RESPONSE, '192.168.1.131', 27015, timeout=1)))
    # Minecraft [WORKING]
    # print(asyncio.run(Query.process_game(Minecraft, Query.MINECRAFT_RESPONSE, '192.168.1.132', 25565, timeout=1)))
    # Quake 3 [WORKING]
    # print(asyncio.run(Query.process_game(Quake3, Query.QUAKE3_RESPONSE, '192.168.1.128', 27960, timeout=1)))
    # Retrocycles
    # print(asyncio.run(Query.process_game(ASE, Query.ASE_RESPONSE, '192.168.1.133', 4534, timeout=1)))
    # Satisfactory
    # print(asyncio.run(Query.process_game(ASE, Query.ASE_RESPONSE, '192.168.1.133', 7777, timeout=1)))
    # Rust
    # print(asyncio.run(Query.process_game(Source, Query.SOURCE_RESPONSE, '192.168.1.129', 28017, timeout=3)))
