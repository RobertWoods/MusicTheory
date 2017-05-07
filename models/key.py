class Key:
    def __init__(self, note):
        self.signature = CircleOfFifths.get_key(note)
