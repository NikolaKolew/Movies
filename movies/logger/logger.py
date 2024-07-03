import logging


def setup_logger(name):
    """
    Setup logger for the given module name.

    :param name: str, name of the logger
    :return: logger instance
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)

    if not logger.handlers:
        logger.addHandler(ch)

    return logger
