import mido
from mido import MidiFile
import os
from src.moodoo import moodoo, generate_string_list

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

position_index_list = [(0,len(n)) for n in notebaglist]
notebaglist
for note,i in zip(vislist,position_index_list):
    print([vis for vis in note][0],i[0],'/',i[1])

# %%
for i in zip(notelist,vislist):
    print(i)

# %%
m = moodoo('midifiles/sad_rude2.mid')

# string_list = generate_string_list(m)

# for s in string_list:
#     print(s)

# %%
for oct,note in notelist:
    playable = m.note_dict[note,oct+1] #TODO
    # self.note_bag_list.append(playable)
    print(str(oct)+'\t|'+note+'\t|'+str(playable))
