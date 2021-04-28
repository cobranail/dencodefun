import html

setting={
}

def encode(content='', setting={}):
    return html.escape(content)

def decode(content='', setting={}):
    return html.unscape(content)
