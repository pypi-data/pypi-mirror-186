import time

import pytest

from exapi.bybit.v3 import Result, enums
from exapi.bybit.v3.spot import (
    Account,
    Balance,
    BookTicker,
    Candle,
    CandlesParams,
    HistoryOrdersParams,
    HistoryTradesParams,
    OpenOrdersParams,
    Order,
    OrderBook,
    OrderCreate,
    OrderError,
    OrderParams,
    OrdersByIdCancel,
    OrdersCancel,
    PublicTrade,
    SpotHTTP,
    Symbol,
    SymbolInfo,
    TickerPrice,
    Trade,
)
from exapi.bybit.v3.spot.enums import OrderType


@pytest.mark.anyio
async def test_fetch_server_time(set_client_request_result, client):
    set_client_request_result({'serverTime': '1672894730735'})
    actual = await client.fetch_server_time()

    assert isinstance(actual, int)
    assert actual == 1672894730735


@pytest.mark.anyio
@pytest.mark.parametrize('timestamp_delta', [-2000, 6000])
async def test_sync_time_exc(monkeypatch, client, timestamp_delta):
    timestamp = int(time.time() * 1000)

    async def fetch_server_time(*args, **kwargs):
        return timestamp + timestamp_delta

    monkeypatch.setattr(client, 'recv_window', 5000)
    monkeypatch.setattr(SpotHTTP, 'fetch_server_time', fetch_server_time)

    with pytest.raises(RuntimeError) as exc_info:
        await client.sync_time()

    assert exc_info.type is RuntimeError


@pytest.mark.anyio
async def test_sync_time_normal(monkeypatch, client):
    timestamp = int(time.time() * 1000)

    async def fetch_server_time(*args, **kwargs):
        return timestamp

    monkeypatch.setattr(client, 'recv_window', 5000)
    monkeypatch.setattr(SpotHTTP, 'fetch_server_time', fetch_server_time)

    await client.sync_time()

    assert True


@pytest.mark.anyio
async def test_fetch_symbols(set_client_request_result, client):
    set_client_request_result(
        {
            'list': [{
                'name': 'BTCUSDT',
                'alias': 'BTCUSDT',
                'baseCoin': 'BTC',
                'quoteCoin': 'USDT',
                'basePrecision': '0.000001',
                'quotePrecision': '0.00000001',
                'minTradeQty': '0.000048',
                'minTradeAmt': '1',
                'maxTradeQty': '46.13',
                'maxTradeAmt': '938901',
                'minPricePrecision': '0.01',
                'category': '1',
                'showStatus': '1',
                'innovation': '0'
            }, {
                'name': 'ETHUSDT',
                'alias': 'ETHUSDT',
                'baseCoin': 'ETH',
                'quoteCoin': 'USDT',
                'basePrecision': '0.00001',
                'quotePrecision': '0.0000001',
                'minTradeQty': '0.00062',
                'minTradeAmt': '1',
                'maxTradeQty': '544.03',
                'maxTradeAmt': '700891',
                'minPricePrecision': '0.01',
                'category': '1',
                'showStatus': '1',
                'innovation': '0'
            }]
        }
    )
    actual = await client.fetch_symbols()

    assert len(actual) == 2
    assert isinstance(actual, list)
    for item in actual:
        assert isinstance(item, Symbol)


@pytest.mark.anyio
@pytest.mark.parametrize(
    'symbol, limit, result',
    [
        (enums.Symbol.BTCUSDT, 2, {
            'asks': [['16823.98', '0.335655'], ['16824', '0.000594']],
            'bids': [['16823.97', '0.932298'], ['16823.95', '0.4']],
            'time': 1672918570761,
        }),
        ('ETHUSDT', 3, {
            'asks': [['1252.07', '1.31879'], ['1252.18', '0.1766'], ['1252.29', '2']],
            'bids': [['1252.06', '7.44143'], ['1252.05', '3.50969'], ['1252.04', '8.01103']],
            'time': 1672919369861,
        }),
    ],
)
async def test_fetch_order_book(set_client_request_result, client, symbol, limit, result):
    set_client_request_result(result)

    actual = await client.fetch_order_book(
        symbol=symbol,
        limit=limit,
    )

    assert isinstance(actual, OrderBook)
    assert len(actual.asks) == limit
    assert len(actual.bids) == limit


@pytest.mark.anyio
@pytest.mark.parametrize(
    'symbol, scale, limit, result',
    [
        (enums.Symbol.BTCUSDT, 1, 3, {
            'asks': [['16817.6', '3.121435'], ['16818', '0.013945'], ['16818.2', '0.150055']],
            'bids': [['16817.5', '0.80669'], ['16817.4', '2.974924'], ['16817.3', '0.38662']],
            'time': 1672921826483,
        }),
        (enums.Symbol.ATOMUSDT, 3, 2, {
            'asks': [['10.074', '221.932'], ['10.075', '222.584']],
            'bids': [['10.071', '48.525'], ['10.07', '58.23']],
            'time': 1672921881464,
        }),
        ('ETHUSDT', 2, 3, {
            'asks': [['1252.15', '2.83429'], ['1252.18', '2'], ['1252.19', '3.57777']],
            'bids': [['1252.14', '10.13784'], ['1252.12', '0.53447'], ['1252.11', '2']],
            'time': 1672921934726,
        }),
    ],
)
async def test_fetch_merged_order_book(set_client_request_result, client, symbol, scale, limit, result):
    set_client_request_result(result)

    actual = await client.fetch_merged_order_book(
        symbol=symbol,
        scale=scale,
        limit=limit,
    )

    assert isinstance(actual, OrderBook)
    assert len(actual.asks) == limit
    assert len(actual.bids) == limit


@pytest.mark.anyio
@pytest.mark.parametrize(
    'symbol, limit, result',
    [
        (enums.Symbol.BTCUSDT, 2, {
            'list': [
                {'price': '16822.36', 'time': 1672924356496, 'qty': '0.000067', 'isBuyerMaker': 1, 'type': '0'},
                {'price': '16822.36', 'time': 1672924361928, 'qty': '0.04258', 'isBuyerMaker': 1, 'type': '0'},
            ]
        }),
        ('ETHUSDT', 3, {
            'list': [
                {'price': '1252.89', 'time': 1672924415180, 'qty': '0.09237', 'isBuyerMaker': 1, 'type': '0'},
                {'price': '1252.89', 'time': 1672924415282, 'qty': '0.0649', 'isBuyerMaker': 1, 'type': '0'},
                {'price': '1252.97', 'time': 1672924415282, 'qty': '0.01977', 'isBuyerMaker': 1, 'type': '0'},
            ]
        }),
    ],
)
async def test_fetch_public_trades(set_client_request_result, client, symbol, limit, result):
    set_client_request_result(result)

    actual = await client.fetch_public_trades(
        symbol=symbol,
        limit=limit,
    )

    assert len(actual) == limit
    assert isinstance(actual, list)
    for item in actual:
        assert isinstance(item, PublicTrade)


@pytest.mark.anyio
@pytest.mark.parametrize(
    'symbol, interval, limit, result',
    [
        (enums.Symbol.BTCUSDT, enums.Interval.d1, 2, {
            'list': [{
                't': 1672790400000,
                's': 'BTCUSDT',
                'sn': 'BTCUSDT',
                'c': '16852.43',
                'h': '16986.63',
                'l': '16654.86',
                'o': '16674.31',
                'v': '4274.157691',
            }, {
                't': 1672876800000,
                's': 'BTCUSDT',
                'sn': 'BTCUSDT',
                'c': '16809.86',
                'h': '16876.37',
                'l': '16786.01',
                'o': '16852.43',
                'v': '1070.677294',
            }],
        }),
        ('ETHUSDT', '30m', 1, {
            'list': [{
                't': 1672925400000,
                's': 'ETHUSDT',
                'sn': 'ETHUSDT',
                'c': '1249.44',
                'h': '1253.21',
                'l': '1248.25',
                'o': '1252.01',
                'v': '552.69695',
            }]
        }),
    ],
)
async def test_fetch_kline(set_client_request_result, client, symbol, interval, limit, result):
    set_client_request_result(result)

    actual = await client.fetch_kline(
        params=CandlesParams(
            symbol=symbol,
            interval=interval,
            limit=limit,
        ),
    )

    assert len(actual) == limit
    assert isinstance(actual, list)
    for item in actual:
        assert isinstance(item, Candle)


@pytest.mark.anyio
@pytest.mark.parametrize(
    'symbol, result',
    [
        (enums.Symbol.BTCUSDT, {
            't': 1672927246726,
            's': 'BTCUSDT',
            'bp': '16782.98',
            'ap': '16782.99',
            'lp': '16782.99',
            'o': '16826.17',
            'h': '16986.63',
            'l': '16760',
            'v': '3405.246007',
            'qv': '57363638.81214461',
        }),
        ('ETHUSDT', {
            't': 1672927283817,
            's': 'ETHUSDT',
            'bp': '1248.82',
            'ap': '1248.83',
            'lp': '1248.82',
            'o': '1253.55',
            'h': '1272.56',
            'l': '1242.39',
            'v': '34932.20675',
            'qv': '43819393.2291849',
        }),
    ],
)
async def test_fetch_symbol_info_with_params(set_client_request_result, client, symbol, result):
    set_client_request_result(result)

    actual = await client.fetch_symbol_info(symbol=symbol)

    assert isinstance(actual, SymbolInfo)
    assert actual.symbol == symbol


@pytest.mark.anyio
async def test_fetch_symbol_info_without_params(set_client_request_result, client):
    result = {
        'list': [{
            't': 1672927320000,
            's': 'XTZUSDT',
            'bp': '0.747',
            'ap': '0.75',
            'lp': '0.746',
            'o': '0.768',
            'h': '0.776',
            'l': '0.746',
            'v': '10875.73',
            'qv': '8303.42615',
        }, {
            't': 1672927338102,
            's': 'BITUSDT',
            'bp': '0.4118',
            'ap': '0.4119',
            'lp': '0.4118',
            'o': '0.3985',
            'h': '0.4174',
            'l': '0.3931',
            'v': '32979744.78',
            'qv': '13346746.181111',
        }],
    }
    set_client_request_result(result)

    actual = await client.fetch_symbol_info()

    assert len(actual) == 2
    assert isinstance(actual, list)
    for item in actual:
        assert isinstance(item, SymbolInfo)


@pytest.mark.anyio
@pytest.mark.parametrize(
    'symbol, result',
    [
        (enums.Symbol.BTCUSDT, {'symbol': 'BTCUSDT', 'price': '16807.98'}),
        ('ETHUSDT', {'symbol': 'ETHUSDT', 'price': '1249.23'}),
    ],
)
async def test_fetch_ticker_price_with_params(set_client_request_result, client, symbol, result):
    set_client_request_result(result)

    actual = await client.fetch_ticker_price(symbol=symbol)

    assert isinstance(actual, TickerPrice)
    assert actual.symbol == symbol


@pytest.mark.anyio
async def test_fetch_ticker_price_without_params(set_client_request_result, client):
    result = {
        'list': [
            {'symbol': 'CHZUSDT', 'price': '0.1106'},
            {'symbol': 'ADAUSDC', 'price': '0.2669'},
        ],
    }
    set_client_request_result(result)

    actual = await client.fetch_ticker_price()

    assert len(actual) == 2
    assert isinstance(actual, list)
    for item in actual:
        assert isinstance(item, TickerPrice)


@pytest.mark.anyio
@pytest.mark.parametrize(
    'symbol, result',
    [
        (enums.Symbol.BTCUSDT, {
            'symbol': 'BTCUSDT',
            'bidPrice': '16780.29',
            'bidQty': '0.17658',
            'askPrice': '16780.3',
            'askQty': '0.237004',
            'time': 1672930217357,
        }),
        ('ETHUSDT', {
            'symbol': 'ETHUSDT',
            'bidPrice': '1245.58',
            'bidQty': '0.99651',
            'askPrice': '1245.59',
            'askQty': '6.06971',
            'time': 1672930253639,
        }),
    ],
)
async def test_fetch_book_ticker_with_params(set_client_request_result, client, symbol, result):
    set_client_request_result(result)

    actual = await client.fetch_book_ticker(symbol=symbol)

    assert isinstance(actual, BookTicker)
    assert actual.symbol == symbol


@pytest.mark.anyio
async def test_fetch_book_ticker_without_params(set_client_request_result, client):
    result = {
        'list': [{
            'symbol': 'ADAUSDC',
            'bidPrice': '0.2645',
            'bidQty': '1696.48',
            'askPrice': '0.265',
            'askQty': '734.53',
            'time': 1672930043661,
        }, {
            'symbol': 'XRPUSDT',
            'bidPrice': '0.3389',
            'bidQty': '36625.03',
            'askPrice': '0.339',
            'askQty': '9265.41',
            'time': 1672930048277,
        }]
    }
    set_client_request_result(result)

    actual = await client.fetch_book_ticker()

    assert len(actual) == 2
    assert isinstance(actual, list)
    for item in actual:
        assert isinstance(item, BookTicker)


@pytest.mark.anyio
async def test_create_order(set_client_request_result, client):
    result = {
        'orderId': '1327741267846721280',
        'orderLinkId': '1673015093237810',
        'symbol': 'KASTAUSDT',
        'createTime': '1673015093247',
        'orderPrice': '0.5',
        'orderQty': '100.2',
        'orderType': 'LIMIT',
        'side': 'SELL',
        'status': 'NEW',
        'timeInForce': 'GTC',
        'accountId': '14165514',
        'execQty': '0',
        'orderCategory': 0,
    }
    set_client_request_result(result)

    actual = await client.create_order(
        params=OrderCreate(
            symbol=enums.Symbol.KASTAUSDT,
            order_qty=100.2,
            side=enums.Side.SELL,
            order_type=OrderType.LIMIT,
            order_price=0.5,
        ),
    )

    assert isinstance(actual, Order)
    assert actual.symbol == enums.Symbol.KASTAUSDT
    assert actual.side == enums.Side.SELL
    assert actual.order_qty == '100.2'
    assert actual.order_price == '0.5'


@pytest.mark.anyio
async def test_fetch_order(set_client_request_result, client):
    result = {
        'accountId': '14165514',
        'symbol': 'KASTAUSDT',
        'orderLinkId': '1673015093237810',
        'orderId': '1327741267846721280',
        'orderPrice': '0.5',
        'orderQty': '100.2',
        'execQty': '0',
        'cummulativeQuoteQty': '0',
        'avgPrice': '0',
        'status': 'CANCELED',
        'timeInForce': 'GTC',
        'orderType': 'LIMIT',
        'side': 'SELL',
        'stopPrice': '0.0',
        'icebergQty': '0.0',
        'createTime': '1673015093247',
        'updateTime': '1673015418756',
        'isWorking': '1',
        'locked': '0',
        'orderCategory': 0,
    }
    set_client_request_result(result)

    actual = await client.fetch_order(
        params=OrderParams(
            order_id='1327741267846721280',
        ),
    )

    assert isinstance(actual, Order)
    assert actual.order_id == '1327741267846721280'
    assert actual.order_link_id == '1673015093237810'
    assert actual.symbol == enums.Symbol.KASTAUSDT
    assert actual.side == enums.Side.SELL
    assert actual.order_qty == '100.2'
    assert actual.order_price == '0.5'


@pytest.mark.anyio
async def test_cancel_order(set_client_request_result, client):
    result = {
        'orderId': '1327753909160210176',
        'orderLinkId': '1673016600198905',
        'symbol': 'KASTAUSDT',
        'status': 'NEW',
        'accountId': '14165514',
        'createTime': '1673016600209',
        'orderPrice': '0.5',
        'orderQty': '100.2',
        'execQty': '0',
        'timeInForce': 'GTC',
        'orderType': 'LIMIT',
        'side': 'SELL',
        'orderCategory': 0
    }
    set_client_request_result(result)

    actual = await client.cancel_order(
        params=OrderParams(
            order_id='1327753909160210176',
        ),
    )

    assert isinstance(actual, Order)
    assert actual.order_id == '1327753909160210176'
    assert actual.order_link_id == '1673016600198905'
    assert actual.symbol == enums.Symbol.KASTAUSDT
    assert actual.side == enums.Side.SELL
    assert actual.order_qty == '100.2'
    assert actual.order_price == '0.5'


@pytest.mark.anyio
async def test_cancel_orders(set_client_request_result, client):
    result = {'success': '1'}
    set_client_request_result(result)

    actual = await client.cancel_orders(
        params=OrdersCancel(
            symbol=enums.Symbol.KASTAUSDT,
        ),
    )

    assert isinstance(actual, Result)
    assert actual.success == '1'


@pytest.mark.anyio
async def test_cancel_orders_by_ids(set_client_request_result, client):
    result = {
        'list': [
            {'orderId': '1327760365804631809', 'code': '12213'},
        ],
    }
    set_client_request_result(result)

    actual = await client.cancel_orders_by_ids(
        params=OrdersByIdCancel(
            order_ids='1327759943002111488,1327760365804631809',
        ),
    )

    assert isinstance(actual, list)
    for item in actual:
        assert isinstance(item, OrderError)


@pytest.mark.anyio
async def test_fetch_open_orders(set_client_request_result, client):
    result = {
        'list': [
            {
                'accountId': '14165514',
                'symbol': 'KASTAUSDT',
                'orderLinkId': '1673017877598847',
                'orderId': '1327764624734467840',
                'orderPrice': '0.5',
                'orderQty': '100.2',
                'execQty': '0',
                'cummulativeQuoteQty': '0',
                'avgPrice': '0',
                'status': 'NEW',
                'timeInForce': 'GTC',
                'orderType': 'LIMIT',
                'side': 'SELL',
                'stopPrice': '0.0',
                'icebergQty': '0.0',
                'createTime': 1673017877605,
                'updateTime': 1673017877612,
                'isWorking': '1',
                'orderCategory': 0,
            },
            {
                'accountId': '14165514',
                'symbol': 'KASTAUSDT',
                'orderLinkId': '1673017798055796',
                'orderId': '1327763957479521792',
                'orderPrice': '0.5',
                'orderQty': '100.2',
                'execQty': '0',
                'cummulativeQuoteQty': '0',
                'avgPrice': '0',
                'status': 'NEW',
                'timeInForce': 'GTC',
                'orderType': 'LIMIT',
                'side': 'SELL',
                'stopPrice': '0.0',
                'icebergQty': '0.0',
                'createTime': 1673017798062,
                'updateTime': 1673017798069,
                'isWorking': '1',
                'orderCategory': 0,
            },
        ],
    }
    set_client_request_result(result)

    actual = await client.fetch_open_orders(
        params=OpenOrdersParams(
            symbol=enums.Symbol.KASTAUSDT,
        ),
    )

    assert len(actual) == 2
    assert isinstance(actual, list)
    for item in actual:
        assert isinstance(item, Order)
        assert item.symbol == enums.Symbol.KASTAUSDT


@pytest.mark.anyio
async def test_fetch_history_orders(set_client_request_result, client):
    result = {
        'list': [
            {
                'accountId': '14165514',
                'symbol': 'XTZUSDT',
                'orderLinkId': '1671211103104',
                'orderId': '1312608303253133824',
                'orderPrice': '0.895',
                'orderQty': '134.27',
                'execQty': '134.27',
                'cummulativeQuoteQty': '120.17165',
                'avgPrice': '0.895',
                'status': 'FILLED',
                'timeInForce': 'GTC',
                'orderType': 'LIMIT',
                'side': 'BUY',
                'stopPrice': '0.0',
                'icebergQty': '0.0',
                'createTime': 1671211103289,
                'updateTime': 1671219052600,
                'isWorking': '1',
                'orderCategory': 0,
            },
            {
                'accountId': '14165514',
                'symbol': 'ATOMUSDT',
                'orderLinkId': '1671211062494',
                'orderId': '1312607962499427328',
                'orderPrice': '8.95',
                'orderQty': '33.519',
                'execQty': '33.519',
                'cummulativeQuoteQty': '299.99505',
                'avgPrice': '8.95',
                'status': 'FILLED',
                'timeInForce': 'GTC',
                'orderType': 'LIMIT',
                'side': 'BUY',
                'stopPrice': '0.0',
                'icebergQty': '0.0',
                'createTime': 1671211062668,
                'updateTime': 1671213861812,
                'isWorking': '1',
                'orderCategory': 0,
            },
        ],
    }
    set_client_request_result(result)

    actual = await client.fetch_history_orders(
        params=HistoryOrdersParams(
            start_time=1671169039000,
            limit=2,
        ),
    )

    assert len(actual) == 2
    assert isinstance(actual, list)
    for item in actual:
        assert isinstance(item, Order)


@pytest.mark.anyio
async def test_fetch_history_trades(set_client_request_result, client):
    result = {
        'list': [
            {
                'symbol': 'BTCUSDT',
                'id': '1312596072536840704',
                'orderId': '1312594748663503360',
                'tradeId': '2290000000033330026',
                'orderPrice': '16830',
                'orderQty': '0.1662',
                'execFee': '0',
                'feeTokenId': 'BTC',
                'creatTime': '1671209645253',
                'isBuyer': '0',
                'isMaker': '0',
                'matchOrderId': '1312596072335426048',
                'makerRebate': '0',
                'executionTime': '1671209645274',
            },
            {
                'symbol': 'ADAUSDT',
                'id': '1312767178715474944',
                'orderId': '1312607606629571072',
                'tradeId': '2260000000045397509',
                'orderPrice': '0.28',
                'orderQty': '1000',
                'execFee': '0',
                'feeTokenId': 'ADA',
                'creatTime': '1671230042706',
                'isBuyer': '0',
                'isMaker': '0',
                'matchOrderId': '1312767178572924672',
                'makerRebate': '0',
                'executionTime': '1671230042720',
            },
        ],
    }
    set_client_request_result(result)

    actual = await client.fetch_history_trades(
        params=HistoryTradesParams(),
    )

    assert len(actual) == 2
    assert isinstance(actual, list)
    for item in actual:
        assert isinstance(item, Trade)


@pytest.mark.anyio
async def test_fetch_account(set_client_request_result, client):
    result = {
        'balances': [
            {'coin': 'BTC', 'coinId': 'BTC', 'total': '0.0000046152', 'free': '0.0000046152', 'locked': '0'},
            {'coin': 'KASTA', 'coinId': 'KASTA', 'total': '224.775', 'free': '224.775', 'locked': '0'},
            {'coin': 'LUNC', 'coinId': 'LUNC', 'total': '10.461019', 'free': '10.461019', 'locked': '0'},
            {'coin': 'SHIB', 'coinId': 'SHIB', 'total': '2610.59', 'free': '2610.59', 'locked': '0'},
        ],
    }
    set_client_request_result(result)

    actual = await client.fetch_account()

    assert isinstance(actual, Account)
    assert isinstance(actual.balances, list)
    assert len(actual.balances) == 4
    for item in actual.balances:
        assert isinstance(item, Balance)
