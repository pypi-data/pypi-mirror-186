
from __future__ import annotations
from dataclasses import dataclass
from typing import ClassVar

from jbg_util import data_converter

DataConverter = data_converter.DataConverter

class SocketEventType:
    order_update = 'executionReport'
    balance_update = 'outboundAccountPosition'
    price_update = '24hrTicker'

class SocketChannel:
    # dflt = 0
    price = 'PRICE'
    balance = 'BALANCE'
    order = 'ORDER'
@dataclass
class BinanceApiKeys:
    api_key : str
    api_secret : str

@dataclass
class SocketData:
    e : str #Event type
    E : int # event time

    data_converter : ClassVar[DataConverter]

    @staticmethod
    def get_data_converter():
        return DataConverter()

    @staticmethod
    def from_raw_socket_data(raw_data):
        return SocketData.data_converter.get_instance_from_dict(raw_data)
@dataclass
class PriceSocketData(SocketData):
    s : str # symbol
    c : float # last price

    @staticmethod
    def from_raw_socket_data(raw_data):
        return PriceSocketData.data_converter.get_instance_from_dict(raw_data,PriceSocketData)
# {
#   "e": "24hrTicker",  // Event type
#   "E": 123456789,     // Event time
#   "s": "BNBBTC",      // Symbol
#   "p": "0.0015",      // Price change
#   "P": "250.00",      // Price change percent
#   "w": "0.0018",      // Weighted average price
#   "x": "0.0009",      // First trade(F)-1 price (first trade before the 24hr rolling window)
#   "c": "0.0025",      // Last price
#   "Q": "10",          // Last quantity
#   "b": "0.0024",      // Best bid price
#   "B": "10",          // Best bid quantity
#   "a": "0.0026",      // Best ask price
#   "A": "100",         // Best ask quantity
#   "o": "0.0010",      // Open price
#   "h": "0.0025",      // High price
#   "l": "0.0010",      // Low price
#   "v": "10000",       // Total traded base asset volume
#   "q": "18",          // Total traded quote asset volume
#   "O": 0,             // Statistics open time
#   "C": 86400000,      // Statistics close time
#   "F": 0,             // First trade ID
#   "L": 18150,         // Last trade Id
#   "n": 18151          // Total number of trades
# }

@dataclass
class AssetBalance:
    a : str # Asset
    f : float #free
    l : float #locked
@dataclass
class BalanceSocketData(SocketData):
    B : list[AssetBalance] #balances

    data_converter : ClassVar[DataConverter]
    @staticmethod
    def get_data_converter():
        dc =DataConverter()

        def convert_balances(raw_balance_data):
            return dc.get_instances_from_arr_of_dicts(raw_balance_data,AssetBalance)
        dc.conversion_fxn_map['list[AssetBalance]']=convert_balances
        return dc

    @staticmethod
    def from_raw_socket_data(raw_data):
        return BalanceSocketData.data_converter.get_instance_from_dict(raw_data,BalanceSocketData)
# {
#   "e": "outboundAccountPosition", //Event type
#   "E": 1564034571105,             //Event Time
#   "u": 1564034571073,             //Time of last account update
#   "B": [                          //Balances Array
#     {
#       "a": "ETH",                 //Asset
#       "f": "10000.000000",        //Free
#       "l": "0.000000"             //Locked
#     }
#   ]
# }

@dataclass
class OrderSocketData(SocketData):
    s : str #Symbol
    i : int #orderID
    S : str #side
    o : str #orderType
    q : float #orderQty
    p : float #price
    z : float #cumulative filled qty
    X : str #orderStatus
    O : int #creationTime

    @staticmethod
    def from_raw_socket_data(raw_data):
        return OrderSocketData.data_converter.get_instance_from_dict(raw_data,OrderSocketData)
# {
#   "e": "executionReport",        // Event type
#   "E": 1499405658658,            // Event time
#   "s": "ETHBTC",                 // Symbol
#   "c": "mUvoqJxFIILMdfAW5iGSOW", // Client order ID
#   "S": "BUY",                    // Side
#   "o": "LIMIT",                  // Order type
#   "f": "GTC",                    // Time in force
#   "q": "1.00000000",             // Order quantity
#   "p": "0.10264410",             // Order price
#   "P": "0.00000000",             // Stop price
#   "d": 4,                        // Trailing Delta; This is only visible if the order was a trailing stop order.
#   "F": "0.00000000",             // Iceberg quantity
#   "g": -1,                       // OrderListId
#   "C": "",                       // Original client order ID; This is the ID of the order being canceled
#   "x": "NEW",                    // Current execution type
#   "X": "NEW",                    // Current order status
#   "r": "NONE",                   // Order reject reason; will be an error code.
#   "i": 4293153,                  // Order ID
#   "l": "0.00000000",             // Last executed quantity
#   "z": "0.00000000",             // Cumulative filled quantity
#   "L": "0.00000000",             // Last executed price
#   "n": "0",                      // Commission amount
#   "N": null,                     // Commission asset
#   "T": 1499405658657,            // Transaction time
#   "t": -1,                       // Trade ID
#   "I": 8641984,                  // Ignore
#   "w": true,                     // Is the order on the book?
#   "m": false,                    // Is this trade the maker side?
#   "M": false,                    // Ignore
#   "O": 1499405658657,            // Order creation time
#   "Z": "0.00000000",             // Cumulative quote asset transacted quantity
#   "Y": "0.00000000",             // Last quote asset transacted quantity (i.e. lastPrice * lastQty)
#   "Q": "0.00000000",             // Quote Order Qty
#   "D": 1668680518494,            // Trailing Time; This is only visible if the trailing stop order has been activated.
#   "j": 1,                        // Strategy ID; This is only visible if the strategyId parameter was provided upon order placement
#   "J": 1000000                   // Strategy Type; This is only visible if the strategyType parameter was provided upon order placement
#   "W": 1499405658657,            // Working Time; This is only visible if the order has been placed on the book.
#   "V": "NONE"                    // SelfTradePreventionMode
# }


for cls in [SocketData,BalanceSocketData,OrderSocketData,PriceSocketData]:
    cls.data_converter = cls.get_data_converter()