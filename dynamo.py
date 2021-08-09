'''
This function is used to get values from a dynamodb table and update the value
'''
import json
import boto3

dynamodb_client = boto3.client('dynamodb')


def lambda_handler(event, context):

    # # Gets the item from Dynamodb
    # get_item_response = dynamodb_client.get_item(
    #     TableName='sites',
    #         Key={
    #             'name': {
    #                 'S': 'tvofik.xyz'
    #             },
    #         }
    #     #ProjectionExpression='visits',
    # )

    # print(get_item_response)

    # previous_visit_count = int(get_item_response['Item']['visits']['N'])
    # current_visit_count = previous_visit_count + 1

    # Update the visits attribute
    update_item_response = dynamodb_client.update_item(
        TableName='sites',
        Key={
            'name': {
                'S': 'tvofik.xyz',
            }
        },
        UpdateExpression='SET visits = visits + :val',
        ExpressionAttributeValues={
            ":val": {"N": "1"}
        },
    )

    print(update_item_response)
