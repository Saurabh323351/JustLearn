from nameko.rpc import rpc

class LoginService:

    name='loginService'

    @rpc
    def login_service(self,request_data):

        username=request_data['username']
        password=request_data['password']

        print(username,password,'------->login_service')

        return 'from login_service'
