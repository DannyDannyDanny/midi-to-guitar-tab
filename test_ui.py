import ui
from moodoo import moodoo
import os

def test_filemanager():
    import filemanager as fm
    somelist = ['a',1,[3,9]]
    fm.put(somelist, 'dink.json')
    getsomelist = fm.get('dink.json')
    return somelist == getsomelist

test_filemanager()

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

test_moodoo()

if False:
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
vislist = [['22| | | | | ',
  '| 17| | | | ',
  '| | 12| | | ',
  '| | | 7 | | ',
  '| | | | 3 | '],
 ['| 20| | | | ',
  '| | 15| | | ',
  '| | | 10| | ',
  '| | | | 6 | ',
  '| | | | | 1 '],
 ['18| | | | | ', '| 13| | | | ', '| | 8 | | | ', '| | | 3 | | '],
 ['20| | | | | ',
  '| 15| | | | ',
  '| | 10| | | ',
  '| | | 5 | | ',
  '| | | | 1 | '],
 ['13| | | | | ', '| 8 | | | | ', '| | 3 | | | '],
 ['23| | | | | ',
  '| 18| | | | ',
  '| | 13| | | ',
  '| | | 8 | | ',
  '| | | | 4 | '],
 ['22| | | | | ',
  '| 17| | | | ',
  '| | 12| | | ',
  '| | | 7 | | ',
  '| | | | 3 | '],
 ['| 20| | | | ',
  '| | 15| | | ',
  '| | | 10| | ',
  '| | | | 6 | ',
  '| | | | | 1 '],
 ['| | 20| | | ', '| | | 15| | ', '| | | | 11| ', '| | | | | 6 '],
 ['| | 22| | | ', '| | | 17| | ', '| | | | 13| ', '| | | | | 8 '],
 ['| 24| | | | ',
  '| | 19| | | ',
  '| | | 14| | ',
  '| | | | 10| ',
  '| | | | | 5 '],
 ['| | 20| | | ', '| | | 15| | ', '| | | | 11| ', '| | | | | 6 ']]
# %%

import json
list = [1, 2, (3, 4)] # Note that the 3rd element is a tuple (3, 4)
json.dumps(list) # '[1, 2, [3, 4]]'


vislist

ui.navigate()


# file_dir = ui.get_file_dir()
