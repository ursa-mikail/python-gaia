"""
% illutrates the utility required for long processes where each round of output
% takes a long time. User may wish to halt in condition of the detection of
% the next maxima. minima, plateau start or plateau end
% further conditions may start N maxima, N minima, N plateau start/ end from now
"""

import os, sys

# point to path
lib_path = os.path.abspath('../../../Libraries/data/trend')
sys.path.append(lib_path)
lib_path = os.path.abspath('../../../Libraries/data')
sys.path.append(lib_path)
lib_path = os.path.abspath('../../../Libraries/display/console')
sys.path.append(lib_path)

# import package from path
from trend_profiler import trend_profiler	# file name
from data_generator import data_generator
from display_console import display_console	
	
####################################
## main
####################################
if __name__ == "__main__":
	id_display_console = "Library Agent: Internal Agent <display_console>"
	print ("=====[" + id_display_console + " Start]===== \n")
	display_console_object = display_console(id_display_console)
	
	
	id_data_generator = "Test Usage Agent: <data_generator>"
	print ("=====[" + id_data_generator + " Start]===== \n")
	data_generator_object = data_generator(id_data_generator)

	id_trend_profiler = "Test Usage Agent: < trend_profiler >"
	print ("=====[" + id_trend_profiler + " Start]===== \n");
	trend_profiler_object = trend_profiler(id_trend_profiler)	
	
	# Note : some functions, for eg. a sine wave does not have a plateau
	proclivityFeatureToHuntModes = ['PLATEAU', 'MAXIMA', 'MINIMA'];
	proclivityFeatureToHunt_Choice = 0;
	proclivityFeatureToHunt = proclivityFeatureToHuntModes[proclivityFeatureToHunt_Choice];
	huntModeON = proclivityFeatureToHunt;
	display_console_object.display_variable('huntModeON', huntModeON)
	
	chosenProclivity = proclivityFeatureToHunt.upper();
	
	# BrakingCriteria
	numOfMinimaOrMaximaStoppingCriteria = 5
	crossOverNumberOfMinimaOrMaxima = 0
	
	
	plot_points = [10, 1, 1, 1, 1, 1, 2, 2, 3, 0, 5, 5, 2, 2, 4, 10, 20]
	
	proclivity_features_of_graph = []
	
	for i in range(0, len(plot_points)-1):
		previousInput = plot_points[i]
		currentInput = plot_points[i+1]
		proclivity_features_of_graph.append(trend_profiler_object.determineProclivity ( currentInput, previousInput ))
		
	display_console_object.display_variable('proclivity_features_of_graph',proclivity_features_of_graph)	
	maximas_minimas_plateaus_of_graph = []
		
	for i in range(0, len(proclivity_features_of_graph)-1):
		previousProclivity = proclivity_features_of_graph[i]
		currentProclivity = proclivity_features_of_graph[i+1]
		maximas_minimas_plateaus_of_graph.append(trend_profiler_object.trend_feature_detector( previousProclivity, currentProclivity ))
	
	display_console_object.display_variable('maximas_minimas_plateaus_of_graph', maximas_minimas_plateaus_of_graph)
		
	[locationsOfMaxOrMin, startSitesPlateau, endSitesPlateau ] = trend_profiler_object.determineLocationsOfMaximaMinimaPlateauFromProclivityFeature( maximas_minimas_plateaus_of_graph, proclivityFeatureToHunt )
	
	display_console_object.display_variable_list (['locationsOfMaxOrMin', 'startSitesPlateau', 'endSitesPlateau'], [locationsOfMaxOrMin, startSitesPlateau, endSitesPlateau])
	
	print ("=====[ ---------------------- ]===== \n")
	[locationsOfMaxOrMin, startSitesPlateau, endSitesPlateau ] = trend_profiler_object.determineLocationsOfMaximaMinimaPlateauFromProclivityFeature( proclivity_features_of_graph, proclivityFeatureToHunt )
	
	display_console_object.display_variable_list (['locationsOfMaxOrMin', 'startSitesPlateau', 'endSitesPlateau'], [locationsOfMaxOrMin, startSitesPlateau, endSitesPlateau])
	
	print ("=====[" + id_trend_profiler + " End]===== \n")
	print ("=====[" + id_data_generator + " End]===== \n")
	print ("=====[" + id_display_console + " End]===== \n")	
		
	# Ref: https://www.mathworks.com/matlabcentral/fileexchange/29432-hunt-for-local-maxima--minima--plateau?s_tid=prof_contriblnk
	"""
	
	"""