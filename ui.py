import mido
from mido import MidiFile
from pynput.keyboard import Key, Listener
import os

class moodoo:
    """A simple example class"""

    # notes in an octave
    notes = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']
    # root notes in standard tuned guitar
    #strings = list('EADGBE') #TODO delete?
    debug = False
    # root notes in standard tuned guitar
    strings = [(note,int(oct)) for note,oct in zip(list('EADGBE'),list('001112'))]
    # frets on guitar
    frets_on_guitar = 24
    v = 4


    def __init__(self, path='midifiles/vapor.mid'):
        # load midifile
        self.mid = MidiFile(path)
        # extract note list from midi file
        self.notelist = []
        for i, track in enumerate(self.mid.tracks):
            for msg in track:
                if not msg.is_meta and msg.type == 'note_on':
                    # save message octave and note to notelist
                    self.notelist.append((msg.note//12,self.notes[msg.note%12]))

        # make the lowest octave zero
        minoct = min([oct for oct,note in self.notelist])
        self.notelist = [(oct-minoct,note) for oct,note in self.notelist]

        # build note dict note_to_fret
        self.note_dict = dict()
        # iterate over guitar strings
        for string_number,(string_note,string_octave) in enumerate(self.strings):
            if self.debug: print('string:',string_note,'('+str(string_octave)+')')
            _s = 'what frets can be played the {} string (octave {})?'
            if self.debug: print(_s.format(string_note,string_octave))
            # iterate over frets on string
            for fret in range(self.frets_on_guitar+1):
                # calculate note at this fret
                note = self.notes[(self.notes.index(string_note)+fret)%len(self.notes)]
                # calculate octave at this fret
                # TODO shorten following line
                note_octave = string_octave + (self.notes.index(string_note)+fret)//len(self.notes)
                if self.debug: print('fret:',fret,'\tnote:',note,'\toctave:',note_octave)
                # add note-octave tuple as key if not already present
                if (note,note_octave) not in self.note_dict.keys():
                    self.note_dict[(note,note_octave)] = []
                # add string number and fret as value to note-octave key
                self.note_dict[(note,note_octave)].append((string_number,fret))

        self.note_bag_list = []
        print('octave\t|note\t|playable(string,fret)')
        for oct,note in self.notelist:
            playable = self.note_dict[note,oct+1] #TODO
            self.note_bag_list.append(playable)
            print(str(oct)+'\t|'+note+'\t|'+str(playable))


    def get_note_bag_list(self):
        return self.note_bag_list

class moodoo_ui:
    """A simple example class"""

    def __init__(self, dat):
	    self.dat = dat

    def printy(dat,arr,lim,note):
        for i,v in enumerate(arr):
            vis = tuple_to_visual(dat[i][v])
            if i == note:
                #print(i,v,dat[i][v],'<----')
                print(vis,'<----')
            else:
                #print(i,v,dat[i][v])
                print(vis)

    def on_press(key):
        global note
        os.system('clear') # on linux / os x
        print('{0} pressed'.format(key))
        # moving which note to change
        if str(key) == 'Key.up':
            note -= 1
        if str(key) == 'Key.down':
            note += 1
        # limiting note index
        if note > len(arr)-1:
            note -= len(arr)
        if note < 0:
            note = len(arr)-1
        # moving fret to change
        if str(key) == 'Key.right':
            arr[note] += 1
        if str(key) == 'Key.left':
            arr[note] -= 1
        # limiting fret index
        if arr[note] < 0 or arr[note] > lim[note] - 1:
            arr[note] = arr[note] % lim[note]
        moodoo_ui.printy(dat,arr,lim,note)

    def on_release(key):
        #print('{0} release'.format(key))

        if key == Key.esc: # Stop listener
            return False

# Collect events until released

#arr = [note for note in range(10)]

note = 0
# dat = []
# dat.append([('A',1),('B',2),('C',3)])
# dat.append([('D',4),('E',5),('F',6)])
# dat.append([('G',7),('H',8),('I',9)])

m = moodoo('midifiles/sad_rude2.mid')
dat = m.get_note_bag_list()
arr = [0 for _ in dat]
lim = [len(i) for i in dat]

# print('note',note)
# print('dat',dat)
# print('arr',arr)
# print('lim',lim)
# print('ready')

#%%
def tuple_to_visual(t):
    """
    given a (string,fret)-tuple return visual string
    example:
    input: (2,11)
    output: '| | 11| | | '
    """
    def fill(x):
        """returns 2-char long str cast of some input"""
        if len(str(x)) == 1:
            return str(x)+' '
        else:
            return str(x)

    s = ''
    for i in range(6):
        if i == t[0]:
            s += fill(t[1])
        else:
            s += '| '
    return s

def note_bag_list_to_visual(n):
    def bag_to_visual(b):
        def tuple_to_visual(t):
            """
            given a (string,fret)-tuple return visual string
            example:
            input: (2,11)
            output: '| | 11| | | '
            """
            def fill(x):
                """returns 2-char long str cast of some input"""
                if len(str(x)) == 1:
                    return str(x)+' '
                else:
                    return str(x)

            s = ''
            for i in range(6):
                if i == t[0]:
                    s += fill(t[1])
                else:
                    s += '| '
            return s
        return [tuple_to_visual(p) for p in b]
    return [bag_to_visual(b) for b in n]


#%%



#TODO maxfret

with Listener(
	on_press=moodoo_ui.on_press,
	on_release=moodoo_ui.on_release) as listener:
    listener.join()