import curses
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN
from random import randint

screen = curses.initscr()
h,w = screen.getmaxyx()

screen.border(0)
hw_str = ' height '+str(h)+', width '+str(w)+' '
ndashes = 20 #int(w/2)+int(len(hw_str)/2)-20

print_str = '-'*ndashes
print_str += hw_str
print_str += '-'*ndashes
screen.addstr(int(h/2), int(w/2)-int(len(print_str)/2), print_str)

print_str2 = 'ndashes: ' + str(ndashes)
screen.addstr(int(h/2)+1,int(w/2)-int(len(print_str2)/2), print_str2)

arr = [[str(j+i)[-1] for j in range(10)] for i in range(10)]
arr
for i_row,row in enumerate(arr):
    print(row)
    for i_c,c in enumerate(row):

        screen.addstr(i_row+10,i_c+10,c)

screen.addstr(0,0,'HI')
screen.refresh()
screen.getch()
curses.endwin()
