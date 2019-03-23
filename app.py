from flask import Flask, request
from flask_restful import Resource, Api
import boto3

app = Flask(__name__)
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
    successResponse = True

    try:
        table.put_item(
            Item={
                'email': reqData['email'],
                'name': reqData['name'],
                'phone': reqData['phone'],
                'dni': reqData['dni']
            }
        )
    except:
        successResponse = False

    return { "success": successResponse }

api.add_resource(Subscriptions, '/landing/subscriptions')

if __name__ == '__main__':
  app.run(debug=True)
