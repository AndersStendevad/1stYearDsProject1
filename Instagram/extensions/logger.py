import logging
import sys

def get_logger():
    logging.basicConfig(format="%(asctime)s %(message)s")

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    handler.setFormatter(formatter)

    # logger.addHandler(handler)

    return logger

