#!/bin/sh
# version: 2018-02-03_1802hr_13sec

# dos2unix "./scripts/cipher_utility.sh"
# source "./scripts/cipher_utility.sh" # pack_n_sha() 
# source "./scripts/files_n_folders.sh"
# source "./scripts/data_convert.sh"

function print_menu() {
  echo "Press 1 : generate_templates_for_python_TDD"
  echo "Press 2 : find_functions"
  echo "Press 3 : list_functions"
  echo "Press 4 : update_then_pack_n_sha_Gaia_and_placed_on_desktop"  
  echo "Press 5 : open_Gaia_dir"
  echo "Press 6 : open_PyCharm_dir"
  echo "Press 7 : get_timestamp"
  echo "Press 8 : get passcode"  
  echo "Press 9 : start MongoDB"    
  echo "Press 10 : back_up_Gaia_OS_to_updates_folder"    
  echo "Press 'x' or 'X' to exit the script"
}


function list_functions(){
	print '
	file_type=py
label=class 
find . -regex ".*\.\($file_type\)" -type f -exec awk '/<'$label'>/,/<\/'$label'>/ {print }' {} \; | sed -e 's/<'$label'>/ /g' | sed -e 's/<\/'$label'>/ /g'

	'
	printf "Hello, $USER.\n\n"
	printf "There are "$#" arguments.\n"
	#input_length=20
	#read  -n $input_length -p "Input arguments:" arguments 
	echo ""
	demarcator="===================================================="
	# handle > 10 parameters in shell
	# can have up to ${255}
	# Use curly braces to set them off:
	# echo "${10}"
	printf "\n $demarcator \n"	
	# iterate over the positional parameters
	# for arg
	printf "\n $demarcator \n"			
	# for arg in "$@"
	printf "\n $demarcator \n"			
	#or
	while (( $# > 0 )) # or [ $# -gt 0 ] 
	do 
		echo "$1" 
		shift 
	done
	printf "\n $demarcator \n"	
}

# generate templates at paths stated for TDD on Gaia Framework
function generate_templates_for_python_TDD () {
	# to be completed
	echo "to be completed: generate_templates_for_python_TDD"
	generator_template_path='.\\scripts\\python\\Gaia\\Utilities\\'
	utility_program_name='utility_Gaia_generate_templates.py'
	eval "cd ${generator_template_path}"
	
	python3 "${utility_program_name}"
	
	printf "running: \'${generator_template_path}${utility_program_name}\' \n"
	
	eval "cd -" # return back to previous path
}

function mongoDB_start(){
	echo "mongoDB_start ..."
	destination_path="C:\\\\Program\ Files\\\\MongoDB\\\\Server\\\\3.4\\\\bin" # for SQL: C:\Program Files\MySQL\MySQL Server 5.7\bin
	eval cd ${destination_path}
	eval mongod --auth # with --auth to mandate password for access
	eval "cd -" # return 
}


function open_Gaia_dir () {
	destination_path="C:\Ursa\cygwin\home\Smita\scripts\python\Gaia"
	# eval ". $(HOME)/.bashrc"
	# eval ". ~/.bashrc"
	cd ${destination_path}
	eval "opendir"
}

function open_PyCharm_dir () {
	destination_path="C:\Users\Smita\PycharmProjects"
	# eval ". $(HOME)/.bashrc"
	# eval ". ~/.bashrc"
	cd ${destination_path}
	eval "opendir"
}

function back_up_Gaia_OS_to_updates_folder() {
	destination_path="C:\Users\Smita\Desktop\__New_Updates__\Opus"
	cp -r "./scripts/"  $destination_path
	cp "main.sh" $destination_path
	cp "main_functions.sh" $destination_path
	cp ".bashrc" $destination_path
	destination_path+="/scripts/" # append subfolder
	cp "./scripts/version.txt" $destination_path
	
echo ""
: <<'RECURSIVE_COPY'

	action='cp ' # copy
	
	declare -a backup_targets=("main.sh" "main_functions.sh" "version.txt") ## declare an array variable
	
	number_of_backup_targets=${#backup_targets[@]}
	number_of_backup_targets="$(($number_of_backup_targets-1))"
	# echo $number_of_backup_targets
	
	cp_statements=()
	final_command=""

	for VARIABLE in $(seq 0 1 $number_of_backup_targets)   ## loop through the above array
	do
		# echo $VARIABLE
		cp_statements+=("$action${backup_targets[$VARIABLE]} $destination_path")
	done
	
	#echo $cp_statements
	
	for i in "${cp_statements[@]}"  ## loop through the above array 
	do
		final_command+=$i";" # and append ";"
		#final_command+=$i
	done	
	
	echo $final_command
	#eval $final_command
	#cp -r "./scripts/"  $destination_path
RECURSIVE_COPY
echo ""	
	
	echo "Backup done."
}

function update_then_pack_n_sha_Gaia_and_placed_on_desktop() {
	time_stamp=$(date +"%Y-%m-%d_%H%Mhr_%S"sec)
	echo "Updated: " $time_stamp >> ./scripts/version.txt
	echo -e "\\n" >> ./scripts/version.txt # next line
	back_up_Gaia_OS_to_updates_folder;
	echo "DONE: back_up_Gaia_OS_to_updates_folder"
	
	destination_path="C://Users//Smita//Desktop//__New_Updates__//Opus"
	cd ${destination_path}

	eval "pack_n_sha 'Gaia'"
	echo "DONE: pack_n_sha 'Gaia*'.zip"
	destination_path="C://Users//Smita//Desktop"
	eval "cp Gaia*.zip ${destination_path}"
	eval "rm -rf Gaia*.zip"
}

function count_parameters(){
	printf "Hello, $USER.\n\n"
	printf "There are "$#" arguments.\n"
	#input_length=20
	#read  -n $input_length -p "Input arguments:" arguments 
	echo ""
	demarcator="===================================================="
	# handle > 10 parameters in shell
	# can have up to ${255}
	# Use curly braces to set them off:
	# echo "${10}"
	printf "\n $demarcator \n"	
	# iterate over the positional parameters
	# for arg
	printf "\n $demarcator \n"			
	# for arg in "$@"
	printf "\n $demarcator \n"			
	#or
	while (( $# > 0 )) # or [ $# -gt 0 ] 
	do 
		echo "$1" 
		shift 
	done
	printf "\n $demarcator \n"	
}

function get_passcode(){
	source "./scripts/terminal_setting.sh"
	clr;
	read -p "Enter passcode:" passcode
	printf "Passcode: $passcode \n"
}

function show_timestamp(){
	source "./scripts/time.sh"
	printf "\n"
    get_timestamp;
			
	source "./scripts/data_convert.sh"
	seed="Hi There"
	ans=$(ascii_to_hex "$seed")
	echo $ans
}

function generate_random_bytes (){
	printf "\n"
    # openssl rand -base64 5
	openssl rand -hex 5
}

function make_passcode_with_N_rounds (){
	printf "\n"
	#SALT_FIXED=$(echo '0: FC89BFC2B05F1C2E64B8784392783AC9' | xxd -r)
	# $(openssl rand -base64 24)
	# $(openssl rand -hex 24) # 24 or less hex characters
	prefix="Salted__"
	suffix=""
			
	SALT_FIXED="11111111"
	PASS_FIXED=$(echo "111111111111111" | xxd -p)
	# printf "$s\n" "$SALT_FIXED"
	#echo $SALT_FIXED 
	#SALT=$(echo SALT_FIXED | xxd -p) # to hex
	SALT=$SALT_FIXED
	#echo $SALT
	#echo $PASS_FIXED
	
	source "./scripts/data_convert.sh"
	#read -p "Enter seed string:" seed
	seed="Hi There"
	# $1=$seed (with spaces)
	#seed_hex=$(ascii_to_hex "$seed")	# use double quote to get string with spaces as 1 argument
	#len=$(echo $seed_hex | wc -c)
	#seed_hex=${seed_hex:0:(len-1)} # remove last character
	seed_hex=$(echo -n "$seed" | xxd -p) 
	echo $seed_hex
	
	
	read -p "Enter N:" N
	#N=3
	# 7eb48561
				
	for VARIABLE in $(seq 1 1 $N)
	do 
		#printf "Round: %d \n" "$VARIABLE"
		ANS=$(echo -n $seed_hex | xxd -p -r | openssl enc -aes-256-cbc -S $SALT -k $PASS_FIXED)
		# truncate prefix="Salted__"
		# echo "$string" | sed -e "s/^$prefix//" -e "s/$suffix$//"
		ANS_FINAL=$(echo $ANS | sed -e "s/^$prefix//" -e "s/$suffix$//")
		ANS_FINAL=$(echo $ANS_FINAL | xxd -p)	
		#printf "\n[%d] untruncated salt: %s\n" "$VARIABLE" "$ANS_FINAL"
		SALT=${ANS_FINAL: -10} # renew SALT last 5 bytes only
		SALT=${SALT:0:8} # remove last byte
		#echo ${ANS_FINAL:0:8} # get 1st 4 bytes
			#echo ${ANS_FINAL: -8} # get last 4 bytes
			#printf "\nSALT:" echo $SALT		
			#printf "\nPASS_FIXED:" echo $PASS_FIXED	
		done			
	
		#echo $SALT
		printf "\npasscode: %s\n" "$SALT"
}
function get_bash_version () {
	source "./scripts/terminal_setting.sh"
	clr;
	N=10
		
	for VARIABLE in 1 2 3 4 5 .. N
	do
		printf "\n"
	done
	echo "Bash version ${BASH_VERSION}..."
	
	echo "Home path: $HOME"
}

function make_passcode (){
	printf "\n"
	SALT_FIXED=$(echo '0: FC89BFC2B05F1C2E64B8784392783AC9' | xxd -r)
	# $(openssl rand -base64 24)
	# $(openssl rand -hex 24) # 24 or less hex characters
	PASS_FIXED="uh.oh.hotdog"
	# printf "$s\n" "$SALT_FIXED"
	echo $SALT_FIXED
	# openssl enc -base64 -aes-256-cbc -S $SALT_FIXED -k $PASS_FIXED
	#openssl enc -aes-256-cbc -S $SALT_FIXED -k $PASS_FIXED
	ANS=$(echo "test" | openssl enc -aes-256-cbc -S 00000000 -k 00000000000000000000000000000000)
	# truncate prefix="Salted__"
	# echo "$string" | sed -e "s/^$prefix//" -e "s/$suffix$//"
	prefix="Salted__"
	suffix=""
	ANS_FINAL=$(echo "$ANS" | sed -e "s/^$prefix//" -e "s/$suffix$//")
	echo $ANS_FINAL | xxd -p
}



function google_search_usual() {
	chrome_exe_location="'/cygdrive/c/Program Files (x86)/Google/Chrome/Application/chrome.exe' " # space is required after calling the executable
	
	action='"https://www.google.com/search?q='
	
echo ""
: <<'COMMENT_NON_LOOP_SEARCH_APPEND'
	keyphase00='north+korea"'
	keyphase01='hurricane+texas+houston"'
	search00="${chrome_exe_location}$action$keyphase00"
	search01="${chrome_exe_location}$action$keyphase01"

	final_command=$search00";"$search01
COMMENT_NON_LOOP_SEARCH_APPEND
echo ""
	declare -a keyphases=('recession' 'ebay stock price' 'north+korea') ## declare an array variable
	
	number_of_keyphases=${#keyphases[@]}
	number_of_keyphases="$(($number_of_keyphases-1))"
	# echo $number_of_keyphases
	
	search_urls=()
	final_command=""

	for VARIABLE in $(seq 0 1 $number_of_keyphases)   ## loop through the above array
	do
		# echo $VARIABLE
		search_urls+=("${chrome_exe_location}$action${keyphases[$VARIABLE]}"'";')
		#echo ${keyphases[$VARIABLE]}'"'
		#echo ${search_urls[$VARIABLE]}
	done
	
	#echo $search_urls
	
	for i in "${search_urls[@]}"  ## loop through the above array 
	do
		#final_command+=$i";" # and append ";"
		final_command+=$i
	done	
	
	eval $final_command

	option_on_of=0
	
	if [ $option_on_of -eq 1 ];
	then
		final_command="" # reset for reuse
		declare -a sites=('https://www.worldtimebuddy.com/?pl=1&lid=5392171,1880252&h=5392171')
		number_of_sites=${#sites[@]}
		
		for VARIABLE in $(seq 0 1 $number_of_sites)   ## loop through the above array
		do
			# echo $VARIABLE
			sites_urls+=("${chrome_exe_location}${sites[$VARIABLE]}"'";')
		done
		
		for i in "${sites_urls[@]}"  ## loop through the above array 
		do
			#final_command+=$i";" # and append ";"
			final_command+=$i
		done	
		
		eval $final_command
	else
		echo "Common site off"
	
	fi
	
	#example: '/cygdrive/c/Program Files (x86)/Google/Chrome/Application/chrome.exe' "https://www.google.com/search?q=hurricane+texas+houston"

}


function exit_program() {
	printf "\n quit.\n"
	echo 'X' : quitprogram
}

function default_action() {
    echo "You have entered an invallid selection!"
    echo "Please try again!"
    echo ""
    echo "Press any key to continue..."
    read -n 1
    clear
	set -u # force it to treat unset variables as an error 
	unset main_menu_input
	#echo $mainmenuinput 
    main
}