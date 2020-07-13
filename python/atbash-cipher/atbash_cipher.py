key = {'a':'z','b':'y','c':'x','d':'w','e':'v','f':'u','g':'t','h':'s','i':'r',
 'j':'q','k':'p','l':'o','m':'n','n':'m','o':'l','p':'k','q':'j','r':'i','s':'h',
 't':'g','u':'f','v':'e','w':'d','x':'c','y':'b','z':'a'}

def encode(plain_text):
    encoded = ''
    char_count = 0
    for c in plain_text:
        if char_count == 5:
            encoded += ' '
            char_count = 0
        if c.isalpha():
            encoded += key[c.lower()]
            char_count += 1
        elif c.isnumeric():
            encoded += c
            char_count += 1
    return encoded.rstrip()


def decode(ciphered_text):
    decoded = ''
    for c in ciphered_text:
        if c.isalpha():
            decoded += key[c.lower()]
        elif c.isdigit():
            decoded += c
    return decoded
