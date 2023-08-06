
import asyncio
from datetime import datetime
from jbg_util import binance_models
from jbg_util.basic_util import now
from jbg_util import trader_models

PriceTraderData,BalanceTraderData,OrderTraderData,AssetSymbol,OrderSide,OrderStatus,OrderType = trader_models.PriceTraderData,trader_models.BalanceTraderData,trader_models.OrderTraderData,trader_models.AssetSymbol,trader_models.OrderSide,trader_models.OrderStatus,trader_models.OrderType
PriceSocketData,BalanceSocketData,OrderSocketData,SocketEventType = binance_models.PriceSocketData,binance_models.BalanceSocketData,binance_models.OrderSocketData,binance_models.SocketEventType
class BinanceMockSocketDataUtil:
    @staticmethod
    def get_mock_price_socket_data(price : float = 16812.9811) -> PriceSocketData:
        price_data = PriceTraderData(
            event_type=SocketEventType.price_update,
            event_datetime=now(),
            symbol=AssetSymbol.BTC,
            price=price
        )
        return price_data.to_socket_data()

    @staticmethod
    def get_mock_balance_socket_data(btc_free : float=.00397067,btc_locked: float=.90397067,usd_free: float=30000.5623,usd_locked: float=2000.6754) -> BalanceSocketData:
        balance_data = BalanceTraderData(
            event_type=SocketEventType.balance_update,
            event_datetime=now(),
            btc_free=btc_free,
            btc_locked=btc_locked,
            usd_free=usd_free,
            usd_locked=usd_locked
        )
        return balance_data.to_socket_data()

    @staticmethod
    def get_mock_order_socket_data(order_id:int=1648660237,side:str=OrderSide.buy,qty:float=.01,filled_qty:float=.01,price:float=17200.5203,
        status:str=OrderStatus.filled,create_datetime:datetime=None,order_type:str=OrderType.limit) -> OrderSocketData:
        order_data = OrderTraderData(
            event_type=SocketEventType.order_update,
            event_datetime=now(),
            symbol=AssetSymbol.BTC,
            order_id=order_id,
            side=side,
            qty=qty,
            filled_qty=qty,
            price=price,
            status=status,
            order_type=order_type,
            create_datetime=create_datetime or now()
        )
        return order_data.to_socket_data()

    @staticmethod
    def get_static_mock_recv_fxn(delay,mock_data):
        async def mock_recv_fxn(self,socket_stream):
            await asyncio.sleep(delay)
            return mock_data
        return mock_recv_fxn

    @staticmethod
    def get_alternating_mock_recv_fxn(delays,mock_datas):
        global alternating_call_ct
        alternating_call_ct=-1
        async def mock_recv_fxn(self,socket_stream):
            global alternating_call_ct
            alternating_call_ct+=1
            idx = alternating_call_ct%len(mock_datas)
            await asyncio.sleep(delays[idx])
            return mock_datas[idx]
        return mock_recv_fxn

    @staticmethod
    def get_ending_mock_recv_fxn(delays,mock_datas):
        global ending_call_ct
        ending_call_ct=-1
        async def mock_recv_fxn(self,socket_stream):
            global ending_call_ct
            ending_call_ct+=1
            if ending_call_ct>=len(mock_datas):
                await asyncio.sleep(3600)
                return None
            await asyncio.sleep(delays[ending_call_ct])
            return mock_datas[ending_call_ct]
        return mock_recv_fxn
