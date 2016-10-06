import requests

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    r = requests.get("http://rongen:5000/")
    return "<b>" + r.content + "</b>"

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5001)
