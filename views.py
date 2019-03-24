# -*- coding: utf-8 -*-

from flask import request
from flask_restful import Resource
from boto3.dynamodb.conditions import Key

from config import *

class Subscriptions(Resource):

    def get(self):

        return {'ping': 'pong'}


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