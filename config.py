import os
import logging
from logging.handlers import RotatingFileHandler

# Set the logs
VERBOSITY = os.getenv(
    "VERBOSITY", "debug"
)  # info as default, #debug for local dev

LOG_PATH = os.getenv("LOG_PATH", "./logs")


# Define the logs
# Set verbosity
def configure_logging(verbosity=VERBOSITY, log_path=LOG_PATH):
    log_level = logging.getLevelName(verbosity.upper())
    if isinstance(log_level, int):
        logging.basicConfig(
            level=log_level,
            format="[%(levelname)s] %(asctime)s | %(message)s | in function: %(funcName)s",
            handlers=[
                RotatingFileHandler(
                    os.path.join(log_path, "info.log"),
                    maxBytes=10000,
                    backupCount=10,
                ),
                logging.StreamHandler(),
            ],
        )
        result = True
    else:
        result = False
        raise NotImplementedError(
            f"Logging level {VERBOSITY.upper()} does not exist!"
        )
    return result


ROWS = 40
COLUMNS = 40
MAX_PROB = 2
MAX_TICK = 60
