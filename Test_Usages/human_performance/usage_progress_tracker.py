from datetime import datetime, date, time, timedelta

import os, sys

# point to path
lib_path = os.path.abspath('../../Libraries/time')
sys.path.append(lib_path)
lib_path = os.path.abspath('../../Libraries/human_performance')
sys.path.append(lib_path)
lib_path = os.path.abspath('../../Libraries/data')
sys.path.append(lib_path)
lib_path = os.path.abspath('../../Libraries/display/console')
sys.path.append(lib_path)

# test data
lib_path = os.path.abspath('./data')
sys.path.append(lib_path)

# import package from path
from timer import timer	# file name
from lib_human_performance import lib_human_performance	# file name
from data_generator import data_generator	
from display_console import display_console

####################################
## main
####################################
if __name__ == "__main__":
	"""
	This tracks the velocity of the progress, to ensure if the user is going faster or slower than the required speed to accomplish the end goal. When all the velocities are kept (on a later version), we can measure the acceleration, provide warning or advice on the peaks or valleys of the performance based on the factors which the users can mined to find the optimal reasons or conditions of which engenders the recorded resultants, etc.
	
	Here, we use the example of book reading.
	"""
	id_display_console = "Library Agent: Internal Agent <display_console>"
	print ("=====[" + id_display_console + " Start]===== \n")
	display_console_object = display_console(id_display_console)
	
	
	
	# target load to be stated
	unit = 'pages'
	
	total_number_of_pages = 348;
	additional_pages_completed = 0;
	current_pages_completed = 317 + additional_pages_completed;
	
	number_of_pages_left =  total_number_of_pages - current_pages_completed;
	
	total_number_of_days_given = 100;
	number_of_days = total_number_of_days_given;
	
	id_timer = "Test Usage Agent: < timer >"
	print ("=====[" + id_timer + " Start]===== \n");
	timer_object = timer(id_timer);
	
	start_date = datetime(2016, 1, 31); # Day 0
	# today = datetime.datetime(2015, 9, 18); 
	today = timer_object.get_now()
	print ("Now: " + str(today))
	
	time_earlier = start_date
	time_later = today
	time_elapsed = timer_object.get_time_delta_given_2_dates(time_earlier, time_later)
	print (time_elapsed)
	
	time_later = timedelta(0, 8, 562000)
	time_later = timedelta(days = 5)
	print (time_later)
	
	current_days_elapsed = time_elapsed.days;
	# get secs: divmod(time_elapsed.days * 86400 + time_elapsed.seconds, 60)
	
	average_pages_required_to_complete_per_day = float(total_number_of_pages)/float(total_number_of_days_given);
	
	print ("average_pages_required_to_complete_per_day (planned) : ", average_pages_required_to_complete_per_day, " pages")
	
	number_of_days_left = total_number_of_days_given - current_days_elapsed
	
	average_pages_to_complete_per_day_updated = float(number_of_pages_left)/float(number_of_days_left);
	
	print ("average_pages_to_complete_per_day_updated (current progress) : ", average_pages_to_complete_per_day_updated, " pages")
	
	print ("number_of_pages_left (current progress) : ", number_of_pages_left, " pages")
	
	if (float(current_days_elapsed) != 0):
		current_pages_completion_velocity = float(current_pages_completed)/float(current_days_elapsed);
		print ("current_pages_completion_velocity (current progress) : ", current_pages_completion_velocity, " pages")
	else:
		print ("Day 0: Activity not started.")
		
	book_completed_in_percent = float(current_pages_completed)/float(total_number_of_pages) * 100;
	book_to_be_completed_in_percent = 100 - book_completed_in_percent;
	
	print ("book_completed_in_percent : ", book_completed_in_percent, " %")
	print ("book_to_be_completed_in_percent : ", book_to_be_completed_in_percent, " %")	
	
	print ("=====[" + id_timer + " End]===== \n");
	
	"""
	# Human Domain Performance Tracking #
	"""	
	# ====================================================
	# import data from test data 
	from human_domains_scores import * # pneumaScores, psycheScores, somaScores, opusScores, kismetScores
	
	id_lib_human_performance = "Test Usage Agent: < lib_human_performance >"
	print ("=====[" + id_lib_human_performance + " Start]===== \n");
	lib_human_performance_object = lib_human_performance(id_lib_human_performance);	
	
	domains = ['pneuma', 'psyche', 'soma', 'opus', 'kismet'];
	number_of_domain = len(domains)
	
	domain_pneuma_data_object = domain_pneuma()
	domain_psyche_data_object = domain_psyche()
	domain_soma_data_object = domain_soma()
	domain_opus_data_object = domain_opus()
	domain_kismet_data_object = domain_kismet()
	
	domain_data_objects = [domain_pneuma_data_object, domain_psyche_data_object, domain_soma_data_object, domain_opus_data_object, domain_kismet_data_object]
	
	for domain_index in range(0, number_of_domain):
		lib_human_performance_object.compute_scores_for_each_domain(domain_data_objects[domain_index].domain_title, domain_data_objects[domain_index].tasks, domain_data_objects[domain_index].weights, \
	domain_data_objects[domain_index].percentage_done_for_each_task)
	
	
	passing_mark = 50
	domain_scores = [pneumaScores, psycheScores, somaScores, opusScores, kismetScores]
	
	for domain_index in range(0, number_of_domain):
		lib_human_performance_object.count_number_of_days_success (domain_scores[domain_index], domains[domain_index], passing_mark)
	
	print ("=====[" + id_lib_human_performance + " End]===== \n");	
	
	id_data_generator = "Library Agent: Internal Agent <data_generator>"
	print ("=====[" + id_data_generator + " Start]===== \n")
	data_generator_object = data_generator(id_data_generator)
	
	# find acceleration as energy / momentum monitoring
	number_of_days = 100;
	[0] * number_of_days;
	velocities_of_each_day = [0] * number_of_days;
	accelerations_of_each_day = [0] * number_of_days;
		
	# generate random test data	
	upper_bound = 5;
	lower_bound = 0;
	number_of_data_points = number_of_days
	number_of_pages_per_day = data_generator_object.generate_random_integers(number_of_data_points, upper_bound, lower_bound)	
	
	# may not be disparate as some days are multiples of each other, 30, 35, 42, 
	number_of_data_points = 1
	
	for i in range(0, number_of_days):
		if (((i + 1) % 5 == 0)):	# weekend: Friday
			upper_bound = 12;
			lower_bound = 5;
			number_of_pages_per_day[i] = data_generator_object.generate_random_integers(number_of_data_points, upper_bound, lower_bound)
		elif (((i + 1) % 6 == 0)):	# weekend: Saturday
			upper_bound = 12;
			lower_bound = 4;
			number_of_pages_per_day[i] = data_generator_object.generate_random_integers(number_of_data_points, upper_bound, lower_bound)
		elif (((i + 1) % 7 == 0)):	# weekend: Sunday
			upper_bound = 9;
			lower_bound = 4;
			number_of_pages_per_day[i] = data_generator_object.generate_random_integers(number_of_data_points, upper_bound, lower_bound)
		else:
			upper_bound = 7;
			lower_bound = 0;	
			number_of_pages_per_day[i] = data_generator_object.generate_random_integers(number_of_data_points, upper_bound, lower_bound)
	
	offset = 22
	every_N_days = 5
	# deliberate add offset every N days to simulate pattern
	for i in range(0, number_of_days):
		if (((i + 1) % every_N_days == 0)):	
			number_of_pages_per_day[i] = number_of_pages_per_day[i] + offset

	every_N_days = 7
	data_description = number_of_pages_per_day
	display_console_object.print_data_formatted_N_per_row(number_of_pages_per_day, data_description, every_N_days)
	
	# sum all efforts 
	total_pages_done = 0;
	number_of_days_elapsed = 0;
	for i in range(0, number_of_days):
		total_pages_done = total_pages_done + number_of_pages_per_day[i];
		number_of_days_elapsed = (i+1);
		velocities_of_each_day[i] = float(total_pages_done)/float(number_of_days_elapsed); #
		
		if (i > 0):
			accelerations_of_each_day[i] = velocities_of_each_day[i] - velocities_of_each_day[i-1];
		
	print ("total_pages_done: ", total_pages_done, "\n")
	
	data_description = "velocities_of_each_day"
	display_console_object.print_data_formatted_N_per_row(velocities_of_each_day, data_description, every_N_days)
	
	data_description = "accelerations_of_each_day"
	display_console_object.print_data_formatted_N_per_row(accelerations_of_each_day, data_description, every_N_days)
	
	work_targeted_to_be_done = 10000
	number_of_days_given = 48
	scores = [9115]
	# scores.extend([0]*50) # append another list
	display_console_object.display_variable ('scores', scores)
	
	unit = 'pull-ups'
	[work_yet_to_be_done_per_day, number_of_days_left] = lib_human_performance_object.compute_velocity_required_to_work_completion_given_number_of_days (work_targeted_to_be_done, scores, unit, number_of_days_given)
	
	display_console_object.display_variable ('work_yet_to_be_done_per_day', work_yet_to_be_done_per_day)
	display_console_object.display_variable ('number_of_days_left', number_of_days_left)
	
	passing_mark = 50;
	progress_trend = lib_human_performance_object.count_number_of_days_success (scores_reference, "NO DESCRIPTION", passing_mark)
	display_console_object.display_variable ('progress_trend', progress_trend)
	
	print ("=====[" + id_data_generator + " End]===== \n")
	print ("=====[" + id_display_console + " End]===== \n")
	'''
	row_size = 2;
	column_size = 5;
	
	matrix = [[0 for x in range(column_size)] for x in range(row_size)] 
	count = 0;
	
	for x in range (0, row_size):
		for y in range (0, column_size):
			count = count + 1;
			matrix[x][y] = count;
			print("%d" % matrix[x][y]),
		print("\n");
	
	string_row_0 = [];
	#string_row_0 = ', '.join([str(matrix[0][0:(column_size-1)]) for x in list])
	#string_row_0 = ', '.join(str(matrix[0][0:(column_size-1)]) for x in list)
	y = matrix[1][0:(column_size-1)];
	
	print y, "\n";
	string_row_0 = ''.join(str(matrix[0][0:(column_size-1)]));
	print string_row_0, "\n";
	string_row_0 = str(string_row_0).strip('[]');
	print string_row_0, "\n";
	string_row_0 = string_row_0.replace(" ", "");
	string_row_0 = string_row_0.replace(",", "");
	print string_row_0, " : ", "length = ", len(string_row_0), "\n";
	
	## string to array
	array_0 = list(string_row_0);
	print array_0, " : ", "length = ", len(array_0), "\n";
	'''
