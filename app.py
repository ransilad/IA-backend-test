# -*- coding: utf-8 -*-

from flask import Flask
from flask import request
from flask_restful import Resource
from flask_restful import Api
from flask_cors import CORS
from boto3.dynamodb.conditions import Key
from boto3 import resource


app = Flask(__name__)
CORS(app)
api = Api(app)


dynamoDB = resource(
    'dynamodb',
    aws_access_key_id='AKIAIMIX7A3JY5EQ4GHA',
    aws_secret_access_key='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',
    region_name='us-east-2',
    endpoint_url='http://dynamodb.us-east-2.amazonaws.com'
)


class Subscriptions(Resource):

    def post(self):

        successResponse = True
        messageResponse = ''
        subscriptionsTable = dynamoDB.Table('Subscriptions')
        JSONDataPOST = request.get_json()

        response = subscriptionsTable.query(
            KeyConditionExpression = Key('email').eq(JSONDataPOST['email'])
        )

        if response['Items']:
            successResponse = False
            messageResponse = 'Ya se ha registrado una subscripción con ese correo. Gracias!'
            return {'success': successResponse, 'message': messageResponse}

        try:
            subscriptionsTable.put_item(
                Item = {
                    'email': JSONDataPOST['email'],
                    'name': JSONDataPOST['name'],
                    'phone': JSONDataPOST['phone'],
                    'dni': JSONDataPOST['dni']
                }
            )
            messageResponse = 'Se registró exitosamente'
        except:
            messageResponse = 'Error registrando la subscripción'
            successResponse = False

        return {'success': successResponse, 'message': messageResponse}


api.add_resource(Subscriptions, '/landing/subscriptions')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
