"""
Example of event handler extension
"""

from nameko.events import event_handler

class MyEventHandlerServiceOne(object):

    name='my_event_handler_service_1'

    @event_handler('my_event_publisher_service','my-event')
    def receiving_publish_event(self,payload):

        print(f'Received an event in 1 : {payload}')



class MyEventHandlerServiceTwo(object):

    name='my_event_handler_service_2'

    @event_handler('my_event_publisher_service','my-event')
    def receiving_publish_event(self,payload):

        print(f'Received an event in 2: {payload}')
