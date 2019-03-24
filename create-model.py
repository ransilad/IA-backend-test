# -*- coding: utf-8 -*-

from boto3 import resource
from config import *


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
