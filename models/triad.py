from models.interval import Interval

class Triad:

    qualities = [
        {'d' : 'm', 'm' : 'm', 'M' : 'M', 'A' : 'M'}, #Third
        {'d' : 'm', 'm' : 'M', 'M' : 'M', 'A' : 'A'}  #Fifth
    ]

    def __init__(self, root, quality):
        self.root = root
        self.quality = quality
        self.third = Interval(root, 3, self.qualities[0][quality]).other
        self.fifth = Interval(root, 5, self.qualities[1][quality]).other

    def __str__(self):
        return "(%s, %s, %s)" % (self.root, self.third, self.fifth)

    def __repr__(self):
        return "Triad(%s, %s)" % (root, quality)
