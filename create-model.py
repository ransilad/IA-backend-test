# -*- coding: utf-8 -*-

from boto3 import resource


dynamodb = resource(
    'dynamodb',
    aws_access_key_id="AKIAIMIX7A3JY5EQ4GHA",
    aws_secret_access_key="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",
    region_name='us-east-2',
    endpoint_url="http://dynamodb.us-east-2.amazonaws.com"
)


table = dynamodb.create_table(
    TableName = 'Subscriptions',
    KeySchema = [
        {
            'AttributeName': 'email',
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'phone',
            'KeyType': 'RANGE'
        }
    ],
    AttributeDefinitions = [
        {
            'AttributeName': 'email',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'name',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'phone',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'dni',
            'AttributeType': 'S'
        },
    ],
    LocalSecondaryIndexes = [
        {
            'IndexName': 'SubsByName',
            'KeySchema': [
                {
                    'AttributeName': 'email',
                    'KeyType': 'HASH'
                },
                {
                    'AttributeName': 'name',
                    'KeyType': 'RANGE'
                },
            ],
            'Projection': {
                'ProjectionType': 'ALL'
            }
        },
        {
            'IndexName': 'SubsByPhone',
            'KeySchema': [
                {
                    'AttributeName': 'email',
                    'KeyType': 'HASH'
                },
                {
                    'AttributeName': 'phone',
                    'KeyType': 'RANGE'
                },
            ],
            'Projection': {
                'ProjectionType': 'ALL'
            }
        },
        {
            'IndexName': 'SubsByDni',
            'KeySchema': [
                {
                    'AttributeName': 'email',
                    'KeyType': 'HASH'
                },
                {
                    'AttributeName': 'dni',
                    'KeyType': 'RANGE'
                },
            ],
            'Projection': {
                'ProjectionType': 'ALL'
            }
        }
    ],
    ProvisionedThroughput = {
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10,
    }
)
