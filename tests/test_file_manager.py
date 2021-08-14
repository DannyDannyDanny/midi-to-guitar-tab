from src import filemanager as fm


def test_filemanager():
    somelist = ['a',1,[3,9]]
    fm.put(somelist, 'dink.json')
    getsomelist = fm.get('dink.json')
    return somelist == getsomelist


if __name__ == "__main__":
    test_filemanager()