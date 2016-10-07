from flask import Flask
app = Flask(__name__)

@app.route('/')
def root():
    response = app.send_static_file('quote.log')
    response.headers["content-type"] = "text/plain"
    return response

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5002)
