import unittest
from ..update_recipe import lambda_handler
from moto import mock_aws
import boto3

class TestUpdateItem(unittest.TestCase):

    @mock_aws
    def test_lambda_handler_success(self):
        # Arrange
        self.dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
        self.table_name = 'Recipes'
        self.table = self.dynamodb.create_table(
            TableName=self.table_name,
            KeySchema=[
                { 'AttributeName': 'RecipeID', 'KeyType': 'HASH' }
            ],
            AttributeDefinitions=[
                { 'AttributeName': 'RecipeID', 'AttributeType': 'S' }
            ],
            ProvisionedThroughput={ 'ReadCapacityUnits': 10, 'WriteCapacityUnits': 10 }
        )
        self.table.put_item(Item={ 'RecipeID': 'sample_recipe_id', 'VisitsCounter': 0 })

        # Act
        event = { 'recipe_id' : 'sample_recipe_id' }
        context = {}
        response = lambda_handler(event, context)

        # Assert
        self.assertIn('VisitsCounter', response['value'])
        self.assertEqual(response['value']['VisitsCounter'], 1)

    @mock_aws
    def test_lambda_handler_non_existent_recipe_id(self):
        # Arrange
        self.dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
        self.table_name = 'Recipes'
        self.table = self.dynamodb.create_table(
            TableName=self.table_name,
            KeySchema=[
                { 'AttributeName': 'RecipeID', 'KeyType': 'HASH' }
            ],
            AttributeDefinitions=[
                { 'AttributeName': 'RecipeID', 'AttributeType': 'S' }
            ],
            ProvisionedThroughput={ 'ReadCapacityUnits': 10, 'WriteCapacityUnits': 10 }
        )
        self.table.put_item(Item={ 'RecipeID': 'sample_recipe_id', 'VisitsCounter': 0 })

        # Act
        event = { 'recipe_id' : 'non_existent_recipe_id' }
        context = {}
        response = lambda_handler(event, context)

        # Assert
        self.assertIn('message', response['error'])

if __name__ == '__main__':
    unittest.main()