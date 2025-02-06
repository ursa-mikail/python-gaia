'''
timing
'''
####################################
import os, sys
from datetime import datetime
from datetime import timedelta

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
    '''
    year = 2015; month = 2;
    cal = timer_object.get_calendar(year, month);
    print "Here is the calendar:"
    print cal;
    '''

    number_of_days = 159
    start_date = datetime(2020, 9, 24); # Day 1

    N_day_stage = 10 # 5
    start_from_Day_N = 1 # 0
    #timer_object.generate_timeline_given_number_of_days(start_date, number_of_days)
    timer_object.generate_timeline_by_every_N_days_given_number_of_days(start_date, number_of_days, N_day_stage, start_from_Day_N)

    # trace number of days between 2 given dates
    start_date = datetime(2017, 8, 2); # Day 0
    end_date = datetime(2022, 2, 22); # Day X
    time_difference = timer_object.get_time_delta_given_2_dates(start_date, end_date)
    number_of_days = time_difference.days
    number_of_days_inclusive_start_day = number_of_days + 1

    print ("Number of days between " + str(start_date) + " and " + str(end_date) + " : " + str(number_of_days))

    # timer_object.generate_timeline_given_2_dates(start_date, end_date)

    # http://pymotw.com/2/datetime/
    start_date = datetime(2017, 8, 2, 12, 55, 0, 40); # Day 0
    end_date = datetime(2017, 8, 23, 14, 5, 15, 30); # Day X
    time_difference = timer_object.get_time_delta_given_2_dates(start_date, end_date)

    print ("Time delta between " + str(start_date) + " and " + str(end_date) + " = " + str(time_difference))

    start_date = datetime.now(); # Day 0
    end_date = datetime(2017, 8, 23, 14, 5, 15, 30); # Day X
    time_difference = timer_object.get_time_delta_given_2_dates(start_date, end_date)
    print ("Time delta between " + str(start_date) + " and " + str(end_date) + " = " + str(time_difference))

    start_date = datetime(2017, 8, 17, 14, 5, 15, 30); # Day 0
    end_date = datetime(2017, 8, 18, 13, 4, 15, 30); # Day X
    time_difference = timer_object.get_time_delta_given_2_dates(start_date, end_date)
    print ("Time delta between " + str(start_date) + " and " + str(end_date) + " = " + str(time_difference))

    start_from_Day_N, number_of_days = 10, 100
    N_day_stage = 10
    start_date = datetime(2018, 3, 10); # Day 0
    timer_object.generate_timeline_given_number_of_days(start_date, number_of_days, N_day_stage, start_from_Day_N)

    """""""""""""""""""""""""""""""""
    =================================
    Time table tableau advisor sample
    =================================
    """""""""""""""""""""""""""""""""
    if (timer_object.now_hour_of_day <= 10):
        print ("""
        Tableau 1:
            Psyche			<Study>
            Soma			<Exercise>
            Pneuma			<Mind clear>
        """)
    if (timer_object.now_hour_of_day > 10) & (timer_object.now_hour_of_day <= 15):
        print ("""
        Tableau 2:
            Opus	
            Psyche/ Opus	<Reading>
            Soma/ Pneuma	<Nap reset>
            Opus			
        """)
    if (timer_object.now_hour_of_day > 15) & (timer_object.now_hour_of_day <= 17):
        print ("""
        Tableau 3:
            Soma/ Pneuma	<Gym, shower/ rumination>
            Psyche/ Opus	<Module making>		
        """)
    if (timer_object.now_hour_of_day > 17) & (timer_object.now_hour_of_day <= 21):
        print ("""
        Tableau 4:
            Kismet/ Pneuma	<`Kismet` Module making>
            Pneuma			<Rumination>	
        """)
    if (timer_object.now_hour_of_day >= 22):
        print ("""
        You should be sleeping.	
        """)


    # track back the date
    number_of_days = -886;
    start_date = datetime(2017, 10, 22); # Day 0 (today)
    back_tracked_day = timer_object.get_date_given_number_of_days(start_date, number_of_days)

    print ("" + str(number_of_days) + " days ago from " + str(start_date) + " is:")
    print ("year: " + str(back_tracked_day.year))
    print ("month: " + str(back_tracked_day.month))
    print ("day: " + str(back_tracked_day.day))

    day_of_week_enum = back_tracked_day.weekday();
    day_of_week = timer_object.days_of_week[day_of_week_enum];
    print ("day of week: " + day_of_week)

    print ("\ntimestamp: " + timer_object.get_timestamp())

    # start_date = datetime(2017, 9, 25, 14, 5, 15, 30); # Day 0
    start_date = datetime(2017, 9, 17, 14, 5, 15, 30); # Day 0

    # end_date = datetime(2018, 1, 2, 13, 4, 15, 30); # Day X
    end_date = datetime(2018, 10, 2, 13, 4, 15, 30); # Day X
    start_from_week_N = 22
    timer_object.generate_timeline_by_week_given_2_dates(start_date, end_date, start_from_week_N)

    print ("==================================== \n");
    number_of_weeks = 5
    timer_object.generate_timeline_by_week_given_number_of_weeks( start_date, number_of_weeks, start_from_week_N)

    number_of_days = 2
    end_date = timer_object.get_end_date_given_number_of_days(start_date, number_of_days)

    print(end_date)

    print ("=====[" + id + " End]===== \n");
    """
    # version: 2017-09-23_2010hr_04sec

    delay_secs = 3;

    timer_object.timer_start();
    timer_object.sleep(delay_secs);
    timer_object.timer_stop();
    time_taken = timer_object.get_time_elapsed();
    print time_taken, " secs \n";
    timer_object.timer_pause(); # the next delay will be ignored due to the timer pause
    delay_secs = 2;
    timer_object.sleep(delay_secs);
    timer_object.timer_continue();
    timer_object.timer_pause(); # the next delay will be ignored due to the timer pause
    delay_secs = 5;
    timer_object.sleep(delay_secs);
    timer_object.timer_continue();
    ## multiple pausing
    delay_secs = 2;
    timer_object.sleep(delay_secs);
    timer_object.timer_pause(); # the next delay will be ignored due to the timer pause
    timer_object.sleep(delay_secs);
    timer_object.timer_pause(); # the next delay will be ignored due to the timer pause

    delay_secs = 5;
    timer_object.sleep(delay_secs);
    timer_object.timer_stop();
    time_taken = timer_object.get_time_elapsed();
    print (time_taken, " secs \n");

    """