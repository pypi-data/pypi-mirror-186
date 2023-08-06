import base64
import hmac


def sign(payload: str, secret: str) -> str:
    digest = hmac.new(
        key=bytes(secret, encoding='utf8'),
        msg=bytes(payload, encoding='utf-8'),
        digestmod='sha256',
    ).digest()

    return str(base64.b64encode(digest), encoding='utf8')


def calc_hash(timestamp, method, request_path, body='') -> str:
    return str(timestamp) + str.upper(method) + str(request_path) + str(body)
