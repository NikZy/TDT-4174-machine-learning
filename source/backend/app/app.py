from flask import Flask, jsonify, request
from flask_restful import Resource, Api, fields, marshal_with, reqparse
from joblib import dump, load
import pandas as pd
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
cors = CORS(app, resources={r"*": {"origins": "https://house-pricing.nikzy.no"}})

scaler = load('../../models/datascaler.joblib')

# dt_best_model = load('../../models/decision-tree-optimized.joblib')
dt_best_model = load('../../models/linear-regression-sklearn.joblib')
X_test = pd.read_csv('../../data/x_test').iloc[:, 1:]
# print(X_test.iloc[4, :])

# print(dt_best_model.predict([X_test.iloc[4, :]]))

fields = {
    'test': fields.String
}


parser = reqparse.RequestParser()
parser.add_argument('bedrooms', type=float)
parser.add_argument('bathrooms', type=float)
parser.add_argument('sqft_living', type=float)
parser.add_argument('sqft_lot', type=float)
parser.add_argument('floors', type=float)
parser.add_argument('waterfront', type=float)
parser.add_argument('view', type=float)
parser.add_argument('condition', type=float)
parser.add_argument('grade', type=float)
parser.add_argument('sqft_above', type=float)
parser.add_argument('sqft_basement', type=float)
parser.add_argument('last_fixed', type=float)
parser.add_argument('zip_code', type=float)
parser.add_argument('sqft_living15', type=float)
parser.add_argument('sqft_lot15', type=float)
parser.add_argument('center_distance', type=float)
parser.add_argument('test', type=int)


class HousePriceEstimatorEndpint(Resource):
    def post(self):
        request.get_json(force=True)
        args = parser.parse_args()

        parameters = [args['bedrooms'],
                      args['bathrooms'],
                      args['sqft_living'],
                      args['sqft_lot'],
                      args['floors'],
                      args['waterfront'],
                      args['view'],
                      args['condition'],
                      args['grade'],
                      args['sqft_above'],
                      args['sqft_basement'],
                      args['last_fixed'],
                      args['zip_code'],
                      args['sqft_living15'],
                      args['sqft_lot15'],
                      args['center_distance']]
        print(parameters)
        prediction = dt_best_model.predict([parameters])
        print(prediction)
        return jsonify(prediction=prediction[0])

    def get(self):
        return {'test': 'world'}

@app.route("/")
def hello():
    return "Hello World from Flask"

api.add_resource(HousePriceEstimatorEndpint, '/estimator')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False, port=80)
