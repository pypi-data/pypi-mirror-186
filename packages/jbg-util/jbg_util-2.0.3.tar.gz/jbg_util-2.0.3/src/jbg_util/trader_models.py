from __future__ import annotations
from datetime import datetime
from dataclasses import dataclass,asdict

from jbg_util import binance_models #SocketData,OrderSocketData,PriceSocketData,BalanceSocketData,AssetBalance
from jbg_util import binance_util

binance_timestamp_to_dte,dte_to_binance_timestamp = binance_util.binance_timestamp_to_dte,binance_util.dte_to_binance_timestamp
SocketData,OrderSocketData,PriceSocketData,BalanceSocketData,AssetBalance = \
    binance_models.SocketData,binance_models.OrderSocketData,binance_models.PriceSocketData,binance_models.BalanceSocketData,binance_models.AssetBalance

class AssetSymbol:
    BTC = 'BTC'
    USD = 'USD'

def convert_socket_to_trader_data(data):
    if isinstance(data,BalanceSocketData):
        return BalanceTraderData.from_socket_data(data)
    elif isinstance(data,PriceSocketData):
        return PriceTraderData.from_socket_data(data)
    elif isinstance(data,OrderSocketData):
        return OrderTraderData.from_socket_data(data)
    raise ValueError("unrecognized datatype: ",type(data))

class OrderSide:
    buy = 'BUY'
    sell = 'SELL'

@dataclass
class OrderStatus:
    filled = 'FILLED'
    new = 'NEW'
    partially_filled = 'PARTIALLY_FILLED'
    canceled = 'CANCELED'
    pending_cancel = 'PENDING_CANCEL'
    rejected = 'REJECTED'
    expired = 'EXPIRED'

class OrderType:
    limit = 'LIMIT'
    market = 'MARKET'

@dataclass
class TraderData:
    event_type : str
    event_datetime : datetime

    @staticmethod
    def from_socket_data(socket_data : SocketData) -> TraderData:
        return TraderData(
            event_type=socket_data.e,
            event_datetime=binance_timestamp_to_dte(socket_data.E)
        )

@dataclass
class PriceTraderData(TraderData):
    symbol : str
    price : float

    def to_socket_data(self) -> PriceSocketData:
        return PriceSocketData(
            E=dte_to_binance_timestamp(self.event_datetime),
            e=self.event_type,
            s=self.symbol,
            c=self.price
        )

    @staticmethod
    def from_socket_data(socket_data : PriceSocketData) -> PriceTraderData:
        trader_data = TraderData.from_socket_data(socket_data)
        return PriceTraderData(
            **asdict(trader_data),
            symbol=socket_data.s,
            price = socket_data.c
        )

@dataclass
class OrderTraderData(TraderData):
    symbol : str
    order_id : int
    order_type : str
    side : str
    qty : float
    filled_qty : float
    price : float
    status : str
    create_datetime : datetime

    def to_socket_data(self) -> OrderSocketData:
        return OrderSocketData(
            E=dte_to_binance_timestamp(self.event_datetime),
            e=self.event_type,
            s=self.symbol,
            i=self.order_id,
            S=self.side,
            q=self.qty,
            z=self.filled_qty,
            p=self.price,
            X=self.status,
            o=self.order_type,
            O=dte_to_binance_timestamp(self.create_datetime)
        )

    @staticmethod
    def from_socket_data(socket_data : OrderSocketData) -> OrderTraderData:
        trader_data = TraderData.from_socket_data(socket_data)
        return OrderTraderData(
            **asdict(trader_data),
            symbol=socket_data.s,
            order_id=socket_data.i,
            side=socket_data.S,
            qty=socket_data.q,
            filled_qty=socket_data.z,
            price=socket_data.p,
            status=socket_data.X,
            order_type=socket_data.o,
            create_datetime=binance_timestamp_to_dte(socket_data.O)
        )

@dataclass
class TraderAssetBalance:
    free : float
    locked : float

@dataclass
class BalanceTraderData(TraderData):
    btc_free : float
    btc_locked : float
    usd_free : float
    usd_locked : float

    def to_socket_data(self) -> BalanceSocketData:
        return BalanceSocketData(
            E=dte_to_binance_timestamp(self.event_datetime),
            e=self.event_type,
            B=[
                AssetBalance(
                    a = AssetSymbol.BTC,
                    f= self.btc_free,
                    l=self.btc_locked
                ),
                AssetBalance(
                    a = AssetSymbol.USD,
                    f=self.usd_free,
                    l=self.usd_locked
                )
            ]
        )

    @staticmethod
    def from_socket_data(socket_data : BalanceSocketData) -> BalanceTraderData:
        btc_qtys = None
        usd_qtys = None
        for bal in socket_data.B:
            if bal.a=='BTC':
                btc_qtys=[bal.f, bal.l]
            elif bal.a=='USD':
                usd_qtys=[bal.f, bal.l]

        trader_data = TraderData.from_socket_data(socket_data)
        return BalanceTraderData(
            **asdict(trader_data),
            btc_free=btc_qtys[0],
            btc_locked=btc_qtys[1],
            usd_free=usd_qtys[0],
            usd_locked=usd_qtys[1]
        )


