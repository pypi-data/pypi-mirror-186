import base64
import hashlib
import random
from string import ascii_letters
from knifes.strings import ensure_bytes


def gfw_decode(content: str):
    b64_str = content[16:]
    index = b64_str.find('=')
    if index == -1:
        return b64decode(b64_str[::-1])
    else:
        return b64decode(b64_str[:index][::-1] + b64_str[index:])


def gfw_encode(content: str):
    b64_str = b64encode(content)
    index = b64_str.find('=')
    random_str = ''.join(random.choices(ascii_letters, k=16))
    if index == -1:
        return random_str + b64_str[::-1]
    else:
        return random_str + b64_str[:index][::-1] + b64_str[index:]


def b64encode(bytes_or_str):
    return base64.b64encode(ensure_bytes(bytes_or_str)).decode('utf-8')


def b64decode(bytes_or_str):
    return base64.b64decode(ensure_bytes(bytes_or_str)).decode('utf-8')


def b32encode(bytes_or_str):
    return base64.b32encode(ensure_bytes(bytes_or_str)).decode('utf-8')


def b32decode(bytes_or_str):
    return base64.b32decode(ensure_bytes(bytes_or_str)).decode('utf-8')


def md5(bytes_or_str):
    return hashlib.md5(ensure_bytes(bytes_or_str)).hexdigest()


