import pytest

from exapi.bitget.v1.spot.client import (
    AccountTransfer,
    AccountTransferParams,
    ApiKeyInfo,
    Asset,
    Bill,
    BillParams,
    SubAccountAsset,
)


@pytest.mark.anyio
async def test_fetch_info(set_bitget_request_result, bitget_spot):
    set_bitget_request_result(
        {
            'user_id': '111222333',
            'inviter_id': None,
            'agent_inviter_code': None,
            'channel': 'eluosi',
            'ips': '',
            'authorities': ['trade', 'transfer', 'readonly'],
            'parentId': 111222333,
            'trader': False
        }
    )
    actual = await bitget_spot.fetch_info()

    assert isinstance(actual, ApiKeyInfo)


@pytest.mark.anyio
async def test_fetch_assets(set_bitget_request_result, bitget_spot):
    # set_bitget_request_result([])
    actual = await bitget_spot.fetch_assets()

    assert len(actual) == 2
    assert isinstance(actual, list)
    for item in actual:
        assert isinstance(item, Asset)


@pytest.mark.anyio
async def test_fetch_asset(set_bitget_request_result, bitget_spot):
    # set_bitget_request_result()
    actual = await bitget_spot.fetch_assets(coin='USDT')

    assert isinstance(actual, Asset)


@pytest.mark.anyio
async def test_fetch_sub_account_assets(set_bitget_request_result, bitget_spot):
    # set_bitget_request_result([])
    actual = await bitget_spot.fetch_sub_account_assets()

    assert len(actual) == 2
    assert isinstance(actual, list)
    for item in actual:
        assert isinstance(item, SubAccountAsset)


@pytest.mark.anyio
async def test_fetch_bills(set_bitget_request_result, bitget_spot):
    # set_bitget_request_result([])
    params = BillParams()
    actual = await bitget_spot.fetch_bills(param=params.dict(exclude_none=True, by_alias=True))

    assert len(actual) == 2
    assert isinstance(actual, list)
    for item in actual:
        assert isinstance(item, Bill)


@pytest.mark.anyio
async def test_fetch_transfers(set_bitget_request_result, bitget_spot):
    # set_bitget_request_result([])
    params = AccountTransferParams()
    actual = await bitget_spot.fetch_transfers(params=params.dict(exclude_none=True, by_alias=True))

    assert len(actual) == 2
    assert isinstance(actual, list)
    for item in actual:
        assert isinstance(item, AccountTransfer)
