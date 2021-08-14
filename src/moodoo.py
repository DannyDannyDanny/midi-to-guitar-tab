import mido
from mido import MidiFile
import os


def generate_string_list(m, visvar=None):
    notelist = m.get_notelist()
    notebaglist = m.get_note_bag_list()
    vislist = m.note_bag_list_to_visual(notebaglist)
    if visvar is None:
        visvar = [1 for vis in vislist] # <---- edit this to change variations

    string_list = []

    string_list.append('octave\t|note\t|playable(string,fret)\t|variation')
    for i,(visnote,(oct,note)) in enumerate(zip(vislist,notelist)):
        playable = m.note_dict[note,oct+1] #TODO
        variation = visvar[i]
        note_vis = visnote[variation]
        v = 1
        # variatin number string i.e [1/3]
        varnostr = '['+str(v)+'/'+str(len(visnote))+']'
        # print(oct,'\t',note,'\t',playable)
        string_list.append(str(oct)+'\t\t|'+str(note)+'\t'+note_vis+'\t\t|'+varnostr)
    return string_list

class moodoo:
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
        if self.debug: print('octave\t|note\t|playable(string,fret)')
        for oct,note in self.notelist:
            playable = self.note_dict[note,oct+1] #TODO
            self.note_bag_list.append(playable)
            if self.debug: print(str(oct)+'\t|'+note+'\t|'+str(playable))

    def get_notelist(self):
        return self.notelist

    def get_note_bag_list(self):
        return self.note_bag_list

    def note_bag_list_to_visual(self,n):
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
