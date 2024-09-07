import unittest
from ..get_recipe import lambda_handler
from moto import mock_aws
import boto3

class TestGetItem(unittest.TestCase):

    @mock_aws
    def test_lambda_handler_item_found(self):
        # Arrange
        self.dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
        self.table = self.dynamodb.create_table(
            TableName='Recipes',
            KeySchema=[
                { 'AttributeName': 'RecipeID', 'KeyType': 'HASH' }
            ],
            AttributeDefinitions=[
                { 'AttributeName': 'RecipeID', 'AttributeType': 'S' }
            ],
            ProvisionedThroughput={ 'ReadCapacityUnits': 10, 'WriteCapacityUnits': 10 }
        )
        self.table.put_item(Item={ 'RecipeID': 'sample_recipe_id' })

        # Act
        event = { 'recipe_id' : 'sample_recipe_id' }
        context = {}
        response = lambda_handler(event, context)

        # Assert
        self.assertEqual(response['statusCode'], 200)
        self.assertIn('body', response)
        self.assertEqual(response['body']['RecipeID'], 'sample_recipe_id')

    @mock_aws
    def test_lambda_handler_item_not_found(self):
        # Arrange
        self.dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
        self.table = self.dynamodb.create_table(
            TableName='Recipes',
            KeySchema=[
                { 'AttributeName': 'RecipeID', 'KeyType': 'HASH' }
            ],
            AttributeDefinitions=[
                { 'AttributeName': 'RecipeID', 'AttributeType': 'S' }
            ],
            ProvisionedThroughput={ 'ReadCapacityUnits': 10, 'WriteCapacityUnits': 10 }
        )
        self.table.put_item(Item={ 'RecipeID': 'sample_recipe_id' })

        # Act
        event = { 'recipe_id' : 'non_existent_recipe_id' }
        context = {}
        response = lambda_handler(event, context)

        # Assert
        self.assertEqual(response['statusCode'], 404)
        self.assertIn('body', response)
        self.assertEqual(response['body']['error'], 'Item not found')

if __name__ == '__main__':
    unittest.main()