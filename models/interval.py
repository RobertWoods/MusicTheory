from CircleOfFifths import CircleOfFifths
from note import Note

class Interval:

    qualities = {'P' : 0, 'M' : 0, 'm' : -1, 'A' : 1, 'd' : -2, 'dd' : -3, 'dA' : 2}

    def __init__(self, root, number, quality, lower=False):
        self.number = number
        self.quality = quality

        if(lower):
            self.other = root
            self.root = calculate_other(lower)
        else:
            self.root = root
            self.other = calculate_other(lower)

    def calculate_other(self, lower):
        if(lower):
            position = CircleOfFifths.circle.index(self.other)
            root_position = (position - (self.number-1)) % len(CircleOfFifths.circle)
            root_letter = CircleOfFifths.circle[root_position]
            test_accidental = 2
            test_note = Note(root_letter, test_accidental)
            key = CircleOfFifths.get_key(test_note)
            while(not key.has_note(self.other)):
                test_accidental -= 1
                test_note = Note(root_letter, test_accidental)
                key = CircleOfFifths.get_key(test_note)
            test_accidental += self.qualities[self.quality]
            return Note(root_letter, test_accidental)
        else:
            position = CircleOfFifths.circle.index(self.root)
            other_position = (position + self.number-1) % len(CircleOfFifths.circle)
            other_letter = CircleOfFifths.circle[other_position]
            key = CircleOfFifths.get_key(self.root)
            other_accidental = key[other_position] + self.qualities[self.quality]
            return Note(other_latter, other_accidental)

    def __str__(self):
        return "(%s, %s)" % (self.root, self.other)
