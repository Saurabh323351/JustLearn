from nameko.rpc import rpc,RpcProxy

class ExpandedGreeterService(object):

    name='expanded_greeter_s'

    greeter_service=RpcProxy('greeter_service')

    @rpc
    def greetbyanothermethod(self,name):

        return '{} Welcome to Pygotham'.format(self.greeter_service.greet(name))

