#!/usr/bin/env python
# coding: utf-8

import json
import boto3
import os


dynamodb = boto3.resource("dynamodb")

table = dynamodb.Table(os.environ["table"])


def handler(event, context):
    headers = {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Credentials": True,
    }
    try:
        response = table.get_item(Key={"product": "Primo"})
        return {
            "statusCode": 200,
            "headers": headers,
            "body": json.dumps(response["Item"]),
        }
    except:
        return {
            "statusCode": 500,
            "headers": headers,
            "body": json.dumps(
                {
                    "result": "An error has occurred, please check with your local library developer."
                }
            ),
        }
