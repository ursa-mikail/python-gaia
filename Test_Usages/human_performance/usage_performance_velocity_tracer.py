import os, sys
import numpy as np

# point to path
lib_path = os.path.abspath('../../Libraries/physics')
sys.path.append(lib_path)

from lib_physics import lib_physics

####################################
## main
####################################
if __name__ == "__main__":
	scores = [75, 50, 50, 50, 50, 50, 75, 50, 50, 50, 10, 10, -25, -25, 20, -25, 50, 0, -25, 50, 10, -25, 30, 10, -25, -25, -25, -25, -25, -25, -25, -25, 10, 20, 10, 0, 25, 25, 60, 20, # <Day 40>
	75, 30, 50, 60, 
	] # unit is percentage
	
	day_N  = len(scores);
	passing_mark = 50;		# target
	unit = '%'
	
	score_total_of_the_days = 0;
	score_average_of_the_day = 0;
	score_average_of_previous_day = 0;
	
	id_lib_physics = "Test Usage Agent <lib_physics>"	
	print ("=====[" + id_lib_physics + " Start]===== \n")
	
	lib_physics_object  = lib_physics(id_lib_physics)
	
	[score_averages_of_the_day_list, velocity_and_trend, acceleration_by, target_hit_or_miss, velocity_disparity_above_or_below] = lib_physics_object.compute_velocity_and_trend_of_work_done (scores, passing_mark)
	
	# check progress
	for i in range(0, day_N):
		if (target_hit_or_miss[i] == 'HIT'):
			print ("Day ", str(i+1), " : Target reached.")
			print ("Above by ", velocity_disparity_above_or_below[i], unit, ".")
		elif (target_hit_or_miss[i] == 'MISS'):
			print ("Day ", str(i+1), " : Target unreached.")
			print ("Disparity of ", velocity_disparity_above_or_below[i],unit, ".")
		else:
			pass;	
			
		# velocity trend
		if (velocity_and_trend[i] == 'acceleration'):
			print (" : Acceleration.")
			print ("Accelerate by ", acceleration_by[i], unit, ".")
		elif (velocity_and_trend[i] == 'decceleration'):
			print (" : Decceleration.")
			print ("Deccelerate by ", acceleration_by[i], unit, ".")
		else: # constant_velocity
			print (" : ", velocity_and_trend[i], '.')			

		print ("The score_average_of_the_day is ", str(score_averages_of_the_day_list[i]), unit, ".")
		
		print()
	
	print ("=====[" + id_lib_physics + " End]===== \n");	

	
	