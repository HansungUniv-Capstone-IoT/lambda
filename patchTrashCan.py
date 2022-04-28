import boto3

"""
patch 요청시 body

{
    "operation": "update",
    "payload": {
        "Key": {
            "id": 477
        },
        "AttributeUpdates": {
            "address": {
                "Value": "서울특별시"
            }
        }
    }
}
"""


def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table('trash_can')
    # key = event[id] # key 현재는 id -> contents 등으로 파티션키 변경해야됨.

    operation = event['operation']

    operations = {
        # 'create': lambda x: table.put_item(**x),
        # 'read': lambda x: table.get_item(**x),
        'update': lambda x: table.update_item(**x)
        # 'delete': lambda x: table.delete_item(**x),
        # 'list': lambda x: table.scan(**x),
        # 'echo': lambda x: x,
        # 'ping': lambda x: 'pong'
    }

    print(operations)

    if operation in operations:
        return operations[operation](event.get('payload'))
    else:
        raise ValueError('Unrecognized operation "{}"'.format(operation))

    """
    response = table.get_item(
        Key={
            'id': key # 파티션 키 변경해야될듯. ex) contents
         }
    )
    item = response['Item']

    return item
    """