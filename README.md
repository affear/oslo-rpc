#Sample code for RPC client/server communication with oslo.messaging

To install (with virtualenv):

```
$ git clone git@github.com:affear/oslo_rpc.git
$ cd oslo_rpc
$ sudo apt-get install python-virtualenv
$ virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

To run:

* Start RabbitMQ (or else) service
* On a shell: `$ python server.py`
* On _another_ shell: `$ python client.py`
* Enjoy