import json


def handler(event,context):
    print(f'Event Message: {json.dumps(event)}')