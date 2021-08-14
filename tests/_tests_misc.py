from src import ui
from src.moodoo import moodoo
import src.filemanager as fm
import os


def test_moodoo():
    datfile = ['/', 'U', 's', 'e', 'r', 's', '/', 'd', 't', 'h', '/', 'D', 'o', 'c', 'u', 'm', 'e', 'n', 't', 's', '/', 'd', 'e', 'v', '/', '2', '0', '1', '8', '/', '\n', 'm', 'i', 'd', 'i', '-', 't', 'o', '-', 'g', 'u', 'i', 't', 'a', 'r', '-', 't', 'a', 'b', '/', 'm', 'i', 'd', 'i', 'f', 'i', 'l', 'e', 's', '/', 's', '\n', 'a', 'd', '_', 'r', 'u', 'd', 'e', '2', '.', 'm', 'i', 'd', ' ', '\n']
    # remove newlines
    datfile = list(filter(lambda a: a != '\n', datfile))
    datfile = ''.join(datfile).strip()
    m = moodoo(datfile)
    notelist = m.get_notelist()
    notebaglist = m.get_note_bag_list()
    vislist = m.note_bag_list_to_visual(notebaglist)
    return len(vislist) > 0

# test_moodoo()

def test_mood_2():
    datfile = ui.ui_get_file()
    datfile = [c for c in datfile]
    # remove newlines
    datfile = list(filter(lambda a: a != '\n', datfile))
    datfile = ''.join(datfile).strip()
    datfile

    m = moodoo(datfile)
    notelist = m.get_notelist()
    notebaglist = m.get_note_bag_list()
    vislist = m.note_bag_list_to_visual(notebaglist)


# %%

import json
list = [1, 2, (3, 4)] # Note that the 3rd element is a tuple (3, 4)
json.dumps(list) # '[1, 2, [3, 4]]'

m = moodoo('midifiles/sad_rude2.mid')
notelist = m.get_notelist()
notebaglist = m.get_note_bag_list()
vislist = m.note_bag_list_to_visual(notebaglist)
notedict = m.note_dict

ui.navigate()


# file_dir = ui.get_file_dir()
