import logging

# setup logger
logging.basicConfig(format="{asctime} {levelname}: pagex-stocks-data - {name}s - {message}",
                    datefmt="%d.%m.%Y %H:%M:%S",
                    style="{", level=logging.INFO,
                    force=True)
logging.getLogger("sqlalchemy").setLevel(logging.ERROR)
