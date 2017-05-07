class Note:
    def __init__(self, letter, accidental):
        self.letter = letter
        self.accidental = accidental

    def __str__(self):
        symbol = '#' if self.accidental >= 0 else 'b'
        return self.letter + symbol * abs(self.accidental)

    def __repr__(self):
        return "Note(%s, %s)" % (self.letter, self.accidental)
