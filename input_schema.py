INPUT_SCHEMA = {
    "text": {
        'datatype': 'STRING',
        'required': True,
        'shape': [1],
        'example': ["The sky above the port was the color of television, tuned to a dead channel."]
    },
    "voice": {
        'datatype': 'STRING',
        'required': False,
        'shape': [1],
        'example': ["af_heart"]
    },
    "split_pattern": {
        'datatype': 'STRING',
        'required': False,
        'shape': [1],
        'example': ["\n+"]
    }
}
IS_STREAMING_OUTPUT = True
