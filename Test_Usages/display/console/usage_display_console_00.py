import os, sys

# point to path
lib_path = os.path.abspath('../../../Libraries/display/console')
sys.path.append(lib_path)

# import package from path
from display_console import display_console

# ensure every menu entry is unique.
def menu_display_and_get_choice (items, question): # list of all menu entries, and question it will ask when all options have been printed
    valid_choice = False
    chars = set('0123456789,')

    display_menu(items)

    while (valid_choice == False):
        option_chosen = str(input(question))

        if any((c in chars) for c in option_chosen):
            print('Numbers Found')
            valid_choice = True
            option_chosen = int(option_chosen) - 1
        else:
            print('Numbers Not Found')

    return option_chosen

def display_menu(items):
    print("In the room you can see", len(items), "things:")
    for entry in items:
        print (1 + items.index(entry), end=""),
        print (") " + entry)

    return None

def inspect_choice (choice, keylocation, items):
    loop, keyfound = True, False

    for i in range(0, len(items)):
        if choice >= len(items):
            print("Unavailable Option.")
            break

        if choice == i:
            if choice == keylocation:
                print("You found a small key in the ", items[i])
                keyfound = True
            else:
                print("You found nothing in the ", items[i])

    if keyfound == True:
        loop = False
        print("You put in the key, turn it, and hear a click")
    else:
        print("The door is locked, you need to find a key.")

    return loop


####################################
## main
####################################
if __name__ == "__main__":
    id_display_console = "Test Usage Agent: <display_console>"
    print ("=====[" + id_display_console + " Start]===== \n")
    display_console_object = display_console(id_display_console)

    items = ["pot plant", "painting", "vase", "lampshade", "shoe", "door"]  # basic info about the room:
    keylocation = 2  # key is in entry number 2 in the list above
    loop = True

    # Get menu working, and the program running until you find the key:
    while loop == True:
        choice = menu_display_and_get_choice (items, "What do you want to inspect? ")
        loop = inspect_choice(choice, keylocation, items)

    print("Got it.")

    print("*** END ***")

"""
# version: 2018-04-07_1429hr_07sec
"""