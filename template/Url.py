import urllib.parse

setting={

}

def encode(content='', setting={}):
    return urllib.parse.quote_plus(content)

def decode(content='', setting={}):
    return urllib.parse.unquote_plus(content)



