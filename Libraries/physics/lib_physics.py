import numpy as np

class lib_physics:
	""" Template model of Gaia """
	id = "lib_physics";
	inventory = {};
	inventory_id = "";
	
	velocity_trend = ['acceleration', 'decceleration', 'constant_velocity', '']
	
	def __init__(self, id):
		self.id = id;
		print ("_gaia object [%s] is born\n" % self.id);
		
	def compute_velocity_and_trend_of_work_done (self, scores, passing_benchmark):
		duration  = len(scores)
		
		score_total_of_the_days = 0;
		score_average_of_the_day = 0;
		score_average_of_previous_day = 0;
		acceleration_by = []
		score_averages_of_the_day_list = []
		velocity_and_trend = []
		
		target_hit_or_miss = []
		velocity_disparity_above_or_below = [] # distance from the given target benchmark score
		
		# check progress
		for i in range(0, duration):
			score_total_of_the_days = float(score_total_of_the_days + scores[i]);
			score_average_of_the_day = float(score_total_of_the_days)/(i+1)
			
			score_averages_of_the_day_list.append(score_average_of_the_day)
			
			if (score_average_of_the_day >= passing_benchmark):
				#print ("Day ", str(i+1), " : Target reached.")
				target_hit_or_miss.append('HIT')
				velocity_disparity_above_or_below.append(float(score_average_of_the_day - passing_benchmark))
			elif (score_average_of_the_day < passing_benchmark):
				#print ("Day ", str(i+1), " : Target unreached.")
				target_hit_or_miss.append('MISS')
				#print ("Disparity of -", float(passing_benchmark - score_average_of_the_day), "unit.")
				velocity_disparity_above_or_below.append(-1 * float(passing_benchmark - score_average_of_the_day) )
			else:
				pass;
				
			# print ("The score_average_of_the_day is ", str(score_average_of_the_day), "unit.")
			
			# velocity
			if (score_average_of_the_day > score_average_of_previous_day):
				velocity_and_trend.append(self.velocity_trend[0]) # Acceleration
				# print (" : ", self.velocity_trend[0].upper())
				# print ("Accelerate by ", float(score_average_of_the_day - score_average_of_previous_day), "unit.")
				acceleration_by.append(float(score_average_of_the_day - score_average_of_previous_day))
			elif (score_average_of_the_day < score_average_of_previous_day):
				velocity_and_trend.append(self.velocity_trend[1]) # Decceleration
				# print (" : ", self.velocity_trend[1].upper())
				# print ("Deccelerate by ", float(score_average_of_the_day - score_average_of_previous_day), "unit.")
				acceleration_by.append(-1 * float(score_average_of_the_day - score_average_of_previous_day))
			else:
				velocity_and_trend.append(self.velocity_trend[2]) # Constant velocity
				acceleration_by.append(0)
				# print (" : ", self.velocity_trend[2].upper())
			
			# update for comparison for the next day
			score_average_of_previous_day = score_average_of_the_day;	
			
		return [score_averages_of_the_day_list, velocity_and_trend, acceleration_by, target_hit_or_miss,
		velocity_disparity_above_or_below]
				
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
	id = "Library Agent: Internal Agent <lib_physics>"
	print ("=====[" + id + " Start]===== \n")
	lib_physics_object = lib_physics(id)
	lib_physics_object.who_am_i()
	
	#import _Gaia._gaia
	#help(lib_physics) # introspect	
	
	print ("=====[" + id + " End]===== \n");
	
"""
# version: 2017-10-23_2010hr_04sec
"""		