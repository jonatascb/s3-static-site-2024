import boto3

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table = dynamodb.Table('Recipes')
    recipe_id = event['recipe_id']

    try:
        response = table.update_item(
            Key={ 'RecipeID': recipe_id },
            UpdateExpression="set VisitsCounter = VisitsCounter + :inc",
            ExpressionAttributeValues={ ':inc': 1 },
            ReturnValues="UPDATED_NEW"
        )
        return {
            'value': response['Attributes']
        }
    except Exception as e:
        return {
            'error': { 'message': str(e) }
        }
