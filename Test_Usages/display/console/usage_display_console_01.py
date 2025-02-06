import os, sys
import string

# point to path
lib_path = os.path.abspath('../../../Libraries/display/console')
sys.path.append(lib_path)
lib_path = os.path.abspath('../../../Libraries/time')
sys.path.append(lib_path)

# import package from path
from display_console import display_console
from timer_0 import timer_0 as timer	# file name
# from timer import timer	# file name

# ensure every menu entry is unique.
def menu_display_and_get_choice (items, question): # list of all menu entries, and question it will ask when all options have been printed
    valid_choice = False
    chars_valid = set('0123456789Xx,')
    chars_invalid = set('`~!@#$%^&*()_+-=$:;"\'?><./\\|,{}[]<>' + string.ascii_lowercase[:26] + string.ascii_uppercase[:26])

    display_menu(items)

    while (valid_choice == False):
        option_chosen = str(input(question))

        if any((c in chars_invalid) for c in option_chosen):
            print('Symbol characters Found')
        else:
            print('Symbol characters Not Found')
            valid_choice = True

        if any((c in chars_valid) for c in option_chosen):
            print('Options range Valid')
            valid_choice = True
        else:
            print('Options range InValid')

    return option_chosen

def display_menu(items):
    print("Menu: ", len(items), " items:")
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
                print("You found a key in the ", items[i])
                keyfound = True
            else:
                print("You found nothing in the ", items[i])

    if keyfound == True:
        loop = False
        print("You put in the key, turn it, and hear a click")
    else:
        print("The door is locked, you need to find a key.")

    return loop

def get_variable_name_for_display(obj, namespace):
    resultant = [name for name in namespace if namespace[name] is obj]
    return resultant[0]

def display_variable_name_and_value(variable):
    print(get_variable_name_for_display(variable, globals()), ' : ', variable)

    return None

####################################
## main
####################################
if __name__ == "__main__":
    id_display_console = "Test Usage Agent: <display_console>"
    print ("=====[" + id_display_console + " Start]===== \n")
    display_console_object = display_console(id_display_console)


    status = 'Can You Read This Status?'
    display_console_object.display_variable_name_and_value(globals(), status)
    display_variable_name_and_value(status)

    items = ["Get time stamp", "painting", "vase", "lampshade", "shoe", "[X, x] Exit"]  #
    loop = True

    #choice = menu_display_and_get_choice (items, "What do you want to inspect? ")
    #loop = inspect_choice(choice, keylocation, items)

    """
    switch(user_input):
    	case 0:
    		print user_input, " :0";
    		break;
    	case 1:
    		print user_input, " :1";
    		break;
    	case 2:
    		print user_input, " :2";
    		break;
    	case 3:
    		print user_input, " :3";
    		break;
    	case 4:
    		print user_input, " :4";
    		break;	
    	case 5:
    		print user_input, " :5";
    		break;
    	case 6:
    		print user_input, " :6";
    		break;  		
    	case 7:
    		print user_input, " :7";
    		break;
    	case 8:
    		print user_input, " :8";
    		break;
    	case 9:
    		print user_input, " :9";
    		break;  
    	case 10:
    		print user_input, " :10";
    		break;  		
    	case 11:
    		print user_input, " :11";
    		break;  	
    	default:
    		print "Only numbers are allowed\n";
    		break;
    """


    def _0():
        print(user_input, " :0")

    def _1():
        print(user_input, " :1")

    def _2():
        print(user_input, " :2")

    def _3():
        print(user_input, " :3")

    def _4():
        print(user_input, " :4")

    def _5():
        print(user_input, " :5")

    def _6():
        print(user_input, " :6")

    def _7():
        print(user_input, " :7")

    def _8():
        print(user_input, " :8")

    def _9():
        print(user_input, " :9")

    def _10():
        print(user_input, " :10")

    def _11():
        print (user_input, " :11")


    options = {
        0: _0,
        1: _1,
        2: _2,
        3: _3,
        4: _4,
        5: _5,
        6: _6,
        7: _7,
        8: _8,
        9: _9,
        10: _10,
        11: _11,
    }

    ### main
    id_timer = "Test Usage Agent: < timer >"
    print("=====[" + id_timer + " Start]===== \n")
    timer_object = timer(id_timer)
    print("\ntimestamp: " + timer_object.get_timestamp())

    user_input = menu_display_and_get_choice(items, "Enter choice: ")
    if (user_input.lower() == 'x'):
        print("*** MENU EXIT ***")
        exit()

    # switch
    options[int(user_input)]()

    print("*** END ***")

"""
# version: 2018-04-07_1548hr_03sec
"""