
file_target = './data/notes.txt'

ON, OFF = True, False
tag_start, tag_end = 'openssl', '2048'
# tag_start, tag_end = '[START]', '[STOP]'
tag_start_index, tag_end_index = 0, 0 # start when tag index count when detected
search_tag_start, search_tag_end, start_recording = ON, OFF, OFF
line_start, line_stop = 0, 0

recorded_lines = []
recorded_lines_list = []
recorded_lines_line_numbers = []
start_stop_line_indices = ()

with open(file_target) as f:
    content = f.readlines()

# remove whitespace characters like `\n` at the end of each line
# content = [x.strip() for x in content]
line_number_total = len(content)

print(content)

for line_index in range(0, line_number_total):                  # scan each line
    line_target = content[line_index]
    character_number_total = len(line_target)
    # print(line_target)
    for character_index in range(0, character_number_total):    # scan each character
        if (search_tag_end == OFF) and (search_tag_start == ON):
            if (line_target[character_index] == tag_start[tag_start_index]):
                search_tag_end = OFF
                search_tag_start = ON
                tag_start_index = tag_start_index + 1

                if (tag_start_index == len(tag_start)):
                    start_recording = ON
                    line_start = line_index
                    # start_stop_line_indices[0] = line_start
                    tag_start_index = 0
                    search_tag_start = OFF
                    search_tag_end = ON
                    character_index = character_index + 1 # skip immediately after the tag

            else:       # Caveat: Nested tags that are the same
                tag_start_index = 0
                search_tag_end = OFF

        if (search_tag_start == OFF) and (search_tag_end == ON):
            if (line_target[character_index] == tag_end[tag_end_index]):
                search_tag_start = OFF
                search_tag_end = ON
                tag_end_index = tag_end_index + 1

                if (tag_end_index == len(tag_end)):
                    start_recording = OFF
                    line_stop = line_index  # Caveat: record line_start, line_stop and reset values
                    #start_stop_line_indices[1] = line_stop
                    start_stop_line_indices = (line_start, line_stop)
                    tag_end_index = 0
                    search_tag_start = ON
                    search_tag_end = OFF

            else:
                tag_end_index = 0

        if (start_recording == ON):
            # print(line_target[character_index], end='')
            recorded_lines.append(line_target[character_index])

        if (start_recording == OFF):
            recorded_lines = ''.join(recorded_lines)
            recorded_lines =  recorded_lines[0:(len(recorded_lines) - len(tag_end) + 1)] # remove the tag_end
            if (len(recorded_lines) != 0):
                recorded_lines_list.append(recorded_lines)
                recorded_lines_line_numbers.append(start_stop_line_indices)

            recorded_lines = [] # clear buffer
            start_stop_line_indices = ()

    # when it is end of file, clear all buffers
    """
    tag_start_index, tag_end_index = 0, 0 # start when tag index count when detected
    search_tag_start, search_tag_end, start_recording = ON, OFF, OFF
    line_start, line_stop = 0, 0

    recorded_lines = []
    recorded_lines_list = []
    recorded_lines_line_numbers = []
    start_stop_line_indices = ()
    """

print(recorded_lines_list)
print(recorded_lines_line_numbers)

number_of_instances = len(recorded_lines_list)

for i in range(0, number_of_instances):
    line_indices = recorded_lines_line_numbers[i]
    line_number_start, line_number_end = line_indices[0] + 1, line_indices[1] + 1
    print("Line: ", line_number_start, " to Line: ", line_number_end)
    print(recorded_lines_list[i])
