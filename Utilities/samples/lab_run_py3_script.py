import sys, getopt

def main(argv):
    inputfile =''
    outputfile =''

    python_filename_current = sys.argv[0]
    usage_advice = ''.join('Usage: \n' + \
                            'py3 ' + python_filename_current + ' -i | --i <inputfile> -o | --o <outputfile> \n' + \
                            'py3 ' + python_filename_current + ' -h | --h')

    print('Number of arguments:', len(sys.argv), 'arguments.')
    print('Argument List:', str(sys.argv))

    try: #
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=", "ofile="])
    except getopt.GetoptError: # raised when an unrecognized option is found in the argument list or when an option requiring an argument is given none.
        print (usage_advice)
        sys.exit(2)

    for opt, arg in opts:
        if opt =='-h':
            print(usage_advice)
            sys.exit()
        elif opt in("-i", "--ifile"):
            inputfile = arg
        elif opt in("-o", "--ofile"):
            outputfile = arg


    print('Input file :', inputfile)
    print('Output file :', outputfile)

    return None

if __name__ =="__main__":
    main(sys.argv[1:])

"""
getopt parse command-line options and arguments.
$ python test.py arg1 arg2 arg3

getopt.getopt(args, options[, long_options])
•	args: argument list to be parsed.
•	options: string of option letters that the script wants to recognize, with options that require an argument should be followed by a colon (:).
•	long_options: optional parameter and if specified, must be a list of strings with the names of long options, which should be supported. Long options, which require an argument should be followed by an equal sign ('='). To accept only long options, options should be an empty string.
method returns value consisting of 2 elements: 1st is a list of (option, value) pairs. 2nd is the list of program arguments left after the option list was stripped.
Each option-and-value pair returned has the option as its first element, prefixed with a hyphen for short options (e.g., '-x') or 2 hyphens for long options (e.g., '--long-option').


 $ chmod +x lab_10.py     # This is to make file executable
 
 in bash:
alias return_to_previous="cd ~"
path_to_script='C:\\Users\\Smita\\PycharmProjects\\Neria\\trial\\'
# alias run_00="clr; py3 $path_to_script''lab_run_py3_script.py"
# alias run_00="clr; cd $path_to_script; py3 lab_run_py3_script.py "$@";return_to_previous;"

# function run_00() {
run_01()
 {
	args=("$@")

	echo Number of arguments: $#
	echo 1st argument: ${args[0]}
	echo 2nd argument: ${args[1]}
	clr; 
	cd $path_to_script; # go to dir where script is
	py3 lab_run_py3_script.py $@;
	return_to_previous; # return to origin dir
 }

"""