from flask import Flask
import random
app = Flask(__name__)

@app.route('/')
def hello_world():
    lines = open('quotes').read().splitlines()
    quote = random.choice(lines)
    return quote

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5001)
