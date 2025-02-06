'''
timing
'''
####################################
import os, sys
import re
from datetime import datetime
from datetime import timedelta

import datetime

# point to path
lib_path = os.path.abspath('../../Libraries/time')
sys.path.append(lib_path)

# import package from path
from timer_0 import timer_0 as timer	# file name
#from timer import timer	# file name

####################################
## main
####################################
if __name__ == "__main__":
    id = "Test Usage Agent: < timer >"
    print ("=====[" + id + " Start]===== \n")
    timer_object = timer(id)
    localtime = timer_object.get_local_time()
    print ("Local current time :", localtime)
    current_moment = timer_object.get_now()
    print ("Timestamp for current moment :",  current_moment)
    print ("================================")

    year_start, month_start, day_start, hour_start, minute_start, secs_start = 2019, 8, 19, 9, 00, 20
    year_end, month_end, day_end, hour_end, minute_end, secs_end = 2019, 8, 21, 9, 00, 20

    log_line = "2018-8-20_09:00:00.648711172 [Info  ] [....]"
    # log_line = "2018-8-20_09:31:00.648711172 [Info  ] [....]"
    log_line = "2018-8-21_09:00:00.648711172 [Info  ] [....]"
    log_line = "2018-8-21_09:00:21.648711172 [Info  ] [....]"

    timer_object.is_between_given_time_and_targeted_log_line(year_start, month_start, day_start, hour_start, minute_start, secs_start,
                                                year_end, month_end, day_end, hour_end, minute_end, secs_end,
                                                log_line)

    hour_start, minute_start, secs_start = 9, 00, 20
    hour_end, minute_end, secs_end = 9, 30, 20

    log_line = "09:00:00.648711172 [Info  ] [....]"
    log_line = "09:31:00.648711172 [Info  ] [....]"

    """
    timer_object.is_between_given_time_within_the_day_and_targeted_log_line(hour_start, minute_start, secs_start,
                                                hour_end, minute_end, secs_end,
                                                log_line)
    """

    """
    log_time = datetime.datetime.strptime(log_line[:log_line.find(".")], "%H:%M:%S").time()

    if start_time <= log_time <= end_time:
        print("The time stated in log: {}".format(log_line), "is within {}".format(start_time),
              " and {}".format(end_time))
    else:
        print("The time stated in log: {}".format(log_line), "is NOT within {}".format(start_time),
              " and {}".format(end_time))

    """

    # sample 1
    timestamp_regex = r'(2[0-3]|[01][0-9]|[0-9]):([0-5][0-9]|[0-9]):([0-5][0-9]|[0-9])'
    target_times = ['01:23:45:', '01:01:45', '01:01:01', '1:1:1', '25:1:1']  # remove empty spaces 1st

    for i in range(0, len(target_times)):
        p = re.compile(timestamp_regex)

        if (bool(re.match(timestamp_regex, target_times[i]))):
            print(target_times[i])
            m = p.search(target_times[i])
            start, end = m.span()
            print(start, ' to ', end)

    # === sample 1 ===
    timestamp_regex = '\d{4}-\d{2}-\d{2}_\d{2}:\d{2}:\d{2}hr'

    target_string = "I have a meeting on 2018-12-15_12:00:00hr in New York"
    match = re.search(timestamp_regex, target_string)
    print(">> ", match.group())
    date = datetime.datetime.strptime(match.group(), '%Y-%m-%d_%H:%M:%Shr')
    print('Time found: ', date)
    print("============================================================")
