import time
import zmq

HOST = '127.0.0.1'
PORT = '4444'

_context = zmq.Context()
_publisher = _context.socket(zmq.PUB)
url = 'tcp://{}:{}'.format(HOST, PORT)

def publish_message(message):

    try:
        _publisher.bind(url)
        time.sleep(1)
        print "sending message : {0}".format(message, _publisher)
        _publisher.send(message)

    except Exception as e:
        print "error {0}".format(e)

    finally:
        print "unbinding"
        _publisher.unbind(url)

from flask import Flask
import random
app = Flask(__name__)

@app.route('/')
def hello_world():
    lines = open('quotes').read().splitlines()
    quote = random.choice(lines)
    publish_message(quote)
    return quote

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5001)
