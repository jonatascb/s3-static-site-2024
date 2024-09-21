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
                'value': response['Item'],
            }
        else:
            return {
                'error': { 'message': 'Item not found' },
            }
    except Exception as e:
        return {
            'error': { 'message': str(e) }
        }
