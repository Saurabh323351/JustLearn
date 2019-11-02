"""
Example of event publisher using rpc extension
"""

from nameko.events import EventDispatcher
from nameko.rpc import rpc

class MyEventPublisherService(object):

    name="my_event_publisher_service"

    dispatch=EventDispatcher()

    @rpc
    def publish(self,payload):

        self.dispatch('my-event',payload)