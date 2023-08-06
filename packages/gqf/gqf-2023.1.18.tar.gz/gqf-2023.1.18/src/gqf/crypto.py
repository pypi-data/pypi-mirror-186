import base64
import hashlib


def asciis2char(asciis: str, delimiter='/'):
    """
    把形如 “/119/101/108/99” 的 ascii 码转为字符
    支持分隔符
    """
    asciis = asciis.split(delimiter)
    char = ""
    for i in range(1, len(asciis)):
        char = char + chr(int(asciis[i]))
    return char


def b64decode(data: str):
    """
    Base64解码
    """
    if not isinstance(data, bytes): data = data.encode()
    decoded = base64.b64decode(data).decode()
    return decoded


def MD5(data: str):
    """
    返回值示例：15dfb80f464d81f01c215e938c2e960f
    """
    if not isinstance(data, bytes): data = data.encode()
    return hashlib.md5(data).hexdigest()


def MD5_16(data: str):
    """
    16 位的 md5
    从 32 位的结果中，提取中间的部分，即第 9 到第 24 位
    """
    if not isinstance(data, bytes): data = data.encode()
    return MD5(data)[8:24]


def SHA256(data: str):
    if not isinstance(data, bytes): data = data.encode()
    return hashlib.sha256(data).hexdigest()


def SHA3_256(data: str):
    if not isinstance(data, bytes): data = data.encode()
    return hashlib.sha3_256(data).hexdigest()


if __name__ == '__main__':
    print(b64decode('Z3Fm'))
    print(SHA256('CCDX_CTF'))
