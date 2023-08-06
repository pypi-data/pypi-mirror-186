from types import FunctionType
import asyncio
class DestinationType:
    local_fxn = 1

class Subscriber:
    def __init__(self,destination,destination_type : DestinationType):
        self.destination = destination
        self.destination_type = destination_type

class PubSubMediator:
    def __init__(self):
        self.subscribers_by_channel = {}

    async def publish(self, data, channel : str):
        if channel not in self.subscribers_by_channel:
            return
        local_fxns_to_call=[]
        for subscriber in self.subscribers_by_channel[channel]:
            if subscriber.destination_type == DestinationType.local_fxn:
                local_fxns_to_call.append(subscriber.destination)
        await asyncio.gather(*[fxn(data,channel) for fxn in local_fxns_to_call])

    def subscribe_local_fxn(self, destination : FunctionType, channel : str):
        subscriber = Subscriber(destination,DestinationType.local_fxn)
        if channel not in self.subscribers_by_channel:
            self.subscribers_by_channel[channel]=[]
        self.subscribers_by_channel[channel].append(subscriber)

