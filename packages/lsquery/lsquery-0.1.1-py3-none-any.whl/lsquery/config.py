__author__ = "Brendon Taylor"
__email__ = "nuke@lanslide.com.au"
__status__ = "Production"

"""
Ensures the application has a valid environment file.
Additionally will allow the user to reconfigure existing values.

Use -c or --config to force configuration.
"""


from decouple import config
import getopt
import os
import sys


class Config:
    """
    DEFAULT_DOCKER_HOST: the default Docker host (if not defined already in .env)
    DEFAULT_WEBSOCKET_HOST: the default websocket host (if not defined already in .env)
    DEFAULT_TIMEZONE: the default timezone (used for time calculations)
    environ: Keeping track of the environment variables
    force_new_config: Whether to force the user to enter new configuration values
    """
    DEFAULT_DOCKER_HOST: str = 'unix:///var/run/docker.sock'
    DEFAULT_WEBSOCKET_HOST: str = 'portal.lanslide.com.au'
    DEFAULT_TIMEZONE: str = 'Australia/Melbourne'
    environ: dict = {}
    force_new_config: bool = False

    @classmethod
    def __read_value(cls, key: str, default_value: str = None) -> None:
        """
        :param key: The key we're trying to read
        :param default_value: The default value displayed to the user

        Read in a particular configuration key
        """
        value = None
        while value is None:
            try:
                if cls.force_new_config:
                    default_value = config(key)
                else:
                    value = config(key)
            except Exception as e:
                pass

            if value is None:
                prompt = 'Enter {}: '.format(key) if default_value is None else 'Enter {} [{}]: '.format(key,
                                                                                                         default_value)
                value = input(prompt)
                if len(value.strip()) == 0:
                    value = default_value if default_value is not None else None

        cls.environ[key] = value
        os.environ[key] = value

    @classmethod
    def __write_config(cls) -> None:
        """
        Write the environment variables to the configuration (.env) file.
        """
        root_dir = os.path.dirname(os.path.abspath(__file__))

        with open('{}/.env'.format(root_dir), "w") as f:
            for key, value in cls.environ.items():
                f.write("{}={}\n".format(key, value))

    @classmethod
    def check_config(cls) -> None:
        """
        Used to check whether we need to read in configuration values.
        """
        optlist, args = getopt.getopt(sys.argv[1:], 'c', ['config'])
        for opt, arg in optlist:
            if opt in ('-c', '--config'):
                cls.force_new_config = True

        cls.__read_value('DOCKER_HOST', cls.DEFAULT_DOCKER_HOST)
        cls.__read_value('WEBSOCKET_HOST', cls.DEFAULT_WEBSOCKET_HOST)
        cls.__read_value('WEBSOCKET_APP_KEY')
        cls.__read_value('TIMEZONE', cls.DEFAULT_TIMEZONE)
        cls.__write_config()
