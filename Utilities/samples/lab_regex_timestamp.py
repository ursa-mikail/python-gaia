from os import listdir
from os.path import isfile, join

import re

def get_year_month_day_hour_min_sec(string_with_timestamp_formatted, location_of_timestamp):
    start_position, end_position = location_of_timestamp[0], location_of_timestamp[1]
    next_position = start_position
    year = string_with_timestamp_formatted[next_position:next_position+4]
    next_position = next_position + 5
    month = string_with_timestamp_formatted[next_position:next_position+2]
    next_position = next_position + 3
    day = string_with_timestamp_formatted[next_position:next_position+2]
    next_position = next_position + 3
    hour = string_with_timestamp_formatted[next_position:next_position+2]
    next_position = next_position + 2
    min = string_with_timestamp_formatted[next_position:next_position+2]
    next_position = next_position + 5
    sec = string_with_timestamp_formatted[next_position:next_position+2]

    return [year, month, day, hour, min, sec]

# field_list, e.g. [year, month, day, hour, min, sec]
# lengths_of_fields, e.g. [4, 2, 2, 2, 2, 2]
# offsets, e.g. [start_position, 1, 1, 0, 3, 0]
def extract_text_given_offsets(target_string, lengths_of_fields, offsets):
    # assert (len(field_list) != len(lengths_of_fields), "length of field_list and lengths_of_fields must be equal")
    assert len(lengths_of_fields) == len(offsets), "length of lengths_of_fields and offsets must be equal"
    field_list = []

    # next_position = start_position # offsets[0]
    next_position = 0

    for i in range(0, len(lengths_of_fields)):
        next_position = next_position + offsets[i]
        field_list.append(target_string[next_position:next_position+lengths_of_fields[i]])
        next_position = next_position + lengths_of_fields[i]

    return field_list

timestamp = " xxx 2014-10-15_0000hr_33sec xxx" #
regex_year_range = r'[0-2][0-2][0-9][0-9]'
regex_month_range = r'[0-1][0-9]'
regex_day_range = r'[0-3][0-9]'
regex_hr_and_min_of_the_day_range = r'[0-2][0-9][0-5][0-9]'
regex_sec_of_the_day_range = r'[0-5][0-9]'
regex_delimiter = r'[-._]'

found_status = re.search(regex_year_range + regex_delimiter + regex_month_range + regex_delimiter + regex_day_range \
                            + regex_delimiter + regex_hr_and_min_of_the_day_range + 'hr' + regex_delimiter + regex_sec_of_the_day_range \
                            + 'sec', timestamp)
if found_status:
    print ("timestamp : ", timestamp, " at ", found_status.span())
else:
    print ("Not found")

num = re.sub(r'#.*$', "", timestamp)
print ("timestamp : ", num)

# Remove anything other than digits
replace_with = ''
replace_with = '[]'
num = re.sub(r'\D', replace_with, timestamp)
print ("timestamp : ", num)


s = "These are oranges and apples and pears, but not pinapples or .."
r = re.compile(r'\bAND\b | \bOR\b | \bNOT\b | \bBUT\b', flags=re.I | re.X)
answer = r.findall(s)
print(answer)

path_to_logs = './data/logs_event/'
files_only = [f for f in listdir(path_to_logs) if isfile(join(path_to_logs, f))]
# files_only = sorted(files_only, reverse=True)
files_only = sorted(files_only)
print("files_only: ", files_only)

for i in range(0, len(files_only)):
    found_status = re.search(regex_year_range + regex_delimiter + regex_month_range + regex_delimiter + regex_day_range \
                             + regex_delimiter + regex_hr_and_min_of_the_day_range + 'hr' + regex_delimiter + regex_sec_of_the_day_range \
                             + 'sec', files_only[i])
    if found_status:
        print("timestamp : ", files_only[i], " at ", found_status.span())
        #[year, month, day, hour, min, sec] = get_year_month_day_hour_min_sec(files_only[i], found_status.span())

        target_string = files_only[i]
        start_position = found_status.span()
        lengths_of_fields = [4, 2, 2, 2, 2, 2]
        offsets = [start_position[0], 1, 1, 1, 0, 3] # 2018[-]04[-]24[_]1912[hr_]20sec
        field_list = extract_text_given_offsets(target_string, lengths_of_fields, offsets)
        [year, month, day, hour, min, sec] = field_list
        print("year, month, day, hour, min, sec = %s %s %s %s %s %s " % (year, month, day, hour, min, sec))

    else:
        print("Not found : ", files_only[i])

