'''
text_statistics_estimation i.e. find frequencies of text occurences, etc
'''
import re

class text_statistics_estimator:
	""" Template model of Gaia """
	id = "text_statistics_estimator"
	
	def __init__(self, id):
		self.id = id;
		print ("_gaia object [%s] is born\n" % self.id);

	def get_frequency(self, filtered_tokens_unique, filtered_tokens):
		frequencies = [0] * len(filtered_tokens_unique);

		for i in range(0, len(filtered_tokens_unique)):
			for j in range(0, len(filtered_tokens)):
				if filtered_tokens_unique[i] == filtered_tokens[j]:
					frequencies[i] = frequencies[i] + 1;
				else:
					pass;
				# trim the original list
			while (filtered_tokens_unique[i] in filtered_tokens):
				filtered_tokens.remove(filtered_tokens_unique[i]);

		return frequencies;

	#
	def get_keywords_with_the_frequency(self, filtered_tokens_unique, frequencies, frequency_target):

		keywords_with_the_frequency = [];
		keywords_with_the_frequency_indices = [];

		if (frequency_target in frequencies):

			for i in range(0, len(frequencies)):
				if (frequency_target == frequencies[i]):
					keywords_with_the_frequency_indices.append(i);
			print("keywords_with_the_frequency_indices: " + str(keywords_with_the_frequency_indices))

			if (len(keywords_with_the_frequency_indices) == 1):  # if only 1 was found
				keywords_with_the_frequency.append(filtered_tokens_unique[keywords_with_the_frequency_indices[0]]);
				print("Only 1 found")
			else:
				print(str(len(keywords_with_the_frequency_indices)) + " found.")
				for j in range(0, len(keywords_with_the_frequency_indices)):
					keywords_with_the_frequency.append(filtered_tokens_unique[keywords_with_the_frequency_indices[j]]);

		else:
			print("Not found.")

		return keywords_with_the_frequency


	def get_keywords_and_frequencies_within_frequency_range(self, filtered_tokens_unique, frequencies, frequency_upper,
															frequency_lower):
		if (frequency_upper < frequency_lower):
			sys.exit("Error in get_keywords_and_frequencies_within_frequency_range(): frequency_upper < frequency_lower")
	
		keywords_within_frequency_range = [];
		keywords_frequencies_within_frequency_range = [];
		keywords_within_frequency_range_indices = [];
		# get the indices
		for i in range(0, len(frequencies)):
			if ((frequency_upper >= frequencies[i]) & (frequency_lower <= frequencies[i])):
				keywords_within_frequency_range_indices.append(i);
			else:
				pass;
		print("keywords_within_frequency_range_indices: " + str(keywords_within_frequency_range_indices))
	
		if (len(keywords_within_frequency_range_indices) == 1):  # if only 1 was found
			keywords_within_frequency_range.append(filtered_tokens_unique[keywords_within_frequency_range_indices[0]]);
			keywords_frequencies_within_frequency_range.append(frequencies[keywords_within_frequency_range_indices[0]]);
			print("Only 1 found")
		else:
			print(str(len(keywords_within_frequency_range_indices)) + " found.")
			for j in range(0, len(keywords_within_frequency_range_indices)):
				keywords_within_frequency_range.append(filtered_tokens_unique[keywords_within_frequency_range_indices[j]]);
				keywords_frequencies_within_frequency_range.append(frequencies[keywords_within_frequency_range_indices[j]]);
	
		return [keywords_within_frequency_range, keywords_frequencies_within_frequency_range];
	
	
	def remove_keywords_with_the_frequency(self, filtered_tokens_unique, frequencies, frequency_target):
		keywords_without_the_frequency = [];
		keywords_frequencies_without_the_frequency = [];
		keywords_without_the_frequency_indices = [];
		# get the indices
		for i in range(0, len(frequencies)):
			if (frequency_target == frequencies[i]):
				pass;
			else:
				keywords_without_the_frequency_indices.append(i);
		# print("keywords_without_the_frequency_indices: " + str(keywords_without_the_frequency_indices))
	
		if (len(keywords_without_the_frequency_indices) == 1):  # if only 1 was found
			keywords_without_the_frequency.append(filtered_tokens_unique[keywords_without_the_frequency_indices[0]]);
			keywords_frequencies_without_the_frequency.append(frequencies[keywords_without_the_frequency_indices[0]]);
			print("Only 1 found")
		else:
			print(str(len(keywords_without_the_frequency_indices)) + " found.")
			for j in range(0, len(keywords_without_the_frequency_indices)):
				keywords_without_the_frequency.append(filtered_tokens_unique[keywords_without_the_frequency_indices[j]]);
				keywords_frequencies_without_the_frequency.append(frequencies[keywords_without_the_frequency_indices[j]]);
	
		return [keywords_without_the_frequency, keywords_frequencies_without_the_frequency];
	
	
	def remove_keywords_within_frequency_range(self, filtered_tokens_unique, frequencies, frequency_upper, frequency_lower):
		if (frequency_upper < frequency_lower):
			sys.exit("Error in get_keywords_and_frequencies_within_frequency_range(): frequency_upper < frequency_lower")
	
		keywords_not_within_frequency_range = [];
		keywords_frequencies_not_within_frequency_range = [];
		keywords_not_within_frequency_range_indices = [];
		# get the indices
		for i in range(0, len(frequencies)):
			if ((frequency_upper > frequencies[i]) & (frequency_lower < frequencies[i])):
				pass;
			else:
				keywords_not_within_frequency_range_indices.append(i);
		# print("keywords_not_within_frequency_range_indices: " + str(keywords_not_within_frequency_range_indices))
	
		if (len(keywords_not_within_frequency_range_indices) == 1):  # if only 1 was found
			keywords_not_within_frequency_range.append(
				filtered_tokens_unique[keywords_not_within_frequency_range_indices[0]]);
			keywords_frequencies_not_within_frequency_range.append(
				frequencies[keywords_not_within_frequency_range_indices[0]]);
			print("Only 1 found")
		else:
			print(str(len(keywords_not_within_frequency_range_indices)) + " found.")
			for j in range(0, len(keywords_not_within_frequency_range_indices)):
				keywords_not_within_frequency_range.append(
					filtered_tokens_unique[keywords_not_within_frequency_range_indices[j]]);
				keywords_frequencies_not_within_frequency_range.append(
					frequencies[keywords_not_within_frequency_range_indices[j]]);
	
		return [keywords_not_within_frequency_range, keywords_frequencies_not_within_frequency_range]

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
	id = "Library Agent: Internal Agent <text_statistics_estimator>"
	print ("=====[" + id + " Start]===== \n")
	text_statistics_estimator_object = text_statistics_estimator(id)
	text_statistics_estimator_object.who_am_i()
	

	
	#import _Gaia._gaia
	#help(text_statistics_estimator) # introspect
	
	print ("=====[" + id + " End]===== \n");
	
"""
# version: 2017-09-23_2010hr_04sec
"""		