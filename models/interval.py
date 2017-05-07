from models.CircleOfFifths import CircleOfFifths
from models.note import Note

class Interval:

    qualities = {'P' : 0, 'M' : 0, 'm' : -1, 'A' : 1, 'd' : -2, 'dd' : -3, 'dA' : 2}
    notes = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

    def __init__(self, root, number, quality, lower=False):
        self.number = number
        self.quality = quality

        if(lower):
            self.other = root
            self.root = self.calculate_other(lower)
        else:
            self.root = root
            self.other = self.calculate_other(lower)

    def calculate_other(self, lower):
        if(lower):
            position = self.notes.index(self.other.letter)
            root_position = (position - (self.number-1)) % len(self.notes)
            root_letter = self.notes[root_position]
            test_accidental = 2
            test_note = Note(root_letter, test_accidental)
            key = CircleOfFifths.get_key(test_note)
            while(not key.has_note(self.other, CircleOfFifths.circle)):
                test_accidental -= 1
                test_note = Note(root_letter, test_accidental)
                key = CircleOfFifths.get_key(test_note)
            test_accidental += self.qualities[self.quality]
            return Note(root_letter, test_accidental)
        else:
            position = self.notes.index(self.root.letter)
            other_position = (position + self.number-1) % len(self.notes)
            other_letter = self.notes[other_position]
            key = CircleOfFifths.get_key(self.root)
            other_accidental = key[other_position] + self.qualities[self.quality]
            return Note(other_letter, other_accidental)

    def __str__(self):
        return "(%s, %s)" % (self.root, self.other)
