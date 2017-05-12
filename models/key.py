class Key:
    def __init__(self, signature, minor=0):
        self.signature = signature
        self.descending = None
        if minor == 1: #minor
            self.signature[5] -= 1
            self.signature[6] -= 1
        elif minor == 2: #harmonic minor
            self.signature[5] -= 1
        elif minor == 3: #melodic minor
            self.descending = list(self.signature)
            self.descending[5] -= 1
            self.descending[6] -= 1
            pass

    def has_note(self, note, circle):
        position = circle.index(note.letter)
        return note.accidental == self.signature[position]

    def __str__(self):
        return str(self.signature)

    def __getitem__(self, key):
        return self.signature[key]

    def __setitem__(self, key, value):
        self.signature[key] = value

    def __delitem__(self, key):
        del self.signature[key]

    def is_melodic(self):
        return self.descending is not None
