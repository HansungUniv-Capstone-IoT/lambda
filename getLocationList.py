import boto3
from random import *


# 다이나모 db 전체 데이터 get
def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table('trash_can')
    id = randint(1, 1000)
    response = table.scan()

    return response