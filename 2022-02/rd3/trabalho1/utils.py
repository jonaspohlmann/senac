NUM_CARACTERES = 30

def clear(): 
    # for windows 
    if name == "nt": 
        _ = system("cls") 
    # for mac and linux(here, os.name is "posix") 
    else: 
        _ = system("clear")

def is_empty(x):
    return x == "" or x == None

def not_is_Empty(x):
    return not(x == "" or x == None)

def return_if_not_empty(x):
    if (not_is_Empty(x)):
        return x

def print_OS(message, char='-'):
    lengthMessage = len(message)
    chars = char*(NUM_CARACTERES-int(lengthMessage/2))
    fullMessage = f'{chars} {message} {chars}'
    if (lengthMessage%2 == 0):
        print(char+fullMessage)
        return char+fullMessage
    else:
        print(fullMessage)
        return fullMessage

def print_menu(menus):
    for menu in menus:
        if (not_is_Empty(menu)):
            print(f'\t[{str(menu[0]).zfill(2)}] - {menu[1].upper()}')