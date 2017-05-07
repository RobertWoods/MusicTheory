from CircleOfFifths import CircleOfFifths

class Key:
    def __init__(self, note):
        self.signature = CircleOfFifths.get_key(note)

    def has_note(self, note):
        position = CircleOfFifths.circle.index(note.letter)
        return note.accidental == self.signature[position]

    def __str__(self):
        return self.signature
