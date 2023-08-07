from os import path
from base64 import b64encode, b64decode
from contextlib import suppress
from functools import reduce
from hashlib import sha1
from imghdr import what
from hmac import new
from typing import Optional, Union, BinaryIO, Callable, Tuple, List
from uuid import uuid4
from io import BytesIO
from time import time, sleep as wait
from threading import Thread
from inspect import signature as inspect_signature
from random import randint
from ujson import dumps, loads
from websocket import WebSocket, WebSocketApp, WebSocketConnectionClosedException
from requests import get, Session as HTTPClient, Response as HTTPResponse
from requests.exceptions import ConnectionError, ReadTimeout, SSLError, ProxyError, ConnectTimeout
from requests_toolbelt import MultipartEncoder
from urllib.parse import urlencode
from retry import retry
from colorama import Fore, Style
from ..entities.messages import *
from ..entities.threads import *
from ..entities.handlers import *
from ..entities.userprofile import *
from ..entities.general import *
from ..entities.wsevents import *

def device_id() -> str:
    """
    `generate_device_id` Generates a device ID based on a specific string.

    `**Returns**`
    - `str` - Returns a device ID as a string.
    """
    encoded_data = sha1(str(uuid4()).encode('utf-8')).hexdigest()

    digest = new(
        b"\xe70\x9e\xcc\tS\xc6\xfa`\x00['e\xf9\x9d\xbb\xc9e\xc8\xe9",
        b"\x19" + bytes.fromhex(encoded_data),
        sha1).hexdigest()

    return f"19{encoded_data}{digest}"


def generate_signature(data: str) -> str:
    """
    `generate_signature` Generates a signature based on a specific string.
    
    `**Parameters**`
    - `data` - Data to generate a signature from
    `**Returns**`
    - `str` - Returns a signature as a string.
    """
    signature = [ 0x19 ]

    signature.extend(new(
        b'\xdf\xa5\xed\x19-\xdan\x88\xa1/\xe1!0\xdcb\x06\xb1%\x1eD',
        str(data).encode("utf-8"), sha1).digest())

    return b64encode(bytes(signature)).decode("utf-8")
