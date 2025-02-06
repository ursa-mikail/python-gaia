import datetime

import os, sys
import numpy as np

# point to path
lib_path = os.path.abspath('../../Libraries/human_performance')
sys.path.append(lib_path)

from ayahuasca_domain_monitor import ayahuasca_domain_monitor

# to-do: input scores using next-day(), and ensure index does not start from -1 (Day 0)

def print_profile(domain):
	print('Name: %s' % domain.name)
	print('Daily scores: ')
	for score in domain.scores:
		print(score)
	print('Average score: ')
	print(domain.average_score)
	total_number_of_tasks = len(domain.tasks)
	print('Tasks: There are %s tasks.' % total_number_of_tasks)
	i = 0
	for task in domain.tasks:
		print('[%s] %s' % ((i + 1), task))
		i += i
	print('<< Tasks\' loads >> ')
	for i in range(0, domain.number_of_tasks):
		print('[%s' % (i + 1) + '] %s' % domain.tasks[i] + ' : %s' % domain.tasks_load[i] + ' %s '
			% domain.tasks_unit[i] + ' %s ' % domain.number_of_days_given + ' days.')
	
	print('<< Tasks completion status >> ')
	for i in range(0, domain.number_of_tasks):
		print(domain.tasks[i] + ": %s" % domain.tasks_load_completed[i] + ' %s ' % domain.tasks_unit[i])
	
	print('<< Tasks daily planned target status >> ')
	for i in range(0, domain.number_of_tasks):
		print('Task #%s' % str(i) + ': tasks_load_work_daily_targeted : %s' 
			% domain.tasks_load_work_daily_targeted[i] + ' %s ' % domain.tasks_unit[i])
	
	print('\n<< Tasks current daily required target status >> ')
	for i in range(0, domain.number_of_tasks):
		print('Task #%s' % str(i) + ': tasks_load_work_left_to_target_daily : %s' 
			% domain.tasks_load_work_left_to_target_daily[i] + ' %s ' + domain.tasks_unit[i])
	
	print('Start_date : %s' % domain.start_date)
	print('End_date : %s' % domain.end_date)
	print('Number_of_days_left : %s' % domain.number_of_days_left)


# =========================================
# main
# =========================================
if __name__ == '__main__':
	total_number_of_days_given = 100
	
	start_date = datetime.datetime(2017, 10, 30)  # Day 1
	# next_day = start_date + datetime.timedelta(days=1)
	end_date = start_date + datetime.timedelta(days=total_number_of_days_given)
	today = datetime.datetime.now()
	# << Pneuma >>
	pneuma_activities = ['Sangfroid conditioning (deep calm 3x)/ Set a time-space for yourself (`shut out the world`)',
						'1 simple idea a day.', '* To maintain the will to do the impossible and daunting.',
						'+ focusing 3x20 mins a day (`flow` induction)']
	pneuma_activities_workload_daily_targeted = [60, 1, 3, 60]
	pneuma_activities_workload_units = ['min', 'time', 'intent', 'min']
	
	pneuma_activity_weightages = [0.6, 0.1, 0.15, 0.15]
	
	pneuma_activities_workload_accumulated_so_far = [0, 0, 0, 0]
	
	id_ayahuasca_domain_monitor = "Test Usage Agent <ayahuasca_domain_monitor>"	
	print ("=====[" + id_ayahuasca_domain_monitor + " Start]===== \n")
	
	pneuma = ayahuasca_domain_monitor(id_ayahuasca_domain_monitor)
	pneuma.set_up_domain_activities_profile('Pneuma', pneuma_activities, pneuma_activities_workload_daily_targeted,
											pneuma_activities_workload_units,
											pneuma_activities_workload_accumulated_so_far, pneuma_activity_weightages,
											start_date, end_date, total_number_of_days_given)
	
	
	
	# << Psyche >>
	psyche_activities = ['lecture', 'Book: Decision Procedure',
						'* Mnemonic practice - recommended: upon awake and before sleep']
	psyche_activities_workload_daily_targeted = [4, float(293) / 100, 1]
	psyche_activities_workload_units = ['min', 'page', 'time']
	psyche_activity_weightages = [0.40, 0.50, 0.10]
	psyche_activities_workload_accumulated_so_far = [42, 0, 0]
	
	psyche = ayahuasca_domain_monitor(id_ayahuasca_domain_monitor)
	psyche.set_up_domain_activities_profile('Psyche', psyche_activities, psyche_activities_workload_daily_targeted,
											psyche_activities_workload_units,
											psyche_activities_workload_accumulated_so_far, psyche_activity_weightages,
											start_date, end_date, total_number_of_days_given)
											
										
	# << Soma >>
	soma = ayahuasca_domain_monitor(id_ayahuasca_domain_monitor)
	soma_activities = ['pull-ups', 'mins horse stance']
	
	soma_activities_workload_daily_targeted = [20, 5]
	soma_activities_workload_units = ['time', 'min']
	soma_activity_weightages = [0.50, 0.50]
	soma_activities_workload_accumulated_so_far = [(2000 - 1196), 145]
	soma.set_up_domain_activities_profile('Soma', soma_activities, soma_activities_workload_daily_targeted,
										soma_activities_workload_units, soma_activities_workload_accumulated_so_far,
										soma_activity_weightages, start_date, end_date, total_number_of_days_given)
										
	
	
	print_profile(pneuma)
	pneuma.daily_update()
	
	print(' ========================================= ')
	print_profile(psyche)
	psyche.daily_update()	
	
	print(' ========================================= ')
	print_profile(soma)
	soma.daily_update()
	
	print ("=====[" + id_ayahuasca_domain_monitor + " End]===== \n");