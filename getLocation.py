import boto3


def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table('trash_can')

    response = table.get_item(
        Key={
            'id': 477  # 파티션 키 변경해야될듯. ex) contents
        }
    )
    item = response['Item']

    return item