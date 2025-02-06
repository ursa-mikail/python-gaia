# memory, speed, power consumption
weights_importance = [0.33, 0.25, (0.25+0.17)]
number_of_parameters = len(weights_importance)

choice_categories = ['a', 'b', 'c', 'd']

memory_of_each_subject = [0.1, 0.3, 0.4, 0.2] # == 1 (winner has the hightest allocation of reward)
speed_of_each_subject = [0.3, 0.3, -0.2, 0.6] 
power_consumption_of_each_subject = [0.25, 0.15, 0.7, -0.1]

number_of_subjects = len(choice_categories)
sums_of_subjects = [0] * number_of_subjects

array_of_parameters_scores = []
array_of_parameters_scores.append(memory_of_each_subject)
array_of_parameters_scores.append(speed_of_each_subject)
array_of_parameters_scores.append(power_consumption_of_each_subject)

print(array_of_parameters_scores)

for i in range(0, number_of_parameters):
	scores_of_parameter = array_of_parameters_scores[i] # pick either of the parameters: memory, speed, power consumption
	for j in range(0, number_of_subjects):
		sums_of_subjects[j] = sums_of_subjects[j] + weights_importance[i] * scores_of_parameter[j]

print(sums_of_subjects)
total_resource_awarded = sum(sums_of_subjects)
print("total_resource_awarded: " + str(total_resource_awarded))

sums_of_subjects_sorted = sorted(sums_of_subjects, key=float, reverse=True) # descending
print(sums_of_subjects_sorted)

for i in range(0, number_of_subjects):
	position_index = sums_of_subjects_sorted.index(sums_of_subjects[i])
	print(choice_categories[i] + " has " + str(sums_of_subjects[i]) + " at position " + str(position_index +1))

# compute distance
for i in range(0, (number_of_subjects-1)):
	distance = sums_of_subjects_sorted[i] - sums_of_subjects_sorted[i+1] # always >= 0 as it is descending order
	print(str(distance) + "\t", end="")
print()	
	

	