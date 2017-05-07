from models.key import Key

class CircleOfFifths:
    circle = ['B','E','A','D','G','C','F']
    pivot = circle.index('C')

    @classmethod
    def get_key(cls, note):
        circle = cls.circle
        pivot = cls.pivot
        position = circle.index(note.letter)
        accidental = note.accidental
        if accidental < 0 or (note.letter == 'F' and accidental == 0):
            num_accidentals = 2 + (position % (len(circle)-1)) - int(position / (len(circle)-1))
            key = ([-1] * num_accidentals) + ([0] * (len(circle) - num_accidentals))
            if(note.letter != 'F'):
                accidental += 1
        else:
            num_accidentals = pivot - (position % len(circle)) - int(position / (len(circle)-1))
            key = ([0] * (len(circle) - num_accidentals)) + ([1] * num_accidentals)
            if(position >= pivot and accidental > 0):
                accidental-=1
        key = [x+accidental for x in key]
        return Key(key)
