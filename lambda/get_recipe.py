import boto3

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table = dynamodb.Table('Recipes')
    recipe_id = event['recipe_id']

    try:
        response = table.get_item(
            Key = {
                'RecipeID': recipe_id
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
