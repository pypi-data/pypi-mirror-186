import pytest

from exapi.bitget.v1.spot.client import Currency, Product


@pytest.mark.anyio
async def test_fetch_server_time(set_bitget_request_result, bitget_spot):
    set_bitget_request_result('1673318403673')
    actual = await bitget_spot.fetch_server_time()

    assert isinstance(actual, int)
    assert actual == 1673318403673


@pytest.mark.anyio
async def test_fetch_currencies(set_bitget_request_result, bitget_spot):
    set_bitget_request_result(
        [
            {
                'coinId': '1',
                'coinName': 'BTC',
                'transfer': 'true',
                'chains': [
                    {
                        'chain': 'BTC',
                        'needTag': 'false',
                        'withdrawable': 'true',
                        'rechargeable': 'true',
                        'withdrawFee': '0.0005',
                        'extraWithDrawFee': '0',
                        'depositConfirm': '1',
                        'withdrawConfirm': '1',
                        'minDepositAmount': '0.0006',
                        'minWithdrawAmount': '0.008',
                        'browserUrl': 'https://blockchair.com/bitcoin/transaction/'
                    },
                    {
                        'chain': 'BEP20',
                        'needTag': 'false',
                        'withdrawable': 'true',
                        'rechargeable': 'true',
                        'withdrawFee': '0.0000051',
                        'extraWithDrawFee': '0',
                        'depositConfirm': '15',
                        'withdrawConfirm': '15',
                        'minDepositAmount': '0.0001',
                        'minWithdrawAmount': '0.001',
                        'browserUrl': 'https://bscscan.com/tx/'
                    },
                ],
            },
            {
                'coinId': '2',
                'coinName': 'USDT',
                'transfer': 'true',
                'chains': [
                    {
                        'chain': 'ERC20',
                        'needTag': 'false',
                        'withdrawable': 'true',
                        'rechargeable': 'true',
                        'withdrawFee': '3.0638816',
                        'extraWithDrawFee': '0',
                        'depositConfirm': '12',
                        'withdrawConfirm': '1',
                        'minDepositAmount': '1',
                        'minWithdrawAmount': '1',
                        'browserUrl': 'https://etherscan.io/tx/'
                    },
                    {
                        'chain': 'TRC20',
                        'needTag': 'false',
                        'withdrawable': 'true',
                        'rechargeable': 'true',
                        'withdrawFee': '0.5',
                        'extraWithDrawFee': '0',
                        'depositConfirm': '1',
                        'withdrawConfirm': '1',
                        'minDepositAmount': '1',
                        'minWithdrawAmount': '1',
                        'browserUrl': 'https://tronscan.org/#/transaction/'
                    },
                ],
            },
        ],
    )
    actual = await bitget_spot.fetch_currencies()

    assert len(actual) == 2
    assert isinstance(actual, list)
    for item in actual:
        assert isinstance(item, Currency)


@pytest.mark.anyio
async def test_fetch_products(set_bitget_request_result, bitget_spot):
    set_bitget_request_result(
        [
            {
                'symbol': 'TRXUSDT_SPBL',
                'symbolName': 'TRXUSDT',
                'baseCoin': 'TRX',
                'quoteCoin': 'USDT',
                'minTradeAmount': '1',
                'maxTradeAmount': '0',
                'takerFeeRate': '0.002',
                'makerFeeRate': '0.002',
                'priceScale': '6',
                'quantityScale': '4',
                'status': 'online',
                'minTradeUSDT': '5'
            },
            {
                'symbol': 'LINKUSDT_SPBL',
                'symbolName': 'LINKUSDT',
                'baseCoin': 'LINK',
                'quoteCoin': 'USDT',
                'minTradeAmount': '0',
                'maxTradeAmount': '0',
                'takerFeeRate': '0.002',
                'makerFeeRate': '0.002',
                'priceScale': '4',
                'quantityScale': '4',
                'status': 'online',
                'minTradeUSDT': '5'
            },
        ]
    )
    actual = await bitget_spot.fetch_products()

    assert len(actual) == 2
    assert isinstance(actual, list)
    for item in actual:
        assert isinstance(item, Product)


@pytest.mark.anyio
async def test_fetch_product(set_bitget_request_result, bitget_spot):
    set_bitget_request_result(
        {
            'symbol': 'btcusdt_SPBL',
            'symbolName': None,
            'baseCoin': 'BTC',
            'quoteCoin': 'USDT',
            'minTradeAmount': '0.0001',
            'maxTradeAmount': '0',
            'takerFeeRate': '0.002',
            'makerFeeRate': '0.002',
            'priceScale': '2',
            'quantityScale': '4',
            'status': 'online',
            'minTradeUSDT': None
        }
    )
    actual = await bitget_spot.fetch_product(symbol='BTCUSDT_SPBL')

    assert isinstance(actual, Product)
    assert actual.symbol == 'BTCUSDT_SPBL'
