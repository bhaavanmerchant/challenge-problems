from flask import Flask
from flask import request
from flask_httpauth import HTTPBasicAuth

import transformer

auth = HTTPBasicAuth()

users = {
    "bhaavan": "PlaintextPasswordsAreBad",
    "revolut": "NotBadEnoughForSomeRandomChallenge",
    "admin": "42"
}

@auth.verify_password
def verify_password(username, password):
    if username in users:
        return users.get(username) == password
    return False

app = Flask(__name__)

@app.route('/')
def index():
  return 'Server Works!'

@app.route('/nest/<keys>', methods=['POST'])
@auth.login_required
def nest_json(keys):
  data = request.json
  nested_keys = keys.split(',')
  return transformer.Transformer().nested_transformer(data, nested_keys)