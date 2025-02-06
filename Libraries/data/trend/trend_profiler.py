

class trend_profiler:
	""" Template model of Gaia """
	id = "";
	
	def __init__(self, id):
		self.id = id;
		print ("_gaia object [%s] is born\n" % self.id);
		
	def get_intersection_symbols(self, data_list_00, data_list_01):
		x = [set(data_list_00), set(data_list_01),  ]
		data_symbols_intersection = set.intersection(*x)
		"""
		x = [{1, 2, 3}, {2, 3, 4}, {3, 4, 5}]
		set.intersection(*x)
		or
		x = [[1,2,3], [2,3,4]]
		x = [set(a) for a in x]
		"""
		data_symbols_intersection = list(data_symbols_intersection)
		
		return sorted(data_symbols_intersection)		
		
	def get_unique_symbols(self, data):
		unique_symbols = set(data)
		unique_symbols = list(unique_symbols)
		
		return sorted(unique_symbols)
		
	def get_non_repeating_symbols(self, data):
		unique_symbols = self.get_unique_symbols(data)
		frequency_of_symbols = self.find_frequency_of_symbol_list(data, unique_symbols)
		non_repeating_symbols = []
		
		for unique_symbols_index in range(0, len(unique_symbols)):
			if (frequency_of_symbols[unique_symbols_index] == 1):
				non_repeating_symbols.append(unique_symbols[unique_symbols_index])
		
		return sorted(non_repeating_symbols)
		
	
	def get_repeating_symbols(self, data):
		unique_symbols = self.get_unique_symbols(data)
		frequency_of_symbols = self.find_frequency_of_symbol_list(data, unique_symbols)
		repeating_symbols = []
		
		for unique_symbols_index in range(0, len(unique_symbols)):
			if (frequency_of_symbols[unique_symbols_index] > 1):
				repeating_symbols.append(unique_symbols[unique_symbols_index])
		
		return sorted(repeating_symbols)
	
	
	def find_frequency_of_symbol(self, data, symbol_to_hunt_for): 
		frequency_of_symbol  = 0
		
		for data_index in range(0, len(data)):
			if (data[data_index] == symbol_to_hunt_for):
				frequency_of_symbol = frequency_of_symbol + 1
					
		return frequency_of_symbol
		
	def find_locations_of_symbol(self, data, symbol_to_hunt_for):
		locations_of_symbol  = []
		
		for data_index in range(0, len(data)):
			if (data[data_index] == symbol_to_hunt_for):
				locations_of_symbol.append(data_index)
				
		return locations_of_symbol	
		
	# given a list of symbols	
	def find_frequency_of_symbol_list(self, data, symbol_list_to_hunt_for): # 
		frequency_of_symbols  = [0]*len(symbol_list_to_hunt_for)
		
		for data_index in range(0, len(data)):
			for symbol_list_index in range(0, len(symbol_list_to_hunt_for)):
				if (data[data_index] == symbol_list_to_hunt_for[symbol_list_index]):
					frequency_of_symbols[symbol_list_index] = frequency_of_symbols[symbol_list_index] + 1
					
		return frequency_of_symbols
		
	# given a list of symbols	
	def find_locations_of_symbol_list(self, data, symbol_list_to_hunt_for):
		# make a list of N different lists:
		locations_of_symbols  = [[] for i in range(len(symbol_list_to_hunt_for))]
		
		for data_index in range(0, len(data)):
			for symbol_list_index in range(0, len(symbol_list_to_hunt_for)):
				if (data[data_index] == symbol_list_to_hunt_for[symbol_list_index]):
					locations_of_symbols[symbol_list_index].append(data_index) # append list to list
				
		return locations_of_symbols		


	def  determineProclivity (self, currentInput, previousInput ):
	# DETERMINEPROCLIVITY determine plateau, acclivity, declivity
		proclivityModes = ['plateau', 'ascent', 'descent']
	
		if (currentInput == previousInput):
			proclivity = proclivityModes[0]
		elif (currentInput > previousInput):
			proclivity = proclivityModes[1]
		else: #
			proclivity = proclivityModes[2]
	
		return proclivity
		
		
	def determineLocationsOfMaximaMinimaPlateauFromProclivityFeature( self, proclivity_features_of_graph, proclivityFeatureToHunt ):
	# DETERMINELOCATIONSOFMAXIMAMINIMAPLATEAU 
	
		plateauSitesCount = 0;
		startSitesPlateau = []
		endSitesPlateau = []
		locationsOfMaxOrMin = []
		
		if (proclivityFeatureToHunt.upper() == 'PLATEAU'):
			startSiteTrackON = True
			# track start and end locations of plateau
			for i in range (0, len(proclivity_features_of_graph)):
				# start of plateau found
				if ( (proclivity_features_of_graph[i].upper() == proclivityFeatureToHunt.upper()) & startSiteTrackON ):
					startSitesPlateau.append(i)
					plateauSitesCount = plateauSitesCount + 1;
					startSiteTrackON = False
				
				# end of plateau found
				if ( (proclivity_features_of_graph[i].upper() != proclivityFeatureToHunt.upper()) & ~startSiteTrackON ):
					endSitesPlateau.append(i)
					startSiteTrackON = True
			
			if (len(startSitesPlateau) != len(endSitesPlateau)):
				endSitesPlateau[plateauSitesCount] = len(proclivity_features_of_graph) + 2
		
			return [locationsOfMaxOrMin, startSitesPlateau, endSitesPlateau ] # End Plateau tracking
		else:	
			print(proclivityFeatureToHunt)
			maxOrMinSitesCount = 0;
			for i in range (0, len(proclivity_features_of_graph)):
				if (proclivity_features_of_graph[i] == proclivityFeatureToHunt.upper()):
					locationsOfMaxOrMin.append(i)
					maxOrMinSitesCount = maxOrMinSitesCount + 1
		
			return [locationsOfMaxOrMin, startSitesPlateau, endSitesPlateau ]
	
		return None
		
	"""
	3 plateau tags:
	
	-- --       for x-x-x-x-x
	--
	
	thence, start = i, end = i + 3 + 1;
	
	"""	
	# Maxima, minima, plateau determination
	def trend_feature_detector(self, previousProclivity, currentProclivity ):
	# TRENDFEATUREDETECTOR 
	# for the next round, only the latest proclivity is required for tracking, ie. latestProclivity = currentProclivity;
		stateModes = ['plateau', 'ascent', 'descent'];
		proclivityFeatureDetectModes = ['MAXIMA', 'MINIMA', 'NO_DETECT', 'ASCENT', 'DESCENT', 'PLATEAU'];
		proclivity_feature = proclivityFeatureDetectModes[2]; # default: 'NO_DETECT'
	
		if (previousProclivity == currentProclivity): # Proclivity remains unchanged
		# proclivity_feature = proclivityFeatureDetectModes[2];
			proclivity_feature = currentProclivity.upper() # constant trend - no change
			
		if (  # 'MINIMA'
		( (previousProclivity == 'descent') & (currentProclivity == 'ascent') ) | \
		( (previousProclivity == 'plateau') & (currentProclivity == 'ascent') ) | \
		( (previousProclivity == 'descent') & (currentProclivity == 'plateau') ) \
		):
			proclivity_feature = proclivityFeatureDetectModes[1]
	
		if (  # 'MAXIMA'
		( (previousProclivity == 'ascent') & (currentProclivity == 'descent') ) | \
		( (previousProclivity == 'plateau') & (currentProclivity == 'descent') ) | \
		( (previousProclivity == 'ascent') & (currentProclivity == 'plateau') ) \
		):
			proclivity_feature = proclivityFeatureDetectModes[0]
	
		return proclivity_feature
	
	"""
	
	MINIMA
	------
	[1]
	\   /
	 \ /
	  V                  descend, ascend
	  
	[2]
		 /
		/
	___/                 plateau, ascend
	
	[3]
	\         /
	 \       /
	  \_____/
			\
			 \           descend, plateau, (ascend/ descend)
	
	MAXIMA
	------
	[1]
	  ^
	 / \
	/   \               ascend, descend
	
	[2]  
	___ 
	   \
		\
		 \              plateau, descend
	
	[3]
			 /
			/
	  _____/
	 /     \
	/       \           ascend, plateau,
	"""
			
				
	
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
	id = "Library Agent: Internal Agent <trend_profiler>"
	print ("=====[" + id + " Start]===== \n")
	trend_profiler_object = trend_profiler(id)
	trend_profiler_object.who_am_i()

	
	
	#import _Gaia._gaia
	#help(trend_profiler) # introspect	
	
	print ("=====[" + id + " End]===== \n");
	
"""
# version: 2017-10-20_2214hr_16sec
"""		