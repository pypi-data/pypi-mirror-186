from dataclasses import fields
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String,DateTime,Float
from jbg_util import data_converter
from jbg_util import trader_models
from jbg_util import binance_models
from jbg_util import logging_util
from jbg_util import pub_sub_mediator

SocketChannel = binance_models.SocketChannel
Logger = logging_util.Logger
PubSubMediator = pub_sub_mediator.PubSubMediator
convert_socket_to_trader_data = trader_models.convert_socket_to_trader_data

class Database:
    TYPE_MAP = {
        'int' : Integer,
        'str' : String,
        'datetime' : DateTime,
        'float' : Float
    }

    def __init__(self,mediator : PubSubMediator = None,engine=None,logger : Logger = None):
        self.subscribe_for_updates(mediator)
        self.logger = logger or Logger(file_path='./logs/database.log',should_print_to_screen=True)
        self.engine = engine or Database.create_engine()
        self.tables : dict[str:Table]= {}
        self.data_converter=data_converter.DataConverter()

    def subscribe_for_updates(self,mediator : PubSubMediator):
        if mediator is None:
            return
        mediator.subscribe_local_fxn(self.on_update,SocketChannel.price)
        mediator.subscribe_local_fxn(self.on_update,SocketChannel.order)
        mediator.subscribe_local_fxn(self.on_update,SocketChannel.balance)

    async def on_update(self,data,channel):
        self.logger.secondary(f'\nDatabase received published data from socket channel {channel}!')
        parsed_data = convert_socket_to_trader_data(data)
        self.logger.info(f'\tParsed_data: {parsed_data}')
        self.save_model(parsed_data)

    def connect(self):
        self.conn = self.engine.connect()
        return self

    def create_table_from_cls(self,cls):
        meta = MetaData()
        table_name = cls.__name__
        try:
            cols = [Column(field.name, Database.TYPE_MAP[field.type.__name__]) for field in fields(cls) if field.name!='id']
        except AttributeError: #TODO: not sure what's happening here, and no time to figure it out right now
            cols = [Column(field.name, Database.TYPE_MAP[field.type]) for field in fields(cls) if field.name!='id']

        table = Table(
            table_name, meta,
            Column('id', Integer, primary_key = True),
            *cols,
        )
        meta.create_all(self.engine)
        self.tables[table_name]=table

    def get_table_for_cls(self,cls) -> Table:
        table_name = cls.__name__
        if table_name not in self.tables:
            self.create_table_from_cls(cls)
        return self.tables[table_name]

    #TODO make this async
    def save_model(self,model):
        table = self.get_table_for_cls(type(model))
        d = self.data_converter.get_dict_from_instance(model)
        ins = table.insert().values(**d)
        rslt = self.conn.execute(ins)

    def row_to_model(self,row : dict,cls):
        if not hasattr(cls,'id'):
            row = {key:val for key,val in row.items() if key!='id'}
        return cls(**row)

    @staticmethod
    def create_engine(db_name='db'):
        engine = create_engine(f'sqlite:///{db_name}.db', echo = True)
        meta = MetaData()
        meta.create_all(engine)
        return engine

    def clear_table_for_cls(self,cls,db_name='db'):
        table=self.get_table_for_cls(cls)
        stmt = table.delete() #.where(t.c.id > id)
        self.conn.execute(stmt)

    def get_all_saved_models(self,cls):
        table = self.get_table_for_cls(cls)
        s = table.select() #.where(table.c.id>2)
        rslt = self.conn.execute(s)
        return [self.row_to_model(row,cls) for row in rslt]