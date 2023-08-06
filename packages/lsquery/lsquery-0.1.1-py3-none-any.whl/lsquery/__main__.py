from lsquery.web_socket import WebSocket
from lsquery.config import Config
import time


def main() -> None:
    Config.check_config()
    try:
        # Attempt to connect to the WebSocket and also docker.
        WebSocket()
    except Exception as err:
        print('[Docker Connect]', str(err))
    finally:
        # Keep the script running
        while True:
            time.sleep(60)


if __name__ == '__main__':
    main()
