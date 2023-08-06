import pytest

from exapi.bitget.v1 import enums
from exapi.bitget.v1.spot.client import Candle, CandleParams, Depth, DepthParams, LastTrade, LastTradeParams, Ticker


@pytest.mark.anyio
async def test_fetch_ticker(set_bitget_request_result, bitget_spot):
    set_bitget_request_result(
        {
            'symbol': 'BTCUSDT',
            'high24h': '17392',
            'low24h': '17133.93',
            'close': '17203.23',
            'quoteVol': '256989756.1937',
            'baseVol': '14904.8162',
            'usdtVol': '256989756.193667',
            'ts': '1673323820030',
            'buyOne': '17203.22',
            'sellOne': '17203.67',
            'bidSz': '0.1983',
            'askSz': '0.0133',
            'openUtc0': '17180.7',
            'changeUtc': '0.00131',
            'change': '-0.00386'
        }
    )
    actual = await bitget_spot.fetch_ticker(symbol='BTCUSDT_SPBL')

    assert isinstance(actual, Ticker)


@pytest.mark.anyio
async def test_fetch_tickers(set_bitget_request_result, bitget_spot):
    set_bitget_request_result(
        [
            {
                'symbol': 'LINKUSDT',
                'high24h': '6.2526',
                'low24h': '5.9771',
                'close': '6.0766',
                'quoteVol': '2110088.5735',
                'baseVol': '344425.8118',
                'usdtVol': '2110088.57342502',
                'ts': '1673324086020',
                'buyOne': '6.073',
                'sellOne': '6.0779',
                'bidSz': '375.9703',
                'askSz': '65.8156',
                'openUtc0': '6.066',
                'changeUtc': '0.00195',
                'change': '-0.02048'
            },
            {
                'symbol': 'UNIUSDT',
                'high24h': '5.9676',
                'low24h': '5.7202',
                'close': '5.8144',
                'quoteVol': '1226237.6268',
                'baseVol': '210577.9105',
                'usdtVol': '1226237.62672047',
                'ts': '1673324086015',
                'buyOne': '5.8078',
                'sellOne': '5.8182',
                'bidSz': '17.9674',
                'askSz': '0.3962',
                'openUtc0': '5.7841',
                'changeUtc': '0.00524',
                'change': '-0.01536'
            }
        ]
    )
    actual = await bitget_spot.fetch_tickers()

    assert len(actual) == 2
    assert isinstance(actual, list)
    for item in actual:
        assert isinstance(item, Ticker)


@pytest.mark.anyio
async def test_fetch_fills(set_bitget_request_result, bitget_spot):
    set_bitget_request_result(
        [{
            'symbol': 'BTCUSDT_SPBL',
            'tradeId': '996560997378084865',
            'side': 'sell',
            'fillPrice': '17204.5',
            'fillQuantity': '0.5045',
            'fillTime': '1673324577659'
        }, {
            'symbol': 'BTCUSDT_SPBL',
            'tradeId': '996560976393981953',
            'side': 'sell',
            'fillPrice': '17204.16',
            'fillQuantity': '0.3277',
            'fillTime': '1673324572656'
        }]
    )
    params = LastTradeParams(symbol='BTCUSDT_SPBL', limit=2)
    actual = await bitget_spot.fetch_fills(params=params.dict(exclude_none=True))

    assert len(actual) == 2
    assert isinstance(actual, list)
    for item in actual:
        assert isinstance(item, LastTrade)


@pytest.mark.anyio
async def test_fetch_candles(set_bitget_request_result, bitget_spot):
    set_bitget_request_result(
        [{
            'open': '17000.2',
            'high': '17328.49',
            'low': '16920.26',
            'close': '17269.93',
            'quoteVol': '241235967.360077',
            'baseVol': '14084.1555',
            'usdtVol': '241235967.360077',
            'ts': '1673193600000'
        }, {
            'open': '17269.93',
            'high': '17392',
            'low': '17133.93',
            'close': '17202.4',
            'quoteVol': '138789133.554003',
            'baseVol': '8045.8045',
            'usdtVol': '138789133.554003',
            'ts': '1673280000000'
        }]
    )
    params = CandleParams(symbol='BTCUSDT_SPBL', period=enums.Interval.d1, limit=2)
    actual = await bitget_spot.fetch_candles(params=params.dict(exclude_none=True))

    assert len(actual) == 2
    assert isinstance(actual, list)
    for item in actual:
        assert isinstance(item, Candle)


@pytest.mark.anyio
async def test_fetch_depth(set_bitget_request_result, bitget_spot):
    set_bitget_request_result(
        {
            'asks': [['17204.2', '1.8816'], ['17204.28', '0.0581']],
            'bids': [['17203.62', '4.9302'], ['17203.52', '1.3499']],
            'timestamp': '1673324783407'
        }
    )
    params = DepthParams(symbol='BTCUSDT_SPBL', type=enums.DepthType.step0)
    actual = await bitget_spot.fetch_depth(params=params.dict(exclude_none=True))

    assert isinstance(actual, Depth)
