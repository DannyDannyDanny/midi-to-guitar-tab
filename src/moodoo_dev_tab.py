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

for oct,note in notelist:
    playable = m.note_dict[note,oct+1] #TODO
    # self.note_bag_list.append(playable)
    print(str(oct)+'\t|'+note+'\t|'+str(playable))
# E|-------5-7-----7-|-8-----8-2-----2-|-0---------0-----|-----------------|
# B|-----5-----5-----|---5-------3-----|---1---1-----1---|-0-1-1-----------|
# G|---5---------5---|-----5-------2---|-----2---------2-|-0-2-2-----------|
# D|-7-------6-------|-5-------4-------|-3---------------|-----------------|
# A|-----------------|-----------------|-----------------|-2-0-0---0--/8-7-|
# E|-----------------|-----------------|-----------------|-----------------|
for note in moodoo.notes:
    print(note)
for note_of_string,oct in reversed(moodoo.strings):
    print(note_of_string,'|'+str(20*'-'))


for i,(note_of_string,oct) in enumerate(reversed(moodoo.strings)):
    note_i = len(moodoo.strings) - i
    print(note_i,note_of_string,'|'+str(20*'-'))

position_index_list = [(0,len(n)) for n in notebaglist]

for i,n in zip(position_index_list,notebaglist):
    print(i[0],'/',i[1],n[i[0]])


for note,i in zip(vislist,position_index_list):
    print([vis for vis in note][0],i[0],'/',i[1])
