import mido
from mido import MidiFile
from pynput.keyboard import Key, Listener
import os
from moodoo import moodoo

note = 0

m = moodoo('midifiles/sad_rude2.mid')

notelist = m.get_notelist()

notebaglist = m.get_note_bag_list()

# %%
print('octave\t|note\t|playable(string,fret)')
for oct,note in notelist:
    playable = m.note_dict[note,oct+1] #TODO
    print(oct,'\t',note,'\t',playable)
# %%

# %%
for oct,note in notelist:
    playable = m.note_dict[note,oct+1] #TODO
    # self.note_bag_list.append(playable)
    print(str(oct)+'\t|'+note+'\t|'+str(playable))


# %%

m = moodoo('midifiles/sad_rude2.mid')
dat = m.get_note_bag_list()

# %%

arr = [0 for _ in dat]
lim = [len(i) for i in dat]
print('note',note)
print('dat',dat)
print('arr',arr)
print('lim',lim)
print('ready')

# %%
# for note_tuples in dat:
#     print(note_tuple)
#     for tuple in note_tuples:
#         print(tuple_to_visual(tuple))

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


#TODO maxfret
