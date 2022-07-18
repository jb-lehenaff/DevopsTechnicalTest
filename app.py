# -*- coding: utf-8 -*-

import boto3

def push_to_s3(event_body, event_client, message_id):
    s3 = boto3.resource('s3')
    filepath = event_client + '/' + message_id + '.json'
    s3.upload_fileobj(io.BytesIO(event_body.encode("utf-8")), Key=filepath)


def process_event(event):
    push_to_s3(event['body'], event_client, message_id)


def lambda_handler(event, context):
    try:
        process_event(event)
    except Exception:
        raise Exception("Unknown error")