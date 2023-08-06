

from datetime import datetime
from jbg_util import file_util
from jbg_util import data_converter
from jbg_util import binance_models
import os

BinanceApiKeys = binance_models.BinanceApiKeys
DataConverter = data_converter.DataConverter
FileManager = file_util.FileManager
def binance_timestamp_to_dte(ts : int):
    return datetime.utcfromtimestamp(ts/1000)

def dte_to_binance_timestamp(dte : datetime):
    return dte.timestamp()*1000

def get_binance_api_keys() -> BinanceApiKeys:
    fu = FileManager()

    env = os.getenv('JBG_ENV')
    file_path='/Users/jgardner/Documents/personal/.binance_api_keys'
    if env=='EC2':
        file_path='/home/ec2-user/.bnb_api_keys'
    d = fu.get_obj_from_file(file_path)
    dc = DataConverter()
    keys = dc.get_instance_from_dict(d,BinanceApiKeys)
    return keys