from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Subscriptions(Resource):
  def post(self):
    return {"Subscriptions":True}

api.add_resource(Subscriptions, '/landing/subscriptions')

if __name__ == '__main__':
  app.run(debug=True)
