import numpy as np

class lib_human_performance:
	""" Template model of Gaia """
	id = "lib_human_performance";
	inventory = {};
	inventory_id = "";
	
	velocity_trend = ['improve', 'deteriorate', 'status_quo', '']
	
	def __init__(self, id):
		self.id = id;
		print ("_gaia object [%s] is born\n" % self.id);
		
	def compute_velocity_required_to_work_completion_given_number_of_days (self, work_targeted_to_be_done, scores, unit, number_of_days_given):
		number_of_days_elapsed = len(scores) 
		number_of_days_left = number_of_days_given - number_of_days_elapsed
		work_yet_to_be_done = work_targeted_to_be_done - sum(scores)
		
		flag_nothing_to_report = False
		
		if (work_yet_to_be_done <= 0):
			print('Work done exceeded by ', abs(work_yet_to_be_done), ' ', unit)
			flag_nothing_to_report = True
		
		if (number_of_days_elapsed > number_of_days_given):
			print('Days exceed by ', abs(number_of_days_left))
			flag_nothing_to_report = True
		
		if (flag_nothing_to_report == True):
			return [None, None]
		else:
			work_yet_to_be_done_per_day = float(work_yet_to_be_done/number_of_days_left)
			return [work_yet_to_be_done_per_day, number_of_days_left]
		
		return [None, None]
		
	def compute_scores_for_each_domain(self, domain_title, tasks, weights, \
				percentage_done_for_each_task, ):
		print ("=================")
		print ("[ ", domain_title, " ]")
		print ("=================")
		number_of_tasks = len(tasks);
		score_for_each_task = [0] * number_of_tasks;
		score_total = 0;
	
		for i in range(0, number_of_tasks):   
			score_for_each_task[i] = weights[i] * percentage_done_for_each_task[i] * 100;score_total = score_total + score_for_each_task[i];
		
		print ("\n")
		
		max_str_len_allowable = 42;
		statement_to_print = "";
	
		for i in range(0, number_of_tasks):    
			statement_to_print = "Task " + str(i+1) + " :" + tasks[i] + " , " + str(weights[i]*100) + "% ";
			str_len_taken_up = len(statement_to_print);
			print (statement_to_print)
			space_to_print = max_str_len_allowable -  str_len_taken_up;
	
			for j in range(0, space_to_print):    # print spaces
				print(' ', end='')
		
			print (" || Score :", score_for_each_task[i], "%")   
	
		if (float(sum(percentage_done_for_each_task))/float(number_of_tasks) == 1):
			score_total = 100;
		else: 
			score_total = float(sum(score_for_each_task));
	
		print ("\t\t Score (total) :", score_total, " %")     
			
		return score_total
		
	def count_number_of_days_success (self, scores, domain, passing_mark):
		print ("[Domain]: ", domain)
		day_N  = len(scores)
		
		progress_trend = []
		
		number_of_days_of_passes = 0;
		number_of_days_of_failures = 0;
	
		# count successes / failures
		for i in range(0, day_N):
			if (scores[i] >= passing_mark):
				number_of_days_of_passes = number_of_days_of_passes + 1;	
			else:
				number_of_days_of_failures = number_of_days_of_failures + 1;
	
		field_tag_1 = "Total number of days (passes) ";
		field_tag_2 = "Total number of days (failures) ";
		line_field = "|| " + field_tag_1.ljust(len(field_tag_1), " ") + " || " + field_tag_2.ljust(len(field_tag_2), " ") + " ||";
		
		starting_point_of_2nd_field = len("|| " + field_tag_1.ljust(len(field_tag_1), " ")) - 1;
		
		print ("-"*(len(line_field)))
		print (line_field)
		print ("-"*(len(line_field)))
		line = "|| %3s || %3.10f %% ||" % (str(number_of_days_of_passes), float(number_of_days_of_passes)/day_N * 100);
		print (line, end ='')
		
		number_of_spaces_to_print = starting_point_of_2nd_field - len(line);
		print (" "*(number_of_spaces_to_print))
		
		line =  "|| %3s || %3.10f %% ||" % (str(number_of_days_of_failures), float(number_of_days_of_failures)/day_N * 100);
		print (line)
		print ("="*(len(line_field)))
		
		score_average = float(sum(scores))/day_N
		
		if (score_average >= passing_mark): 
			print ("PASS: exceeding by ", float(passing_mark - score_average), "%.")
		else:
			print ("FAIL: Disparity of ", float(passing_mark - score_average), "%.")
			
		number_of_days_of_ascent = 0;
		number_of_days_of_descent = 0;	
		
		print ("The average score is ", str(score_average), "%.")

		# check progress
		for i in range(1, day_N):
			if (scores[i] > scores[i-1]):
				# print ("Day ", str(i+1), " : Improvement")
				progress_trend.append(self.velocity_trend[0])
				number_of_days_of_ascent = number_of_days_of_ascent + 1;
			elif (scores[i] < scores[i-1]):
				# print ("Day ", str(i+1), " : Decline")
				number_of_days_of_descent = number_of_days_of_descent + 1;
				progress_trend.append(self.velocity_trend[1])
			elif (scores[i] == scores[i-1]):
				# print ("Day ", str(i+1), " : Constant")
				number_of_days_of_descent = number_of_days_of_descent + 1;progress_trend.append(self.velocity_trend[2])				
			else:
				pass;
		
		print ("Total number of days (in descent) ", str(number_of_days_of_descent))
		print ("Total number of days (in ascent) ", str(number_of_days_of_ascent))
		
		"""
		print "Total number of days (passes) ", str(number_of_days_of_passes), " - ", str(float(number_of_days_of_passes)/day_N * 100),"%.";
		print "Total number of days (in failures) ", str(number_of_days_of_failures), " - ", str(float(number_of_days_of_failures)/day_N * 100),"%.";
		"""		
		return progress_trend
				
	def who_am_i(self): # 
		""" Introspection """
		self.line_storage = [];
		
		print ("My name is Gaia [" + self.id + "].")
		
		return
		
	def __del__(self):
		print ("_gaia object [%s] removed\n" % self.id);
			
####################################
## main
####################################
if __name__ == "__main__":
	id = "Library Agent: Internal Agent <lib_human_performance>"
	print ("=====[" + id + " Start]===== \n")
	lib_human_performance_object = lib_human_performance(id)
	lib_human_performance_object.who_am_i()
	
	#import _Gaia._gaia
	#help(lib_human_performance) # introspect	
	
	print ("=====[" + id + " End]===== \n");
	
"""
# version: 2017-10-23_2010hr_04sec
"""		