from models.CircleOfFifths import CircleOfFifths
from models.interval import Interval
from models.key import Key
from models.note import Note
from models.triad import Triad
from sys import argv

if __name__ == "__main__":
    if(len(argv) > 3):
        note = Note(argv[2], int(argv[3]))
        if(argv[1] == "-i"):        #interval
            if len(argv) < 6:
                print("-i takes 4 parameters: note, accidental, interval size, quality")
                exit()
            print(Interval(note, int(argv[4]), argv[5]))
        elif (argv[1] == "-t"):     #triad
            if len(argv) < 5:
                print("-t takes 3 parameters: note, accidental, quality")
                exit()
            print(Triad(note, argv[4]))
        elif (argv[1] == "-k"):     #key
            if len(argv) < 4:
                print("-k takes 2 parameters: note, accidental")
            print(CircleOfFifths.get_key(note))
