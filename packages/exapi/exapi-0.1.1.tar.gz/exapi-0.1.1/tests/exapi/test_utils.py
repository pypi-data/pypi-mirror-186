import pytest

from exapi.utils import get_time_ms, to_camel, to_lower_camel, to_snake


@pytest.mark.parametrize(
    'text, expected',
    [
        ('snakesOnAPlane', 'snakes_on_a_plane'),
        ('SnakesOnAPlane', 'snakes_on_a_plane'),
        ('snakes_on_a_plane', 'snakes_on_a_plane'),
        ('myHTTPProto', 'my_http_proto'),
        ('otherHTTP2Proto', 'other_http2_proto'),
        ('HTTPResponseCodeXYZ', 'http_response_code_xyz'),
        ('IPhoneHysteria', 'i_phone_hysteria'),
        ('iPhoneHysteria', 'i_phone_hysteria'),
        ('_IPhone', '_i_phone'),
        ('__IPhone', '__i_phone'),
    ]
)
def test_to_snake(text, expected):
    actual = to_snake(text)

    assert isinstance(actual, str)
    assert actual == expected


@pytest.mark.parametrize(
    'text, expected',
    [
        ('snakes_on_a_plane', 'SnakesOnAPlane'),
        ('my_http_proto', 'MyHttpProto'),
        ('other_http2_proto', 'OtherHttp2Proto'),
        ('http_response_code_xyz', 'HttpResponseCodeXyz'),
        ('i_phone_hysteria', 'IPhoneHysteria'),
        ('_i_phone', 'IPhone'),
        ('__i_phone', 'IPhone'),
    ]
)
def test_to_camel(text, expected):
    actual = to_camel(text)

    assert isinstance(actual, str)
    assert actual == expected


@pytest.mark.parametrize(
    'text, expected',
    [
        ('snakes_on_a_plane', 'snakesOnAPlane'),
        ('my_http_proto', 'myHttpProto'),
        ('other_http2_proto', 'otherHttp2Proto'),
        ('http_response_code_xyz', 'httpResponseCodeXyz'),
        ('i_phone_hysteria', 'iPhoneHysteria'),
        ('_i_phone', 'iPhone'),
        ('__i_phone', 'iPhone'),
    ]
)
def test_to_lower_camel(text, expected):
    actual = to_lower_camel(text)

    assert isinstance(actual, str)
    assert actual == expected
