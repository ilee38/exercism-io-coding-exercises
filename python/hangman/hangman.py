# Game status categories
# Change the values as you see fit
STATUS_WIN = "win"
STATUS_LOSE = "lose"
STATUS_ONGOING = "ongoing"


class Hangman(object):
    def __init__(self, word):
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING
        self._word = word
        self.masked_word = ''
        for _ in range(len(word)):
            self.masked_word += '_'

    def guess(self, char):
        if self.status == STATUS_LOSE or self.status == STATUS_WIN:
            raise ValueError(self.status)
        if char not in self._word or char in self.masked_word:
            self.remaining_guesses -= 1
            if self.remaining_guesses < 0:
                self.status = STATUS_LOSE
        else:
            temp_word = ''
            for i in range(len(self._word)):
                if self._word[i] == char:
                    temp_word += char
                else:
                    temp_word += self.masked_word[i]
            self.masked_word = temp_word
            if self._word == self.masked_word:
                self.status = STATUS_WIN

    def get_masked_word(self):
        return self.masked_word

    def get_status(self):
        return self.status
