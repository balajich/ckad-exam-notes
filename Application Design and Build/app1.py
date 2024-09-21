import requests
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    # call the app1 running on port 5001
    return "I am app1, Calling app11 -> " + requests.get('http://localhost:5001/').text


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
