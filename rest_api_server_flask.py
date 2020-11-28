#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" ref: https://www.codementor.io/@sagaragarwal94/building-a-basic-restful-api-in-python-58k02xsiq """

import pandas as pd
from flask import Flask, jsonify
from flask_cors import CORS
from flask_restful import Resource, Api


DB_PATH = 'data/'

app = Flask(__name__)
cors = CORS(app)
api = Api(app)


class GetSensorDataSince(Resource):
    def get(self, user_id, sensor_id, last_index):
        db_name = DB_PATH + str(user_id) + '_sensor_' + str(sensor_id) + '_db.csv'
        df = pd.read_csv(db_name, index_col=0)
        data = df.iloc[int(last_index):].to_dict('records')

        return jsonify(data)


class GetSpendingForecastDataSince(Resource):
    def get(self, user_id, last_index):
        db_name = DB_PATH + str(user_id) + '_spending_forecast_db.csv'
        df = pd.read_csv(db_name, index_col=0)
        data = df.iloc[int(last_index):].to_dict('records')

        return jsonify(data)


api.add_resource(GetSensorDataSince, '/<user_id>/sensor/<sensor_id>/data/from/<last_index>')
api.add_resource(GetSpendingForecastDataSince, '/<user_id>/spending_forecast/data/from/<last_index>')


if __name__ == '__main__':
    PORT = 5002
    app.run(port=str(PORT))
