# -*- coding: utf-8 -*-

from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from views import Subscriptions


app = Flask(__name__)
CORS(app)
api = Api(app)


api.add_resource(Subscriptions, '/landing/subscriptions')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
