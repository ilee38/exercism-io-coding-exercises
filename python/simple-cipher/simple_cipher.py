class Cipher:
    def __init__(self, key=None):
        self.key = key
        self._alphabet = 'abcdefghijklmnopqrstuvwxyz'


    def encode(self, text):
        encoded = ''
        key = self._alphabet.index('d')
        for letter in text:
            idx = self._alphabet.index(letter) + key
            encoded += self._alphabet[idx]
        self.key = encoded.lower()
        return encoded


    def decode(self, text):
        pass





