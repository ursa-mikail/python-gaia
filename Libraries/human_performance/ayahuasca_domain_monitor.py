import datetime

class ayahuasca_domain_monitor:
	
	def __init__(self, id):
		self.id = id
		self.name = ''
		self.scores = []
		
		self.average_score = 0.0
		# values = None # list cannot be initialized here!
		self.tasks = []
		self.tasks_weightages = []  # must add up to 1, i.e. 100%

		self.number_of_tasks = 0  #
		self.tasks_load = []  # total target for given days
		self.tasks_unit = []

		self.tasks_load_completed = []
		self.tasks_load_work_daily_targeted = []
		self.tasks_load_work_left_to_target = []
		self.tasks_load_work_left_to_target_daily = []

		self.number_of_days_given = 0
		self.start_date = None
		self.end_date = None
		self.number_of_days_left = 0

	def check_tasks_weightages(self):
		total_tasks_weightages = sum(self.tasks_weightages)
		
		if total_tasks_weightages == 0:
			print('tasks_weightages unassigned.')
		elif total_tasks_weightages < 0:
			print('tasks_weightages incompletely assigned.')
			print('Underloaded: Currently, ", (total_tasks_weightages*100), " % assigned.')
		elif total_tasks_weightages > 1:
			print('tasks_weightages wrongly assigned.')
			print('Overloaded: Currently, ", (total_tasks_weightages*100), " % assigned.')
		elif total_tasks_weightages == 1:
			print('tasks_weightages assigned.')
		else:
			pass

	def set_up_basic_parameters(self, start_date_, end_date_, total_number_of_days_given_):
		self.number_of_days_given = total_number_of_days_given_
		self.start_date = start_date_
		self.end_date = end_date_

		self.number_of_tasks = len(self.tasks)

		# setup daily expectations
		for i in range(0, self.number_of_tasks):
			self.tasks_load_work_daily_targeted.append(self.tasks_load[i] - 0)

		self.check_tasks_weightages()

	def daily_update(self):
		today = datetime.datetime.now()
        # +1 to include today
		if (today >= self.end_date): # end_date in the past
			self.number_of_days_left = (-1)*((today - self.end_date).days + 1)
		else:
			self.number_of_days_left = ((self.end_date - today).days + 1)
			
		print('Current (number_of_days_left): ', self.number_of_days_left)	
		print('today: ', today)
		print('end_date: ', self.end_date)
		return None	

	def compute_current_daily_required_work_effort(self):
		for i in range(0, self.number_of_tasks):
			self.tasks_load_work_left_to_target.append(float(self.tasks_load[i]) - float(self.tasks_load_completed[i]))

			self.tasks_load_work_left_to_target_daily.append(
                float(self.tasks_load_work_left_to_target[i]) / self.number_of_days_left)

	def set_up_domain_activities_profile(self, name, tasks, activities_workload_daily_targeted,
                                         activities_workload_units, activities_workload_accumulated_so_far,
                                         activity_weightages, start_date_, end_date_, total_number_of_days_given_):
		self.name = name
		self.number_of_tasks = len(tasks)

		for i in range(0, self.number_of_tasks):
			self.tasks.append(tasks[i])
			self.tasks_load.append(activities_workload_daily_targeted[i] * total_number_of_days_given_)
			self.tasks_unit.append(activities_workload_units[i])
			self.tasks_load_completed.append(activities_workload_accumulated_so_far[i])
			self.tasks_weightages.append(activity_weightages[i])

		self.set_up_basic_parameters(start_date_, end_date_, total_number_of_days_given_)
		self.daily_update()
		self.compute_current_daily_required_work_effort()
		
	def __del__(self):
		print ("_gaia object [%s] removed\n" % self.id)

####################################
## main
####################################
if __name__ == "__main__":
	id = "Library Agent: Internal Agent <ayahuasca_domain_monitor>"
	print ("=====[" + id + " Start]===== \n")
	ayahuasca_domain_monitor_object = ayahuasca_domain_monitor(id)
	ayahuasca_domain_monitor_object.who_am_i()
	
	#import _Gaia._gaia
	#help(ayahuasca_domain_monitor) # introspect	
	
	print ("=====[" + id + " End]===== \n");		