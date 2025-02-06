'''

'''
import time
import calendar
import datetime

from datetime import datetime
from datetime import timedelta

import math

####################################
class timer_0:
    """ timing operations """
    id = ""
    inventory = {}
    inventory_id = ""
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    def __init__(self, id):
        self.id = id;
        self.start_time = 0;
        self.end_time = 0;
        self.time_elapsed = 0;
        self.pause_time_start = 0;
        self.pause_time_end = 0;
        self.pause_time_delta_list = [];
        self.pause_on = False;
        print ("timer object [%s] is born\n" % self.id)

    def timer_start(self):
        self.start_time = time.time()
        return self.start_time;

    def timer_stop(self):
        if (self.pause_on == True):
            self.pause_on = False; # off pause
            self.pause_time_end = time.time();
            pause_delay = self.pause_time_end - self.pause_time_start;
            self.pause_time_delta_list.append(pause_delay);
            self.pause_time_start = 0; # clear after use
            self.pause_time_end = 0; # clear after use

        total_number_of_pauses_occurred = len(self.pause_time_delta_list);

        for x in xrange(0, total_number_of_pauses_occurred):   #
            self.start_time = self.start_time + self.pause_time_delta_list[0]; # bring the start time forward to offset the pause
            self.pause_time_delta_list.remove(self.pause_time_delta_list[0]); # remove front element

        self.end_time = time.time()
        return self.end_time;

    def timer_continue(self):
        if (self.pause_on == True):
            self.pause_on = False; # off pause
            self.pause_time_end = time.time();
            pause_delay = self.pause_time_end - self.pause_time_start;
            self.pause_time_delta_list.append(pause_delay);
            self.pause_time_start = 0; # clear after use
            self.pause_time_end = 0; # clear after use

        total_number_of_pauses_occurred = len(self.pause_time_delta_list);

        for x in range(0, total_number_of_pauses_occurred):   #
            self.start_time = self.start_time + self.pause_time_delta_list[0]; # bring the start time forward to offset the pause
            self.pause_time_delta_list.remove(self.pause_time_delta_list[0]); # remove front element

        self.end_time = time.time()
        return self.end_time;

    def timer_pause(self):
        if (self.pause_on == False): # correct for multiply pauses
            self.pause_time_start = time.time()
            self.pause_on = True;

    def timer_clear(self):
        self.start_time = 0;
        self.end_time = 0;
        self.time_elapsed = 0;

    def get_time_elapsed(self):
        self.time_elapsed = self.end_time - self.start_time;
        return self.time_elapsed;

    def sleep(self, countdown_secs):
        time.sleep(countdown_secs);


    """
    DATE
    Dates in the far future cannot be represented this way - the cutoff point is sometime in 2038 for UNIX and Windows.
    """

    def get_time_instance_reference_in_seconds(self, year, month, day, hour = 0, min = 0, sec = 0):
        time_reference = datetime(year, month, day, hour, min, sec)
        time_instance_reference_in_seconds = time_reference.timestamp()

        '''
        Python datetime object to seconds
        (t-datetime.datetime(1970,1,1)).total_seconds()
        1256083200.0

        from datetime import datetime
        dt = datetime.today()  # Get timezone naive now
        seconds = dt.timestamp()

        # Unix time
        import datetime, time
        t = datetime.datetime(2011, 10, 21, 0, 0)
        time.mktime(t.timetuple())
        '''

        return time_instance_reference_in_seconds

    def get_earlier_time (self, time_00, time_01):
        time_instance_reference_in_seconds_00 = self.get_time_instance_reference_in_seconds(time_00.year, time_00.month, time_00.day, time_00.hour, time_00.minute, time_00.second)
        time_instance_reference_in_seconds_01 = self.get_time_instance_reference_in_seconds(time_01.year, time_01.month, time_01.day, time_01.hour, time_01.minute, time_01.second)

        if (time_instance_reference_in_seconds_00 < time_instance_reference_in_seconds_01):
            earlier_time = time_00
        else:
            earlier_time = time_01

        return earlier_time

    def get_later_time (self, time_00, time_01):
        earlier_time = self.get_earlier_time(time_00, time_01)
        if (earlier_time == time_00):
            later_time = time_01
        else:
            later_time = time_00

        return later_time

    def get_local_time(self):
        localtime = time.asctime( time.localtime(time.time()) )
        localtime_struct = time.localtime(time.time());
        self.now_year = localtime_struct.tm_year;
        self.now_month = localtime_struct.tm_mon;
        self.now_day_of_month = localtime_struct.tm_mday;
        self.now_hour_of_day = localtime_struct.tm_hour;
        self.now_minute_of_day = localtime_struct.tm_min;
        self.now_sec_of_minute = localtime_struct.tm_sec; # (60 or 61 are leap-seconds)

        self.now_day_of_week = self.days_of_week[localtime_struct.tm_wday];
        # print ">>", self.now_day_of_week
        self.now_day_of_year = localtime_struct.tm_yday # Julian day
        self.now_daylight_savings = localtime_struct.tm_isdst # -1 (means library determines DST), 0, 1
        return localtime;

    def get_now(self): # more precise with microseconds
        #print "microseconds:", datetime.timedelta(microseconds=1)
        #now = datetime.datetime.now().time()
        #print now
        self.now = datetime.now()
        self.now_year = self.now.year
        self.now_month = self.now.month
        self.now_day_of_month = self.now.day
        self.now_day_of_week_enum = self.now.weekday()
        self.now_day_of_week = self.days_of_week[self.now_day_of_week_enum]; # +1 =  self.now.isoweekday()
        self.now_hour_of_day = self.now.hour
        self.now_minute_of_hour = self.now.minute
        self.now_sec_of_minute = self.now.second
        self.now_msec_of_sec = self.now.microsecond

        return self.now;

    def is_between_given_time_and_targeted_log_line(self, year_start, month_start, day_start, hour_start, minute_start, secs_start,
                                                        year_end, month_end, day_end, hour_end, minute_end, secs_end,
                                                        log_line):
        start_time = datetime(year_start, month_start, day_start, hour_start, minute_start, secs_start)
        end_time = datetime(year_end, month_end, day_end, hour_end, minute_end, secs_end)

        log_time = datetime.strptime(log_line[:log_line.find(".")], "%Y-%m-%d_%H:%M:%S")

        if start_time <= log_time <= end_time:
            print("The time stated in log: {}".format(log_line), "is within {}".format(start_time),
                " and {}".format(end_time))
        else:
            print("The time stated in log: {}".format(log_line), "is NOT within {}".format(start_time),
                " and {}".format(end_time))


    """
    def is_between_given_time_within_the_day_and_targeted_log_line(self, hour_start, minute_start, secs_start,
                                                        hour_end, minute_end, secs_end,
                                                        log_line):
        start_time = datetime.time(hour_start, minute_start, secs_start)
        end_time = datetime.time(hour_end, minute_end, secs_end)

        log_time = datetime.strptime(log_line[:log_line.find(".")], "%H:%M:%S").time()

        if start_time <= log_time <= end_time:
            print("The time stated in log: {}".format(log_line), "is within {}".format(start_time),
                " and {}".format(end_time))
        else:
            print("The time stated in log: {}".format(log_line), "is NOT within {}".format(start_time),
                " and {}".format(end_time))

    """

    def get_timestamp(self):
        now = self.get_now()
        if (now.month < 10):
            timestamp_month = "0" + str(now.month)
        else:
            timestamp_month = str(now.month)

        if (now.day < 10):
            timestamp_day = "0" + str(now.day)
        else:
            timestamp_day = str(now.day)

        if (now.hour < 10):
            timestamp_hour = "0" + str(now.hour)
        else:
            timestamp_hour = str(now.hour)

        if (now.minute < 10):
            timestamp_minute = "0" + str(now.minute)
        else:
            timestamp_minute = str(now.minute)

        if (now.second < 10):
            timestamp_second = "0" + str(now.second)
        else:
            timestamp_second = str(now.second)

        self.timestamp = str(now.year) + "-" + timestamp_month + "-" + timestamp_day + "_" + timestamp_hour + timestamp_minute + "hr_" + timestamp_second + "sec"

        return self.timestamp

    def generate_timestamp(self, year, month, day, hour, minute, second):
        if (month < 10):
            timestamp_month = "0" + str(month)
        else:
            timestamp_month = str(month)

        if (day < 10):
            timestamp_day = "0" + str(day)
        else:
            timestamp_day = str(day)

        if (hour < 10):
            timestamp_hour = "0" + str(hour)
        else:
            timestamp_hour = str(hour)

        if (minute < 10):
            timestamp_minute = "0" + str(minute)
        else:
            timestamp_minute = str(minute)

        if (second < 10):
            timestamp_second = "0" + str(second)
        else:
            timestamp_second = str(second)

        timestamp = str(year) + "-" + timestamp_month + "-" + timestamp_day + "_" + timestamp_hour + timestamp_minute + "hr_" + timestamp_second + "sec"

        return timestamp

    def get_calendar(self, year, month):
        calendar_table = calendar.month(year, month)
        return calendar_table

    def get_end_date_given_number_of_days(self, start_date, number_of_days):

        end_date = start_date + timedelta(days=number_of_days)

        return end_date

    # According to international standard ISO 8601, Monday is the first day of the week.
    def generate_timeline_by_week_given_2_dates(self, date_start, date_end, start_from_week_N = 1):
        difference_in_dates = date_end - date_start;
        number_of_days = difference_in_dates.days;
        number_of_days_inclusive_start_day = number_of_days + 1
        self.generate_timeline_by_week_given_number_of_days( date_start, number_of_days_inclusive_start_day, start_from_week_N)

        return None

    def generate_timeline_by_week_given_number_of_weeks(self, start_date, number_of_weeks, start_from_week_N = 1):

        number_of_days = number_of_weeks*7
        self.generate_timeline_by_week_given_number_of_days(start_date, number_of_days, start_from_week_N)

        return None

    def generate_timeline_by_week_given_number_of_days(self, start_date, number_of_days, start_from_week_N = 1):
        next_day = start_date # + timedelta(days=1);
        days_skipped = 0

        day_of_week_enum = next_day.weekday()
        day_of_week = self.days_of_week[day_of_week_enum];

        # find Monday as the start
        while (day_of_week != 'Monday'):
            next_day = next_day + timedelta(days=1)
            days_skipped = days_skipped + 1

            if (days_skipped > number_of_days):
                break
            else: # skip the day, and get the day_of_week of next_day
                day_of_week_enum = next_day.weekday()
                day_of_week = self.days_of_week[day_of_week_enum];

        week_number = start_from_week_N - 1
        day_counter_of_the_week = 0

        # Week N :  2017-07-30   - 2017-08-05
        # Monday should be found as the start day by now
        for x in range(days_skipped, number_of_days+1):
            day_counter_of_the_week = day_counter_of_the_week + 1

            if (day_counter_of_the_week == 1):
                if (next_day.day < 10):
                    day = "0" + str(next_day.day);
                else:
                    day = str(next_day.day);

                if (next_day.month < 10):
                    month = "0" + str(next_day.month);
                else:
                    month = str(next_day.month);

                start_date_of_week = str(next_day.year) + '-' + month + '-' + day

            if (day_counter_of_the_week == 7):
                # reset day_counter_of_the_week
                day_counter_of_the_week = 0

                if (next_day.day < 10):
                    day = "0" + str(next_day.day);
                else:
                    day = str(next_day.day);

                if (next_day.month < 10):
                    month = "0" + str(next_day.month);
                else:
                    month = str(next_day.month);

                end_date_of_week = str(next_day.year) + '-' + month + '-' + day
                week_number = week_number + 1

                print ("Week "+ str(week_number) +": [" + start_date_of_week + " to " + end_date_of_week + "]: ")

                if ((week_number % 10) == 0): # every n lines leave 1 empty line
                    print ("");

            next_day = next_day + timedelta(days=1)

        # make sure you don't exceed the day as it had stopped for the previous for()
        next_day = next_day - timedelta(days=1)

        # if there are still some days left
        if (day_counter_of_the_week != 0):
            if (next_day.day < 10):
                day = "0" + str(next_day.day);
            else:
                day = str(next_day.day);

            if (next_day.month < 10):
                month = "0" + str(next_day.month);
            else:
                month = str(next_day.month);

            end_date_of_week = str(next_day.year) + '-' + month + '-' + day
            week_number = week_number + 1

            day_of_week_enum = next_day.weekday()
            day_of_week = self.days_of_week[day_of_week_enum];
            print ("Week "+ str(week_number) +" (incomplete week): [" + start_date_of_week + " to " + end_date_of_week + " (" + day_of_week +")]: ")

        return None

    # N_day_stage: every N day, 1 milestone
    # start from Day N: default = 1
    def generate_timeline_by_every_N_days_given_2_dates(self, date_start, date_end, N_day_stage = 10, start_from_Day_N = 1):

        self.generate_timeline_given_2_dates(date_start, date_end, N_day_stage, start_from_Day_N)

        return None

    def generate_timeline_by_every_N_days_given_number_of_days(self, date_start, number_of_days, N_day_stage = 10, start_from_Day_N = 1):

        self.generate_timeline_given_number_of_days(date_start, number_of_days, N_day_stage, start_from_Day_N)

        return None

    # date_start is Day 1
    def generate_timeline_given_2_dates(self, date_start, date_end, N_day_stage = 10, start_from_Day_N = 1):
        difference_in_dates = date_end - date_start
        number_of_days = difference_in_dates.days;
        number_of_days_inclusive_start_day = number_of_days + 1
        self.generate_timeline_given_number_of_days( date_start, number_of_days_inclusive_start_day, N_day_stage, start_from_Day_N)

        return None

    def generate_timeline_given_number_of_days(self, start_date, number_of_days, N_day_stage = 10, start_from_Day_N = 1):
        next_day = start_date # + timedelta(days=1);

        for x in range(0, number_of_days):
            day_of_week_enum = next_day.weekday()
            day_of_week = self.days_of_week[day_of_week_enum];

            if (next_day.day < 10):
                day = "0" + str(next_day.day);
            else:
                day = str(next_day.day);

            if (next_day.month < 10):
                month = "0" + str(next_day.month);
            else:
                month = str(next_day.month);

            print ("Day "+ str(start_from_Day_N) +": ["+ month + "." + day + "]\t (" + day_of_week + ")")
            start_from_Day_N = start_from_Day_N + 1
            #print "Day ", (x+61), ": [", month, ".", day, "] :"
            next_day = next_day + timedelta(days=1);

            if (((x+1) % N_day_stage) == 0): # every n lines leave 1 empty line, default 10 days given in parameter of the function
                print ("");

        return None

    def get_time_delta_given_2_dates(self, time_earlier, time_later):
        time_delta = time_later - time_earlier;
        return time_delta

    # number_of_days after : +ve ; 	number_of_days before (back_tracked) : -ve
    def get_date_given_number_of_days(self, date_given, number_of_days):
        if (number_of_days > 0):
            tracked_date = date_given + timedelta(days=number_of_days)
            date_derived = tracked_date
            print("forward_track")
        else: # back_tracked
            back_tracked_date = date_given + timedelta(days=number_of_days)
            date_derived = back_tracked_date
            print("back_track")

        return date_derived

    def get_time_delta_formatted(self, time_earlier, time_later):
        time_format = '%Y-%m.%d_%H%M:%S'
        time_delta = datetime.strptime(time_earlier, time_format) - datetime.strptime(time_later, time_format)

        # switch the time and determine the module
        if (time_delta.days < 0):
            # time_delta = timedelta(days=0, seconds=time_delta.seconds, microseconds=time_delta.microseconds)
            temporary_holder = then
            then = now
            now = temporary_holder
            time_delta = datetime.strptime(now, time_format) - datetime.strptime(then, time_format) # re-calculate
            print("Earlier time given as 1st reference.")

            # if (time_delta.seconds > 60):
        """
        weeks, days = divmod(time_delta.days, 30)		
        hours, seconds = divmod(time_delta.seconds, 3600)
        minutes, seconds = divmod(seconds, 60)
            
        print(time_delta)
        print("weeks :" + str(weeks))
        print("days :" + str(days))
        print("hours :" + str(hours))
        print("minutes :" + str(minutes))
        print("seconds :" + str(seconds))
        
        print(time_delta.days)
        print(time_delta)			
        """
        return time_delta

    # time range: 0000 - 2359
    def chart_interval_in_hours (self, number_of_events, duration_in_hours, start_time = 0):
        number_of_intervals = number_of_events - 1
        hours_of_interval = float(duration_in_hours/number_of_intervals) #

        minutes_of_interval = float(hours_of_interval - math.floor(hours_of_interval)) # get decimal after mantissa
        minutes_of_interval = minutes_of_interval * 60

        hours_of_interval = math.floor(hours_of_interval) * 100 # in terms of 0000 - 2359 hr format

        duration_of_interval = hours_of_interval + minutes_of_interval

        milestone_in_hours = []
        milestone_in_hours.append(start_time)

        end_time = start_time + (duration_in_hours * 100) # in terms of 0000 - 2359 hr format

        next_event_time_min = start_time % 100 # get last 2 digits
        next_event_time_hour = start_time - next_event_time_min

        current_time_min = start_time % 100
        current_time_hour = start_time - current_time_min

        duration_of_interval_min = duration_of_interval % 100
        duration_of_interval_hour = duration_of_interval - duration_of_interval_min

        print('start_time: ', start_time)
        print('end_time: ', end_time)
        print('duration_of_interval: ', duration_of_interval)
        print(duration_of_interval_hour)
        print(duration_of_interval_min)

        # while(current_time <= end_time): # can't be equal because of the division truncation error, e.g. .3333*
        for i in range(0, number_of_events - 1):
            next_event_time_hour = next_event_time_hour + duration_of_interval_hour
            next_event_time_min = next_event_time_min + duration_of_interval_min

            if (next_event_time_min >= 60):
                next_event_time_hour = next_event_time_hour + 100
                next_event_time_min = next_event_time_min - 60

            next_event_time_hour = next_event_time_hour % 2400 # 24 hours clock modulo
            next_event_time = next_event_time_hour + next_event_time_min
            milestone_in_hours.append(next_event_time)
            # current_time = current_time + duration_of_interval
            # print(current_time)

        '''
        number_of_items_to_remove = 1
        # remove last timing	
        milestone_in_hours = milestone_in_hours[:-(number_of_items_to_remove)]
        '''
        return milestone_in_hours

    def seconds_to_minutes (self, seconds):
        minutes, seconds_remainder = divmod(seconds, 60)

        return [minutes, seconds_remainder]

    def minutes_to_hours (self, minutes):
        hours, minutes_remainder = divmod(minutes, 60)

        return [hours, minutes_remainder]

    def hours_to_days (self, hours):
        days, hours_remainder = divmod(hours, 24)

        return [days, hours_remainder]

    def days_to_weeks (self, days):
        weeks, days_remainder = divmod(days, 7)

        return [weeks, days_remainder]

    def days_to_months (self, days):
        months, days_remainder = divmod(days, 30)

        return [months, days_remainder]

    def days_to_years (self, days):
        years, days_remainder = divmod(days, 365)

        return [years, days_remainder]

    def months_to_years (self, months):
        years, months_remainder = divmod(months, 12)

        return [years, months_remainder]

    def __del__(self):
        print ("_gaia object [%s] removed\n" % self.id);


####################################
## main
####################################
if __name__ == "__main__":
    id = "Library Agent: < timer >"
    print ("=====[" + id + " Start]===== \n");
    ticks = time.time()
    print ("Number of ticks since 12:00am, January 1, 1970:", ticks)

    timer_object = timer(id)
    now_time = timer_object.get_now()
    now = str(now_time.year) + '-' + str(now_time.month) + '.' + str(now_time.day) + \
        '_' + str(now_time.hour) + str(now_time.minute) + ':' + str(now_time.second) # e.g. '2017-09.15_01:24:26'
    print(now)

    time_samples = ['2014-05.20_1116:52', '2014-05.20_1109:52' , '2014-05.21_1109:52', '2014-06.22_1109:52']
    # then = time_samples[len(time_samples)-1]
    then = time_samples[0]

    time_delta = timer_object.get_time_delta_formatted(now, then)
    print ("Time difference: " + str(time_delta))

    #import _Gaia._gaia
    #help(timer) # introspect

    [year, month, day, hour, min, sec] = [2011, 10, 21, 17, 50, 37]
    time_instance_reference_in_seconds = timer_object.get_time_instance_reference_in_seconds(year, month, day, hour, min, sec)
    time_past = datetime(year, month, day, hour, min, sec)

    current_time = '2017-10-22_0034hr_23sec'
    # print (current_time[0:4])
    [year, month, day, hour, min, sec] = [int(current_time[0:4]), int(current_time[5:7]), int(current_time[8:10]), int(current_time[11:13]), int(current_time[13:15]), int(current_time[18:20])]
    time_present = datetime(year, month, day, hour, min, sec)

    current_time_reference_in_seconds = timer_object.get_time_instance_reference_in_seconds(year, month, day, hour, min, sec)

    print (time_instance_reference_in_seconds, ' secs')
    print (current_time_reference_in_seconds, ' secs')

    time_delta_in_secs = current_time_reference_in_seconds - time_instance_reference_in_seconds

    print (time_delta_in_secs, ' secs')
    [minutes, seconds_remainder] = timer_object.seconds_to_minutes(time_delta_in_secs)
    print (minutes, ' mins ', seconds_remainder, ' secs')

    [hours, minutes_remainder] = timer_object.minutes_to_hours (minutes)
    print (hours, ' hrs ', minutes_remainder, ' mins')

    [days, hours_remainder] = timer_object.hours_to_days (hours)
    print (days, ' days ', hours_remainder, ' hrs')

    [years, days_remainder] = timer_object.days_to_years (days)
    print (years, ' years ', days_remainder, ' days')

    print(time_present.year, time_present.month, time_present.day, time_present.hour, time_present.minute, time_present.second)

    earlier_time = timer_object.get_earlier_time (time_past, time_present)
    print(earlier_time)

    later_time = timer_object.get_later_time (time_past, time_present)
    print(later_time)

    [number_of_events, duration_in_hours, start_time] = [4, 24, 0]
    #[number_of_events, duration_in_hours, start_time] = [4, 24, 100]
    #[number_of_events, duration_in_hours, start_time] = [4, 23, 100]
    #[number_of_events, duration_in_hours, start_time] = [5, 24, 100]
    #[number_of_events, duration_in_hours, start_time] = [4, 23, 0]
    [number_of_events, duration_in_hours, start_time] = [4, 24, 2359]
    [number_of_events, duration_in_hours, start_time] = [4, 20, 2359]
    milestone_in_hours = timer_object.chart_interval_in_hours (number_of_events, duration_in_hours, start_time)

    print(milestone_in_hours)

    print ("=====[" + id + " End]===== \n");

# version: 2017-09-23_0340hr_57sec
