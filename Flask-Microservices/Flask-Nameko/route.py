

from flask import Flask,request

app = Flask(__name__)
# from __init__ import app, rpc
from nameko.standalone.rpc import ClusterRpcProxy
config = {
    "AMQP_URI":"pyamqp://guest:guest@localhost"
}

# @app.route('/',methods=['GET','POST'])
# def index():
#     result = rpc.service.do_something('test')
#     return result



@app.route('/login',methods=['GET','POST'])
def login():

    request_data=request.get_json()
    print(request_data)

    with ClusterRpcProxy(config) as cluster_rpc:

        result=cluster_rpc.loginService.login_service(request_data)
        print(result,'--------result')

    return "Hi saurabh login here"


if __name__ == '__main__':

    app.run(debug=True)