class Note:
    def __init__(self, letter, accidental):
        self.letter = letter
        self.accidental = accidental

    def __str__(self):
        if(self.accidental >= 0):
            return self.letter + ('x' * int(self.accidental / 2)) + ('#' * int(self.accidental % 2))
        else:
            return self.letter + 'b' * abs(self.accidental)

    def __repr__(self):
        return "Note(%s, %s)" % (self.letter, self.accidental)
