import json

from nameko.web.handlers import http
from nameko.rpc import rpc

# class API:
#
#     name = 'micro-api'
#
#
#     @http('GET', '/hello1')
#     def get_method(self ,request):
#
#         return json.dumps({'hello': 'world'})


# class HttpService:
#
#     name="multiply_service"
#
#     @http('GET','/get_product/<int:first>/<int:second>')
#     def get_product(self,request,first,second):
#
#         third=int(request.args.get('third',1))
#         print(third)
#         product= first*second*third
#         print(product,'--->')
#         response=json.dumps({"Your Product is => ":product})
#
#         return response


class GreeterService(object):

    name= 'greeter_service'

    # @http('GET', '/greet_me/<string:name>')

    @rpc
    def greet(self,name):

        print(name,'----->')
        return f"Hello {name}"