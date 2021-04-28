
setting={
    'dot':'.',
    'dash':'-',
    'char':' ',
    'word':'/'
}

chars = ",.0123456789?abcdefghijklmnopqrstuvwxyz"
codes = """--..-- .-.-.- ----- .---- ..--- ...-- ....- ..... -.... --... ---..
      ----. ..--.. .- -... -.-. -... . ..-. --. .... .. .--- -.- .-.. --
      -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --.."""

keys = {',': '--..--', '.': '.-.-.-', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '?': '..--..', 'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-...', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..'}
unkeys = {'--..--': ',', '.-.-.-': '.', '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9', '..--..': '?', '.-': 'a', '-...': 'd', '-.-.': 'c', '.': 'e', '..-.': 'f', '--.': 'g', '....': 'h', '..': 'i', '.---': 'j', '-.-': 'k', '.-..': 'l', '--': 'm', '-.': 'n', '---': 'o', '.--.': 'p', '--.-': 'q', '.-.': 'r', '...': 's', '-': 't', '..-': 'u', '...-': 'v', '.--': 'w', '-..-': 'x', '-.--': 'y', '--..': 'z'}

#keys = dict(zip(chars, codes.split()))
#unkeys = dict(zip(codes.split(), chars))
#print(keys)
#print(unkeys)

def formatdecode(content, setting):
    r = content.replace(setting['dot'], '(dot)')
    r = r.replace(setting['dash'], '(dash)')
    r = r.replace(setting['char'], ' ')
    r = r.replace(setting['word'], ' ')

    r = r.replace('(dot)','.')
    r = r.replace('(dash)','-')
    return r

def formatencode(content, setting):
    r = content
    r = r.replace('.','(dot)')
    r = r.replace('-','(dash)')
    r = r.replace('(dot)',setting['dot'])
    r = r.replace('(dash)', setting['dash'])
    r = r.replace(' ',setting['char'])
    r = r.replace('/',setting['word'])


    return r

def char2morse(char):
    return keys.get(char.lower(), char)

def morse2char(char):
    return unkeys.get(char.lower(), char)

def encode(content='', setting={}):
    #print(setting)
    buff= []
    for c in content:
        buff.append(char2morse(c))
    r = ' '.join(buff)
    return formatencode(r, setting)

def decode(content='', setting={}):
    r = formatdecode(content, setting)
    elems = r.split()
    buff = ''
    for c in elems:
        buff = buff + morse2char(c)
    return buff

