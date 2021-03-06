from flask import Flask, request
from flask.json import jsonify
from models.model_predict import Model

import os

MESSAGES_MODEL = Model(os.path.abspath(
    "routes/api/machine-learning/models/emotext.tf"))
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/predict', methods=['POST'])
def predict():
    
    texts = request.get_json()

    textStrings = texts['texts']
    textsRay = ("" + textStrings).split("||")
    prediction = MESSAGES_MODEL.predict(textsRay)
    return jsonify({"success": True, "message": ("negative" if prediction > 0.5 else "positive")})


@app.route('/predict_list', methods=['POST'])
def predict_list():
    
    prediction = MESSAGES_MODEL.predict(request.get_json()['texts'])
    return jsonify({"success": True, "message": ("negative" if prediction > 0.5 else "positive")})

if __name__ == '__main__':
    app.debug = True
    app.run(host="localhost", port=8000, debug=True)
