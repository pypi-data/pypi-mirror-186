from __future__ import annotations
from dataclasses import dataclass
from jbg_util import trader_models
from jbg_util import websocket_util
from jbg_util import pub_sub_mediator
from jbg_util import logging_util
from jbg_util import circular_buffer
#from jbg_util.trader_engine_states import RallyTraderEngineState,PostRallyTraderEngineState,DumpTraderEngineState,PostDumpTraderEngineState,WarmingUpTraderEngineState,StableTraderEngineState,TraderEngineStateName,TraderEngineState

CircularBuffer = circular_buffer.CircularBuffer
Logger = logging_util.Logger
PubSubMediator = pub_sub_mediator.PubSubMediator
SocketChannel,PriceSocketData,OrderSocketData,BalanceSocketData = websocket_util.SocketChannel,websocket_util.PriceSocketData,websocket_util.OrderSocketData,websocket_util.BalanceSocketData
PriceTraderData,OrderTraderData,BalanceTraderData,TraderAssetBalance,AssetSymbol = \
    trader_models.PriceTraderData,trader_models.OrderTraderData,trader_models.BalanceTraderData,trader_models.TraderAssetBalance,trader_models.AssetSymbol
class TraderEngineDataType:
    price = 1
    balance = 2
    order = 3
@dataclass
class TraderEngineStateName:
    warming_up='warming_up'
    rally='rally'
    post_rally='post_rally'
    dump='dump'
    post_dump = 'post_dump'
    stable='stable'

class TraderEngineState:
    state_name : str = None

    def __init__(self,data : TraderEngineData,logger : Logger):
        self.logger : Logger = logger
        self.data : TraderEngineData = data

    def start(self):
        self.logger.warning(f'Starting new trader state: {self.state_name}')

    def end(self):
        self.logger.warning(f'Ending trader state: {self.state_name}')

    def do(self):
        self.logger.info(f'Doing trader state: {self.state_name}. Latest price={self.latest_price}')

    def next_state(self) -> str:
        return self.state_name
        #raise NotImplementedError("Cannot execute next_state on a generic TraderEngineState.")

    @property
    def oldest_price(self):
        return self.data.prices.oldest.data.price

    @property
    def latest_price(self):
        return self.data.prices.latest.data.price

    def is_dump(self):
        if self.oldest_price-self.latest_price > self.data.prices.capacity:
            return True
        return False

    def is_rally(self):
        if self.latest_price-self.oldest_price > self.data.prices.capacity:
            return True
        return False

class RallyTraderEngineState(TraderEngineState):
    state_name : str = TraderEngineStateName.rally
class PostRallyTraderEngineState(TraderEngineState):
    state_name : str= TraderEngineStateName.post_rally
class DumpTraderEngineState(TraderEngineState):
    state_name : str= TraderEngineStateName.dump
class PostDumpTraderEngineState(TraderEngineState):
    state_name : str = TraderEngineStateName.post_dump
class WarmingUpTraderEngineState(TraderEngineState):
    state_name : str = TraderEngineStateName.warming_up

    def next_state(self) -> str:
        if self.data.prices.curr_size!=self.data.prices.capacity:
            return TraderEngineStateName.warming_up
        if self.is_dump():
            return TraderEngineStateName.dump
        if self.is_rally():
            return TraderEngineStateName.rally
        return TraderEngineStateName.stable

class StableTraderEngineState(TraderEngineState):
    state_name : str = TraderEngineStateName.stable

    def next_state(self) -> str:
        if self.is_dump():
            return TraderEngineStateName.dump
        if self.is_rally():
            return TraderEngineStateName.rally
        return TraderEngineStateName.stable

class TraderEngine:
    data : TraderEngineData
    curr_state : TraderEngineState
    states : dict #[str : TraderEngineState]
    logger : Logger

    def __init__(self, mediator : PubSubMediator,logger : Logger = None, max_num_prices : int= 10):
        self.subscribe_for_updates(mediator)
        self.logger = logger or Logger('./logs/trader_engine.log',should_print_to_screen=True).empty_log()
        self.data = TraderEngineData(self.logger,max_num_prices)

        self.states = {
            cls.state_name : cls(self.data,self.logger) for cls in [RallyTraderEngineState,PostRallyTraderEngineState,
                DumpTraderEngineState,PostDumpTraderEngineState,WarmingUpTraderEngineState,StableTraderEngineState]
        }
        self.curr_state=self.states[TraderEngineStateName.warming_up]

    # def get_trader_state_by_name(state_name : str):

    def subscribe_for_updates(self,mediator : PubSubMediator):
        mediator.subscribe_local_fxn(self.on_price_update,SocketChannel.price)
        mediator.subscribe_local_fxn(self.on_order_update,SocketChannel.order)
        mediator.subscribe_local_fxn(self.on_balance_update,SocketChannel.balance)

    @property
    def prices(self) -> CircularBuffer[PriceTraderData]:
        return self.data.prices

    @property
    def balances(self) -> dict[str:TraderAssetBalance]:
        return self.data.balances

    @property
    def orders(self) -> dict[str:OrderTraderData]:
        return self.data.orders

    def change_state(self,new_state_name : str):
        self.logger.warning(f'Changing state from {self.curr_state.state_name} to {new_state_name}')
        new_state = self.states[new_state_name]

        self.curr_state.end()
        new_state.start()
        #new_state.do()

        self.curr_state = new_state

    def on_any_update(self):
        next_state=self.curr_state.next_state()
        if next_state != self.curr_state.state_name:
            # self.logger.warning(f'CHANGING STATE! {next_state}, {self.curr_state.state_name}')
            self.change_state(next_state)
        self.curr_state.do()

    async def on_price_update(self,data : PriceSocketData,channel):
        trader_data = PriceTraderData.from_socket_data(data)
        self.logger.success(f'Received price update: {trader_data}')
        self.data.on_price_update(trader_data)
        #self.data.prices.add(trader_data)
        self.on_any_update()

    async def on_order_update(self,data : OrderSocketData,channel):
        trader_data = OrderTraderData.from_socket_data(data)
        self.logger.success(f'Received order update: {trader_data}')
        self.data.on_order_update(trader_data)
        # self.orders[trader_data.order_id] = trader_data
        self.on_any_update()

    async def on_balance_update(self,data : BalanceSocketData,channel):
        trader_data = BalanceTraderData.from_socket_data(data)
        self.logger.success(f'Received balance update: {trader_data}')
        self.data.on_balance_update(trader_data)
        # self.balances[AssetSymbol.BTC] = TraderAssetBalance(free=trader_data.btc_free,locked=trader_data.btc_locked)
        # self.balances[AssetSymbol.USD] = TraderAssetBalance(free=trader_data.usd_free,locked=trader_data.usd_locked)
        self.on_any_update()

    # def print_buffer_sizes(self):
    #     for name,buffer in [('prices',self.prices),('orders',self.orders),('balances',self.balances)]:
    #         self.logger.warning(f'CircBuffer {name} has size {buffer.curr_size}')

    # def print_buffer_latests(self):
    #     for name,buffer in [('prices',self.prices),('orders',self.orders),('balances',self.balances)]:
    #         self.logger.warning(f'CircBuffer {name} has latest {buffer.latest}')

class TraderEngineData:
    prices : CircularBuffer[PriceTraderData]
    orders : dict #[int : OrderTraderData]
    balances : dict #[str : TraderAssetBalance]

    num_updates_by_type : dict[str : int]

    def __init__(self,logger : Logger, max_num_prices : int):
        self.logger = logger
        self.prices = CircularBuffer(capacity=max_num_prices)
        self.orders = {}
        self.balances = {}
        self.num_updates_by_type = {t:0 for t in [TraderEngineDataType.price,TraderEngineDataType.order,TraderEngineDataType.balance]}

    @property
    def btc(self):
        return self.balances[AssetSymbol.BTC]

    @property
    def usd(self):
        return self.balances[AssetSymbol.USD]

    def on_price_update(self,data : PriceTraderData):
        self.prices.add(data)
        self.num_updates_by_type[TraderEngineDataType.price]+=1

    def on_order_update(self,data : OrderTraderData):
        self.orders[data.order_id] = data
        self.num_updates_by_type[TraderEngineDataType.order]+=1

    def on_balance_update(self,data : BalanceTraderData):
        self.balances[AssetSymbol.BTC] = TraderAssetBalance(free=data.btc_free,locked=data.btc_locked)
        self.balances[AssetSymbol.USD] = TraderAssetBalance(free=data.usd_free,locked=data.usd_locked)
        self.num_updates_by_type[TraderEngineDataType.balance]+=1

