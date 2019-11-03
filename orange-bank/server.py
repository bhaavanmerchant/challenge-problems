import flask
from flask import jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = False

@app.route('/trends/<country>')
def trends(country):
  return 'Server Works!'

app.run()
