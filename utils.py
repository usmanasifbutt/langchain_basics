import base64

def decode_file(path: str):
    with open(path, 'rb') as f:
        return base64.b64encode(f.read()).decode('utf-8')