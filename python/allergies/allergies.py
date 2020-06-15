class Allergies:

    def __init__(self, score):
        self._lst = self._get_list(score)

    def allergic_to(self, item):
        return item in self.lst

    @property
    def lst(self):
        return self._lst

    def _get_list(self, score):
        items = ['eggs', 'peanuts', 'shellfish', 'strawberries', 'tomatoes', 'chocolate', 'pollen', 'cats']
        lst = []
        s = bin(score)
        s = s.lstrip('0b')
        if len(s) > 8:
            s = s[len(s)-8:]
        idx = len(s) - 1
        for digit in s:
            if digit == '1':
                lst.append(items[idx])
            idx -= 1
        return lst
