import os
import json
import pickle
from io import StringIO
import sys

import flask

import numpy as np
import pandas as pd


prefix = '../notebook/'
model_path = os.path.join(prefix, 'model')
model_file = 'model.pkl'

class ScoringService(object):
    model = None

    @classmethod
    def get_model(cls):
        if cls.model == None:
            with open(os.path.join(model_path, model_file), 'rb') as inp:
                cls.model = pickle.load(inp)
        return cls.model

    @classmethod
    def predict(cls, input):
        clf = cls.get_model()
        return clf.predict(input)

app = flask.Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    data = None

    if flask.request.content_type == 'text/csv':
        data = flask.request.data.decode('utf-8')
        s = StringIO(data)
        data = pd.read_csv(s, header=None)
    elif flask.request.content_type == 'text/json':
        data = flask.request.data.decode('utf-8')
        s = StringIO(data)
        data = pd.read_json(s)
    else:
        return flask.Response(response='Invalid Data Format this api supports CSV or JSON data', status=415, mimetype='text/plain')

    predictions = ScoringService.predict(data)

    out = StringIO()
    pd.DataFrame({'results':predictions}).to_json(out)
    result = out.getvalue()

    return flask.Response(response=result, status=200, mimetype='text/json')

if __name__ == "__main__":
    print(" Starting Flask API server")
    app.run(host='0.0.0.0')