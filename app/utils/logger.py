import logging

logging.basicConfig(
    format="[%(asctime)s] [%(processName)s] [%(levelname)s]: %(message)s [%(filename)s/%(funcName)s:%(lineno)d]",
    encoding="utf-8",
    level="INFO")
log = logging.getLogger("main")
