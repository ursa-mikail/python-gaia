#!/bin/sh
# version: 2018-02-03_1802hr_13sec
dos2unix "./ayahuasca_main_functions.sh"
source "./ayahuasca_main_functions.sh"

# source_utility_executable_dir="./scripts/python/Gaia/Utilities/"
# source_utility_executable="utility_lib.py"
# chmod +x $source_utility_executable_dir$source_utility_executable

# MAIN
ayahuasca_main () {
	print_menu;
	number_of_digits_for_inputs=2
	read  -n $number_of_digits_for_inputs  -p "Input Selection:" main_menu_input
  
	if [ "$main_menu_input" = "1" ]; then
		#cd $source_utility_executable_dir
		#clear; python3 $source_utility_executable
		#printf "Returning to path : "
		#cd -
		echo "yet to be done"
    elif [ "$main_menu_input" = "2" ]; then
		list_functions $1 # clr; py3 utility_lib.py;
    elif [ "$main_menu_input" = "3" ]; then
		clr; py3 utility_lib.py;
    elif [ "$main_menu_input" = "4" ]; then
		clr; py3 utility_lib.py;           
    elif [ "$main_menu_input" = "5" ]; then
		clr; py3 utility_lib.py;
    elif [ "$main_menu_input" = "6" ];then
		clr; py3 utility_lib.py;
    elif [ "$main_menu_input" = "7" ];then
		clr; py3 utility_lib.py;		
    elif [ "$main_menu_input" = "x" -o "$main_menu_input" = "X" ];then # -o := `or` and `||`
		exit_program;
    else
		default_action;
    fi
}

# This builds the main menu and routs the user to the function selected.
ayahuasca_main # This executes the main menu function.

echo ""
: <<'COMMENT_GENERATE_PASS'


COMMENT_GENERATE_PASS
echo ""
