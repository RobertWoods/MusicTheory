class Key:
    def __init__(self, signature):
        self.signature = signature

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
