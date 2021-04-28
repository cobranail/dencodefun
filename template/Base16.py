import base64

setting={
    'coding':'utf-8'
}

def encode(content='', setting={}):
    return base64.b16encode(content.encode(setting['coding']))

def decode(content='', setting={}):
    return base64.b16decode(content.encode(setting['coding']))



