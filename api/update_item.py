import boto3
import os

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Visits')
    visit_id = os.environ.get('VISIT_ID', 'default_visit_id')

    try:
        response = table.update_item(
            Key={ 'VisitID': visit_id },
            UpdateExpression="set VisitsCounter = VisitsCounter + :inc",
            ExpressionAttributeValues={ ':inc': 1 },
            ReturnValues="UPDATED_NEW"
        )
        return {
            'statusCode': 200,
            'headers': { 'Content-Type': 'application/json' },
            'body': response['Attributes']
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'headers': { 'Content-Type': 'application/json' },
            'body': { 'error': str(e) }
        }
