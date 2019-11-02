from flask import Flask,request
from flask_nameko import FlaskPooledClusterRpcProxy

rpc = FlaskPooledClusterRpcProxy()

def create_app():
    app = Flask(__name__)
    app.config.update(dict(
        NAMEKO_AMQP_URI='pyamqp://guest:guest@localhost'
    ))

    rpc.init_app(app)
    return app
app = create_app()