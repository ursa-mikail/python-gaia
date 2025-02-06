import os, sys
import types
import re
from inspect import getmembers, isfunction
import ast

# point to path
lib_path = os.path.abspath('../../Libraries/data/file')
sys.path.append(lib_path)


# import package from path
from file_manager import file_manager	# file name


def top_level_functions(body):
    return (f for f in body if isinstance(f, ast.FunctionDef))

def parse_ast(filename):
    with open(filename, "rt") as file:
        return ast.parse(file.read(), filename=filename)

def list_classes(root_directory):
    class_files = []
    file_extension_to_search_for = '.py'

    # list all python files in Gaia
    for root, dirs, files in os.walk(root_directory):
        for file in files:
            if file.endswith(file_extension_to_search_for):
                print(os.path.join(root, file))

                file_name = os.path.join(root, file)  # start listing the functions
                """
                tree = parse_ast(file_name)
                for func in top_level_functions(tree.body):
                    print("  %s" % func.name)
                """
                file_name = file_name.replace('\\', '/')  # change slash orientation
                class_files.append(file_name)

    return class_files

def list_functions(file_name_with_path):
    functions = []

    functions_to_omit = ['__del__', '__init__', 'who_am_i']
    is_function_to_omit = False

    print("==========================================")

    pattern = re.compile("def (.*)\(")
    for i, line in enumerate(open(file_name_with_path, encoding="utf8")):
        for match in re.finditer(pattern, line):
            for j in range(0, len(functions_to_omit)):
                if functions_to_omit[j] in line:
                    is_function_to_omit = True

            if (not is_function_to_omit):
                print('%s: %s' % (i + 1, match.groups()[0]))  # line number: function name
                functions.append(match.groups()[0])
            else:
                is_function_to_omit = False  # skip once already, check the next

    return functions

def list_imports(file_name_with_path):
    imports = []

    pattern = re.compile("def (.*)\(")
    for i, line in enumerate(open(file_name_with_path, encoding="utf8")): # i := line number
        if ('import ' in line):
            imports.append(line)

    return imports

####################################
## main
####################################
if __name__ == "__main__":
    id_file_manager = "Usage Agent: Internal Agent <file_manager>"
    print("=====[" + id_file_manager + " Start]===== \n")
    file_manager_object = file_manager(id_file_manager)

    # inventory
    number_of_python_files, number_of_functions = 0, 0

    root_directory = 'C:/Users/Smita/PycharmProjects/Ursa/ayahuasca/gaia'
    file_extension_to_search_for = '.py'

    functions_to_omit = ['__del__', '__init__', 'who_am_i']
    is_function_to_omit = False

    # list all python files in Gaia
    for root, dirs, files in os.walk(root_directory):
        for file in files:
            if file.endswith(file_extension_to_search_for):
                print(os.path.join(root, file))

                file_name = os.path.join(root, file)    # start listing the functions
                """
                tree = parse_ast(file_name)
                for func in top_level_functions(tree.body):
                    print("  %s" % func.name)
                """
                file_name = file_name.replace('\\', '/') # change slash orientation
                # file_name = file_name.replace('/', '\\')  # change slash orientation

                number_of_python_files = number_of_python_files + 1

                pattern = re.compile("def (.*)\(")

                for i, line in enumerate(open(file_name, encoding="utf8")):
                    for match in re.finditer(pattern, line):
                        for j in range(0, len(functions_to_omit)):
                            if functions_to_omit[j] in line:
                                is_function_to_omit = True

                        if (not is_function_to_omit):
                            print('%s: %s' % (i + 1, match.groups()[0])) # line number: function name
                            number_of_functions = number_of_functions + 1
                        else:
                            is_function_to_omit = False # skip once already, check the next



    keyword_to_search = 'zip'

    functions_list = [o for o in getmembers(file_manager) if isfunction(o[1])]
    for i in range(0, len(functions_list)):
        if (keyword_to_search in functions_list[i]):
            print ("function with keyword, ", keyword_to_search," : ", functions_list[i])


    print("==================================")
"""
    print("number_of_python_files : ", number_of_python_files)
    print("number_of_functions : ", number_of_functions)

    class_files = list_classes(root_directory)

    for i in range(0, len(class_files)):
        print("class_file ", i, " : ", class_files[i].replace(root_directory, ""))

    file_name_with_path = class_files[15] # 5
    functions = list_functions(file_name_with_path)
    print("\nfile_name_with_path : ", file_name_with_path)
    print("functions : ", functions)

    imports_all = []

    # list all imports within python files in Gaia
    for root, dirs, files in os.walk(root_directory):
        for file in files:
            if file.endswith(file_extension_to_search_for):
                print(os.path.join(root, file))

                file_name = os.path.join(root, file)  # start listing the functions
                
                tree = parse_ast(file_name)
                for func in top_level_functions(tree.body):
                    print("  %s" % func.name)
                
                file_name = file_name.replace('\\', '/')  # change slash orientation
                imports = list_imports(file_name)
                # print ("imports : ", imports)
                imports_all.append(imports)


    #print("import_flat_list: ", imports_all)
    flat_list = [item for sublist in imports_all for item in sublist]
    flat_list_unique = set(flat_list)
    print("import_flat_list: ", flat_list_unique)
    print(len(flat_list), " - ", len(flat_list_unique))
"""