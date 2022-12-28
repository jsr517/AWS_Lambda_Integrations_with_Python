import boto3

def lambda_handler(event, context):
    # TODO implement
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('users')
    PID=event['UserID']
    try:
        # TODO: write code...
        response = table.get_item(
            Key={"UserID":PID},
            ConsistentRead=True) 
        return response
    except:
        raise

