import os
from src import ui
from src.moodoo import moodoo
import src.filemanager as fm
from src.moodoo import generate_string_list

# Launch UI and get path to midi file
# datfile = ui.ui_get_file()
# datfile = [c for c in datfile])

m = moodoo('midifiles/sad_rude2.mid')
notelist = m.get_notelist()
notebaglist = m.get_note_bag_list()
vislist = m.note_bag_list_to_visual(notebaglist)
notedict = m.note_dict

string_list = generate_string_list(m)
fm.put(string_list, 'string_list.json')
fm.put(vislist, 'vislist.json')
fm.put(notelist, 'notelist.json')
fm.put(notedict, 'notedict.json')
# ui.navigate()

# file_dir = ui.get_file_dir()
