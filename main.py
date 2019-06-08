import ui

# datfile = ui.ui_get_file()
# datfile = [c for c in datfile])

datfile = ['/', 'U', 's', 'e', 'r', 's', '/', 'd', 't', 'h', '/', 'D', 'o', 'c', 'u', 'm', 'e', 'n', 't', 's', '/', 'd', 'e', 'v', '/', '2', '0', '1', '8', '/', '\n', 'm', 'i', 'd', 'i', '-', 't', 'o', '-', 'g', 'u', 'i', 't', 'a', 'r', '-', 't', 'a', 'b', '/', 'm', 'i', 'd', 'i', 'f', 'i', 'l', 'e', 's', '/', 's', '\n', 'a', 'd', '_', 'r', 'u', 'd', 'e', '2', '.', 'm', 'i', 'd', ' ', '\n']
# remove newlines
datfile = list(filter(lambda a: a != '\n', datfile))
datfile = ''.join(datfile)

# file_dir = ui.get_file_dir()
