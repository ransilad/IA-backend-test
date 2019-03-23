# -*- coding: utf-8 -*-

from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS
import boto3

app = Flask(__name__)
CORS(app)
api = Api(app)

dynamodb = boto3.resource(
    'dynamodb',
    aws_access_key_id="AKIAIMIX7A3JY5EQ4GHA",
    aws_secret_access_key="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",
    region_name='us-east-2',
    endpoint_url="http://dynamodb.us-east-2.amazonaws.com"
)

class Subscriptions(Resource):

    def post(self):

        table = dynamodb.Table('Subscriptions')
        reqData = request.get_json()
        print(reqData)
        successResponse = True
        messageResponse = ""

        try:
            table.put_item(
                Item={
                    'email': reqData['email'],
                    'name': reqData['name'],
                    'phone': reqData['phone'],
                    'dni': reqData['dni']
                }
            )
            messageResponse = "Se registró exitosamente"
        except Exception as e:
            print(str(e))
            messageResponse = "Error registrando la subscripción"
            successResponse = False

        return { "success": successResponse, "message": messageResponse}

api.add_resource(Subscriptions, '/landing/subscriptions')

if __name__ == '__main__':
  app.run(host="0.0.0.0", port=80)
