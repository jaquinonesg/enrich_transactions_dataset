import logging

logging.basicConfig(
    filename="logs.log",
    filemode="a",
    format="%(asctime)s %(message)s",
    level=logging.WARNING,
)
