# -*- coding: utf-8 -*-

from boto3 import resource

dynamoDB = resource(
    'dynamodb',
    aws_access_key_id='AKIAIMIX7A3JY5EQ4GHA',
    aws_secret_access_key='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',
    region_name='us-east-2',
    endpoint_url='http://dynamodb.us-east-2.amazonaws.com'
)
