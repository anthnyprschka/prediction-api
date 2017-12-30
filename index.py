def lambda_handler(event, context):

    response = {
        "statusCode": 200,
        "headers": {
            "my_header": "my_value"
        },
        "body": "works indeed",
    };

    return response