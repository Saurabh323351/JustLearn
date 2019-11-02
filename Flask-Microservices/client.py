from nameko.standalone.rpc import ClusterRpcProxy

config = {
    "AMQP_URI":"pyamqp://guest:guest@localhost"
}

with ClusterRpcProxy(config) as cluster_rpc:

    print(cluster_rpc.greeter_service.greet("Saurabh try to call greet() method  of GreeterService from client service using ClusterRpcProxy"))