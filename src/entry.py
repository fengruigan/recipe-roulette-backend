import json


def handler(event, context):
    # main entry point for lambda
    return json.dumps({"message": "To be implemented"})


if __name__ == '__main__':
    handler({"key": "value"}, None)