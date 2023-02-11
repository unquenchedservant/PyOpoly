'''
This is where any necessary global variables will be. such as menu positions for various menus and what not, as well as things that need a cached storage.
this is probably janky, and I could just better implement a settings object, but that's less fun ;)
'''
def init():
    global main_position
    main_position = 1
    global current_menu
    current_menu = 1 # I'll have integers connected to each menu/submenu
    global y_pos
    y_pos = 1
    global x_pos
    x_pos = 1
    global current_player
    current_player = 1
