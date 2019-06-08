import sys,os
import curses
from curses.textpad import Textbox, rectangle
import filemanager as fm
from moodoo_dev import generate_string_list
from moodoo import moodoo

def ui_get_file():
    def get_file(stdscr):
        stdscr.addstr(0, 0, "Enter IM message: (hit Ctrl-G to send)")

        editwin = curses.newwin(5,30, 2,1)
        rectangle(stdscr, 1,0, 1+5+1, 1+30+1)
        stdscr.refresh()

        box = Textbox(editwin)

        # Let the user edit until Ctrl-G is struck.
        box.edit()

        # Get resulting contents
        message = box.gather()
        return message
    return curses.wrapper(get_file)

def draw_menu(stdscr):
    m = moodoo('midifiles/sad_rude2.mid')
    notelist = m.get_notelist()
    notebaglist = m.get_note_bag_list()
    vislist = m.note_bag_list_to_visual(notebaglist)
    notedict = m.note_dict



    k = 0
    cursor_x = 0
    cursor_y = 0

    # string_list = fm.get('string_list.json')
    visvar = [0 for vis in vislist]
    string_list = generate_string_list(m,visvar)

    # Clear and refresh the screen for a blank canvas
    stdscr.clear()
    stdscr.refresh()

    # Start colors in curses
    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)

    # Loop where k is the last character pressed
    increm = 0
    while (k != ord('q')):
        increm = 0

        # Initialization
        stdscr.clear()
        height, width = stdscr.getmaxyx()

        if k == curses.KEY_DOWN:
            cursor_y = cursor_y + 1
        elif k == curses.KEY_UP:
            cursor_y = cursor_y - 1
        elif k == curses.KEY_RIGHT:
            increm = 1
            cursor_x = cursor_x + 1
        elif k == curses.KEY_LEFT:
            increm = -1
            cursor_x = cursor_x - 1

        cursor_x = max(0, cursor_x)
        cursor_x = min(width-1, cursor_x)

        cursor_y = max(0, cursor_y)
        cursor_y = min(height-1, cursor_y)

        # Declaration of strings
        keystr = "Last key pressed: {}".format(k)[:width-1]
        statusbarstr = "Press 'q' to exit | STATUS BAR | Pos: {}, {}".format(cursor_x, cursor_y)
        if k == 0:
            keystr = "No key press detected..."[:width-1]

        # Centering calculations
        start_x_keystr = int((width // 2) - (len(keystr) // 2) - len(keystr) % 2)
        start_y = int((height // 2) - 2)

        # Rendering some text
        whstr = "Width: {}, Height: {}".format(width, height)
        stdscr.addstr(0, 0, whstr, curses.color_pair(1))

        # Render status bar
        stdscr.attron(curses.color_pair(3))
        stdscr.addstr(height-1, 0, statusbarstr)
        stdscr.addstr(height-1, len(statusbarstr), " " * (width - len(statusbarstr) - 1))
        stdscr.attroff(curses.color_pair(3))

        # Turning on attributes for title
        stdscr.attron(curses.color_pair(2))
        stdscr.attron(curses.A_BOLD)

        # Turning off attributes for title
        stdscr.attroff(curses.color_pair(2))
        stdscr.attroff(curses.A_BOLD)

        # Print rest of text
        i_visvar = (cursor_y % len(vislist))+1

        visvar[i_visvar-1] += increm
        if visvar[i_visvar-1] > len(string_list[i_visvar-1]):
            visvar[i_visvar-1] = len(string_list[i_visvar-1])
        if visvar[i_visvar-1] < 0:
            visvar[i_visvar-1] = 0
        string_list = generate_string_list(m,visvar)
        for i,s in enumerate(string_list):
            if i == i_visvar:
                stdscr.addstr(2+i, 2, s+'<------')
            else:
                stdscr.addstr(2+i, 2, s)

        stdscr.move(cursor_y, cursor_x)

        # Refresh the screen
        stdscr.refresh()

        # Wait for next input
        k = stdscr.getch()

def navigate():
    curses.wrapper(draw_menu)
