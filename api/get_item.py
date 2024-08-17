import boto3
import os

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Visits')
    visit_id = os.environ.get('VISIT_ID', 'default_visit_id')

    try:
        response = table.get_item(
            Key = {
                'VisitID': visit_id
            }
        )
        if 'Item' in response:
            return {
                'statusCode': 200,
                'body': response['Item'],
                'headers': { 'Content-Type': 'application/json' }
            }
        else:
            return {
                'statusCode': 404,
                'body': { 'error': 'Item not found' },
                'headers': { 'Content-Type': 'application/json' }
            }
    except Exception as e:
        return {
            'statusCode': 500,
            'headers': { 'Content-Type': 'application/json' },
            'body': { 'error': str(e) }
        }
