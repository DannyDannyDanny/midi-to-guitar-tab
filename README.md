# Moodoo
Python program for displaying / converting an midi file exported from ableton (containg a melody) into plaintext guitar tabs.

## Install

```
git clone https://github.com/DannyDannyDanny/midi-to-guitar-tab/
cd midi-to-guitar-tab
pipenv install
pipenv shell
pip install -e .
python -m src   # run main
pytest          # test
```

## Next Steps
* [Get inspired from kord](https://github.com/synestematic/kord)

## Running Tool
* `python test_ui.py` will launch cli ui for `'midifiles/sad_rude2.mid'`

Resources:
* [billroy/jsonio.py for put/get](https://gist.github.com/billroy/3761495)
* [claymcleod/pycurses.py Curses (python ui) example](https://gist.github.com/claymcleod/b670285f334acd56ad1c)
