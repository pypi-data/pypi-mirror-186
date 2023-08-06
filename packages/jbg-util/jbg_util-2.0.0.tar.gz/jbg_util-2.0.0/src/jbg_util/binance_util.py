

from datetime import datetime
from jbg_util.file_util import FileManager
from jbg_util.data_converter import DataConverter
from jbg_util.models.binance_models import BinanceApiKeys
import os
def binance_timestamp_to_dte(ts : int):
    return datetime.utcfromtimestamp(ts/1000)

def dte_to_binance_timestamp(dte : datetime):
    return dte.timestamp()*1000

def get_binance_api_keys() -> BinanceApiKeys:
    fu = FileManager()

    env = os.getenv('JBG_ENV')
    file_path='/Users/jgardner/Documents/personal/.binance_api_keys'
    if env=='EC2':
        file_path='~/.bnb_api_keys'
    d = fu.get_obj_from_file(file_path)
    dc = DataConverter()
    keys = dc.get_instance_from_dict(d,BinanceApiKeys)
    return keys