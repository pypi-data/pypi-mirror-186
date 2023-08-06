import hmac


def sign(payload: str, secret: str) -> str:
    return hmac.new(
        key=bytes(secret, encoding='utf8'),
        msg=bytes(payload, encoding='utf-8'),
        digestmod='sha256',
    ).hexdigest()


def calc_hash(timestamp, secret, recv_window, data) -> str:
    return str(timestamp) + str(secret) + str(recv_window) + str(data)
