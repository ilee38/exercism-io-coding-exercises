def rotate(text, key):
    plain = "abcdefghijklmnopqrstuvwxyz"
    cipher_txt = ""
    curr_char = ""
    L = len(plain)
    index = 0
    for c in text:
        if c.isalpha():
            index = plain.find(c.lower())
            curr_char = plain[(index + key) % L]
            if c.islower():
                cipher_txt += curr_char
            else:
                cipher_txt += curr_char.upper()
        else:
            cipher_txt += c
    return cipher_txt
