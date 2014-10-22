from oslo import messaging
import config as cfg

transport = messaging.get_transport(cfg.CONF)
target = messaging.Target(topic='hello')
client = messaging.RPCClient(transport, target)

def call(method):
	return client.call({}, method)

while True:
	method = raw_input('Insert method: ')
	try:
		result = call(method)
	except:
		result = "Error in method call"
	print result
