import mido
from mido import MidiFile
from pynput.keyboard import Key, Listener
import os
from moodoo import moodoo

note = 0

m = moodoo('midifiles/sad_rude2.mid')
notelist = m.get_notelist()
notebaglist = m.get_note_bag_list()
vislist = m.note_bag_list_to_visual(notebaglist)
for visnote,notenote in zip(vislist,notelist):
    print(notenote,'\t<',3*'-',len(visnote))
    for visnotevar in visnote:
        print(visnotevar)
# %%

for note in vislist:
    print([vis for vis in note][0])

# %%
for i in zip(notelist,vislist):
    print(i)

# %%
m = moodoo('midifiles/sad_rude2.mid')
def generate_string_list(m,visvar):
    notelist = m.get_notelist()
    notebaglist = m.get_note_bag_list()
    vislist = m.note_bag_list_to_visual(notebaglist)
    # visvar = [1 for vis in vislist] # <---- edit this to change variations

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

# string_list = generate_string_list(m)

# for s in string_list:
#     print(s)

# %%
for oct,note in notelist:
    playable = m.note_dict[note,oct+1] #TODO
    # self.note_bag_list.append(playable)
    print(str(oct)+'\t|'+note+'\t|'+str(playable))
