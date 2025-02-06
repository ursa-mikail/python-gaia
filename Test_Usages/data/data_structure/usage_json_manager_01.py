####################################
import os, sys

# point to path
lib_path = os.path.abspath('../../../Libraries/data/data_structure')
sys.path.append(lib_path)
lib_path = os.path.abspath('../../../Libraries/text')
sys.path.append(lib_path)

# import package from path
from json_manager import json_manager	# file name
from string_processor import string_processor_class	# file name
# from text_processor import text_processor	# file name

import json
####################################
## main
####################################
if __name__ == "__main__":
    id = "Library Agent: Internal Agent <json_manager>"
    print("=====[" + id + " Start]===== \n")
    json_manager_object = json_manager(id)
    json_manager_object.who_am_i()

    chart = {   "emotions":
             {
                "anger":
                    {
                        "hurt": ["embarrassed", "devastated"],
                        "threatened": ["insecure", "jealous"],
                        "hateful": ["violated", "resentful"],
                        "mad": ["furious", "enraged"],
                        "aggressive": ["provoked", "hostile"],
                        "frustrated": ["infuriated", "irritated"],
                        "distant": ["withdrawn", "suspicious"],
                        "critical": ["skeptical", "sarcastic"]
                    },
                 "disgust":
                     {
                         "disapproval": ["judgmental", "loathing"],
                         "disappointed": ["repugnant", "revolted"],
                         "awful": ["revulsion", "detestable"],
                         "avoidance": ["aversion", "hesitant"]
                     },
                 "sad":
                     {
                         "guilty": ["remorseful", "ashamed"],
                         "abandoned": ["ignored", "victimized"],
                         "despair": ["powerless", "vulnerable"],
                         "depressed": ["inferior", "empty"],
                         "lonely": ["abandoned", "isolated"],
                         "bored": ["apathetic", "indifferent"]
                     },
                 "happy":
                     {
                         "optimistic": ["inspired", "open"],
                         "intimate": ["playful", "sensitive"],
                         "peaceful": ["hopeful", "loving"],
                         "powerful": ["provocative", "courageous"],
                         "accepted": ["fulfilled", "respected"],
                         "proud": ["confident", "important"],
                         "interested": ["inquisitive", "amused"],
                         "joyful": ["ecstatic", "liberated"]
                     },
                 "surprised":
                     {
                         "excited": ["energetic", "eager"],
                         "amazed": ["awe", "astonished"],
                         "confused": ["perplexed", "disillusioned"],
                         "startled": ["dismayed", "shocked"]
                     },
                 "fear":
                     {
                         "scared": ["terrified", "frightened"],
                         "anxious": ["overwhelmed", "worried"],
                         "insecure": ["inadequate", "inferior"],
                         "submissive": ["worthless", "insignificant"],
                         "rejected": ["inadequate", "alienated"],
                         "humiliated": ["disrespected", "ridiculed"]
                     }
             }
        }

    chart = {
            "glossary": {
                "title": "example glossary",    # level 1
		        "GlossDiv": {
                    "title": "S",               # level 2
			        "GlossList": {
                        "GlossEntry": {
                            "ID": "SGML",
					        "SortAs": "SGML",
					        "GlossTerm": "Standard Generalized Markup Language",
					        "Acronym": "SGML",
					        "Abbrev": "ISO 8879:1986",
					        "GlossDef": {
                                "para": "A meta-markup language, used to create markup languages such as DocBook.",
						        "GlossSeeAlso": ["GML", "XML"]
                                        },
					        "GlossSee": "markup"
                                        }
                                    }
                                }
                            }
            }

    json_indented = json.dumps(chart, indent=4)
    contents_formatted_json_stream = json_manager_object.check_json_format_with_json_stream(json_indented)
    print('contents_formatted_json_stream: ', contents_formatted_json_stream)

    depth_max = json_manager_object.get_max_depth_of_json_file_structure(json_indented)
    print('depth_max: ', depth_max)

    depth_max = json_manager_object.get_depth(chart)
    print('depth_max: ', depth_max)

    layer_number_index = 4
    contents = json_manager_object.extract_json_content_at_N_layer(json_indented, layer_number_index) #

    # print("At level ", layer_number_index, " : ", contents, "\nLength of contents: ", len(contents))

    layer_number_index = 7
    if(json_manager_object.level_exist(json_indented, layer_number_index)):
        print("Level ", layer_number_index, " exists")
    else:
        print("Level ", layer_number_index, " exist NOT")

    number_of_keys = json_manager_object.count_number_of_keys_in_json_stream(contents)
    print('number_of_keys: ', number_of_keys)

    print(type(contents))
    contents = " ".join(contents.split("\n")) # replace newline with space
    # contents = " ".join(contents.split("\t"))  # replace tab with space
    contents = " ".join(contents.split("    "))  # replace tab with space
    keys_in_contents_serialized_string, values_in_contents_serialized_string = json_manager_object.get_keys_only_in_json_stream(contents)
    print('keys_in_contents_serialized_string: ', keys_in_contents_serialized_string)
    print('values_in_contents_serialized_string: ', values_in_contents_serialized_string)

    for i in range(0, len(values_in_contents_serialized_string)):
        print("terms: ", values_in_contents_serialized_string[i])

    print("There are ", len(values_in_contents_serialized_string), " terms")
    #contents = json_manager_object.extract_json_content_under_N_layer(json_indented, layer_number_index)
    #print("Under level ", layer_number_index, " : ", contents)

    print("=====[" + id + " End]===== \n");

    """
    print(chart.keys())

    for key in chart.keys():
        if isinstance(chart[key], dict) == False:
            print(key, chart[key])
    """

"""
# version: 2017-11-25_2350hr_20sec
"""