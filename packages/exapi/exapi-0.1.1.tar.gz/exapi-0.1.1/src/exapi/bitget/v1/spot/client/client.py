from exapi.bitget.v1.client import BaseClient
from exapi.bitget.v1.spot.client.account import Account
from exapi.bitget.v1.spot.client.market import Market
from exapi.bitget.v1.spot.client.public import Public
from exapi.bitget.v1.spot.client.trade import Trade
from exapi.bitget.v1.spot.client.wallet import Wallet


class SpotClient(BaseClient, Account, Market, Public, Trade, Wallet):
    pass
