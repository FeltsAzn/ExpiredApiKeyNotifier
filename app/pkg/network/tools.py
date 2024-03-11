import asyncio
import functools
import json
import random
from typing import Any

from aiohttp import client_exceptions

from config import PROXY_LIST, PROXY_ON
from utils import log


def retry(init_retries: int = 3) -> Any:
    def send_request(func):
        @functools.wraps(func)
        async def wrap(*args, **kwargs):
            delay_range = [i / 10 for i in range(10, 31)]
            retries = init_retries
            while retries:
                try:
                    return await func(*args, **kwargs)
                except json.decoder.JSONDecodeError as ex:

                    log.debug(f"retry={retries}, func={func.__name__}, type{type(ex)} "
                              f"description={ex}, args={args}, kwargs={kwargs}")
                    await asyncio.sleep(random.choice(delay_range))
                except ConnectionError as ex:
                    log.debug(f"retry={retries}, func={func.__name__}, type{type(ex)} "
                              f"description={ex}, args={args}, kwargs={kwargs}")
                    await asyncio.sleep(random.choice(delay_range))
                    retries -= 1
                except client_exceptions.ClientProxyConnectionError as ex:
                    log.debug(f"retry={retries}, func={func.__name__}, type{type(ex)}, "
                              f"description={ex}, args={args}, kwargs={kwargs}")
                except client_exceptions.ClientOSError as ex:
                    log.debug(f"retry={retries}, func={func.__name__}, type{type(ex)}, "
                              f"description={ex}, args={args}, kwargs={kwargs}")
                    await asyncio.sleep(random.choice(delay_range))
                    retries -= 1
                except client_exceptions.ServerDisconnectedError as ex:
                    log.debug(f"retry={retries}, func={func.__name__}, type{type(ex)}, "
                              f"description={ex}, args={args}, kwargs={kwargs}")
                    await asyncio.sleep(random.choice(delay_range))
                    retries -= 1
                except client_exceptions.ClientPayloadError as ex:
                    log.debug(f"retry={retries}, func={func.__name__}, type{type(ex)}, "
                              f"description={ex}, args={args}, kwargs={kwargs}")
                    await asyncio.sleep(random.choice(delay_range))
                    retries -= 1
                except KeyError as ex:
                    log.debug(f"retry={retries}, func={func.__name__}, type{type(ex)} "
                              f"description={ex}, args={args}, kwargs={kwargs}")
                    await asyncio.sleep(random.choice(delay_range))
                    retries -= 1
                except Exception as ex:
                    error_message = f"Unexpected error. retry={retries}, func={func.__name__}, " \
                                    f"type{type(ex)} description={ex}, args={args}, kwargs={kwargs}"
                    log.error(error_message)
                    retries -= 1
                    await asyncio.sleep(random.choice(delay_range))
                finally:
                    if retries == 0:
                        error_message = f"All retries is finished. " \
                                        f"Connection denied. args={args}, kwargs={kwargs}"
                        log.exception(error_message)
                        return []

        return wrap

    return send_request


def get_proxy() -> str | None:
    if PROXY_ON:
        return random.choice(PROXY_LIST)
    return None
