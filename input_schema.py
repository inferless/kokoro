INPUT_SCHEMA = {
    "text": {
        'datatype': 'STRING',
        'required': True,
        'shape': [1],
        'example': ["Welcome to this beautiful world."]
    },
    "voice": {
        'datatype': 'STRING',
        'required': False,
        'shape': [1],
        'example': ["af_heart"]
    },
    "speed": {
        'datatype': 'FP32',
        'required': False,
        'shape': [1],
        'example': [1.0]
    },
    "split_pattern": {
        'datatype': 'STRING',
        'required': False,
        'shape': [1],
        'example': ["\n+"]
    }
}
IS_STREAMING_OUTPUT = True
