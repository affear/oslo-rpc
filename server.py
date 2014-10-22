from oslo import messaging
import config as cfg

class Endpoints(object):
	def hello(self, ctx):
		return 'Hello'

	def hi(self, ctx):
		return 'Hi'


transport = messaging.get_transport(cfg.CONF)
target = messaging.Target(topic='hello', server='hello-server')
endpoints = [Endpoints(), ]
server = messaging.get_rpc_server(transport, target, endpoints,
                                  executor='blocking')
server.start()
server.wait()