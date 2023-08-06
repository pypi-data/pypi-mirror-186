import base64
import pickle

import lz4.frame


def encode_payload(payload):
    compressed = lz4.frame.compress(pickle.dumps(payload))
    return base64.b64encode(compressed).decode('utf-8')


def decode_payload(payload):
    compressed = base64.b64decode(payload)
    return pickle.loads(lz4.frame.decompress(compressed))