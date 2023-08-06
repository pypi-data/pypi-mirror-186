from __future__ import annotations
import asyncio
from binance import AsyncClient, BinanceSocketManager
from jbg_util import binance_models
from jbg_util import pub_sub_mediator
from jbg_util import logging_util
from jbg_util import data_converter
from json import dumps

Logger = logging_util.Logger
DataConverter = data_converter.DataConverter
PubSubMediator = pub_sub_mediator.PubSubMediator
SocketData,BalanceSocketData,PriceSocketData,OrderSocketData,SocketChannel,SocketEventType,BinanceApiKeys = \
    binance_models.SocketData,binance_models.BalanceSocketData,binance_models.PriceSocketData,binance_models.OrderSocketData,binance_models.SocketChannel,binance_models.SocketEventType,binance_models.BinanceApiKeys

# TODO: don't make socket connect in tests with mockData!
class SocketManager:
    def __init__(self,logger : Logger = None):
        self.logger = logger or Logger(file_path='./logs/socket_manager.log',should_print_to_screen=True).empty_log()
        self.socket_streams : list[BinanceSocketStream]=[]

    async def start_sockets(self,api_keys : BinanceApiKeys, pub_sub_mediator : PubSubMediator,socket_classes):
        tasks = []
        for cls in socket_classes:
            socket_stream = cls(pub_sub_mediator,self.logger)
            task = asyncio.create_task(self.start_socket(api_keys,socket_stream))

            self.socket_streams.append(socket_stream)
            tasks.append(task)
        rslts = await asyncio.gather(*tasks)

    async def start_socket(self,api_keys : BinanceApiKeys,socket_stream : BinanceSocketStream):
        await socket_stream.init(api_keys)
        await socket_stream.open_socket()

    def stop_sockets(self):
        for socket_stream in self.socket_streams:
            socket_stream.close_socket()

class BinanceSocketStream:
    data_converter = DataConverter()

    def __init__(self, pub_sub_mediator : PubSubMediator, logger : Logger, name : str=None):
        self.pub_sub_mediator=pub_sub_mediator
        self.name=name
        self.close_socket_event = asyncio.Event()
        self.logger = logger

    async def open_socket(self):
        raise NotImplementedError("A generic socket stream cannot be opened.")

    async def init(self, api_keys : BinanceApiKeys):
        self.client = await AsyncClient.create(api_key=api_keys.api_key, api_secret=api_keys.api_secret,tld='us')
        self.binance_socket_manager = BinanceSocketManager(self.client)

    async def recv(self,socket_stream):
        return await socket_stream.recv()

    async def listen(self):
        self.logger.info(f'Opened the {self.name} socket connection...')
        try:
            async with self.ts as socket_stream:
                while True:
                    completed,pending = await asyncio.wait([self.recv(socket_stream),self.wait_until_close_socket_event()],return_when=asyncio.FIRST_COMPLETED)
                    if self.close_socket_event.is_set():
                        self.logger.info(f'Close socket event has occurred on socket_stream={self.name}')
                        return
                    for task in completed:
                        # print('\n\nTASK\n',task)
                        # print('\n\nRESULT\n',task.result())
                        await self.publish(task.result())
        except Exception as e:
            raise e
        finally:
            self.logger.info(f'Closing the {self.name} connection...')
            await self.client.close_connection()

    async def wait_until_close_socket_event(self):
        await self.close_socket_event.wait()

    def close_socket(self):
        self.close_socket_event.set()

    async def publish(self,data):
        self.logger.info(dumps(data))
        data,channel=self.parse_data(data)
        if self.pub_sub_mediator is None:
            return
        await self.pub_sub_mediator.publish(data,channel)

    @staticmethod
    def parse_data(data) -> SocketData:
        return data,None

class BinanceUserSocketStream(BinanceSocketStream):
    def __init__(self, pub_sub_mediator : PubSubMediator, logger : Logger):
        super().__init__(pub_sub_mediator, logger, name='user')

    async def open_socket(self):
        self.ts = self.binance_socket_manager.user_socket()
        await self.listen()

    @staticmethod
    def parse_data(data) -> SocketData:
        event_type=data['e']
        if event_type ==SocketEventType.order_update:
            data = OrderSocketData.from_raw_socket_data(data)
            return data,SocketChannel.order
        if event_type ==SocketEventType.balance_update:
            data = BalanceSocketData.from_raw_socket_data(data)
            return data,SocketChannel.balance
        raise ValueError(f'unrecognized event type = {event_type}',data)

class BinanceTickerSocketStream(BinanceSocketStream):
    def __init__(self, pub_sub_mediator : PubSubMediator, logger : Logger):
        super().__init__(pub_sub_mediator, logger, name='ticker')

    async def open_socket(self):
        self.ts = self.binance_socket_manager.symbol_ticker_socket('BTCUSD')
        await self.listen()

    @staticmethod
    def parse_data(data) -> SocketData:
        data = PriceSocketData.from_raw_socket_data(data)
        return data,SocketChannel.price