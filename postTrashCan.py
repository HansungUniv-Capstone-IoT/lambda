import boto3
from random import *
from decimal import Decimal


def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table('trash_can')
    id = randint(1, 1000)
    latitude = event['latitude']
    longitude = event['longitude']
    dlatitude = Decimal(latitude)
    dlongitude = Decimal(longitude)

    response = table.put_item(
        Item={
            'id': id,
            'address': event['address'],
            'name': event['name'],
            'latitude': dlatitude,
            'longitude': dlongitude,
            'createdBy': event['createdBy']
        }
    )

    return response

    """
    {
        "address": "서울특별시 성북구 삼선동 삼선교로16길 116",
        "name" : "한성대학교 공학관A동 1층",
        "createdBy" : "jonghyun",
        "latitude" : "37.58181151262402",
        "longitude" : "27.00990332950407"
    }
"""