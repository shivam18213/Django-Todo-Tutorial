from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse
import pickle
import numpy as np
import json

app = Flask(__name__)
api = Api(app)

# create parser for payload
#we usually send the data in a JSON serialized format and name the key as data
parser = reqparse.RequestParser()
parser.add_argument('data')


# Resource is imported from flask_restful
# IrisClassifier in herits resource
class IrisClassifier(Resource):
    def post(self):
        args = parser.parse_args()
        print(args)
        # since data was the key to the json passed
        X = np.array(json.loads(args['data']))
        prediction = model.predict(X)
        return jsonify(prediction.tolist())

api.add_resource(IrisClassifier,'/iris')

if __name__ == '__main__':
    with open('model.pickle','rb') as f:
        model = pickle.load(f)
    
    app.run(debug = True)

