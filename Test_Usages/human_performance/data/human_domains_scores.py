scores_reference = [
75, 50, 50, 50, 50, 50, 75, 50, 50, 50, 10, 10, -25, -25, 20, -25, 50, 0, -25, 50, 10, -25, 30, 10, -25, -25, -25, -25, -25, -25, -25, -25, 10, 20, 10, 0, 25, 25, 60, 20, 75, 30, 50, 70, 25, 60, 60, 60, -25, 50, 50, 75, 60, 135, 70, 60, 100, 70, 100, 120, 110, 100, 95, 135, 110, 110, 150, 180, 210, 250, 160, 200, 230, 300, 410, 10, 150, 200, 200, 100, 150, 250, 350, 130, 100, 100, 100, 100, 250, 100, 
100, 100, 100, 50, 100, 100, -25, 100, 50, 100
]

pneumaScores = [100, 90, 45, 50, 65, 75, 70, 20, 60, 20, 50, 80, 45, 60, 20, 0, 35, 20, 20, 35, 40, 20, 90, 20, 35, 20, 40, 55, 20, 20, 0, 20, 60, 20, 45, 40, 20, 20, 20, 70, 40, 70, 50, 50, 20, 50, 90, 60, 20, 40, # <Day 50>
	40, 20, 0, 50, 60, 50, 30, 50,
	
	];
psycheScores = [10, 10, 10, 10, 10, 33, 50, 100, 100, 20, 0, 0, 0, -25, -25, -25, 0, 0, -25, 0, 0, -25, 0, 10, 30, 10, 10, 0, 10, -25, -25, -25, -25, 110, 10, 20, 10, 10, 10, 310, 210, 140, 50, 50, -25, -25, 40, 80, 10, 10, # <Day 50>
	-25, -25, 0, 0, 10, 10, -25, 
	
	];
somaScores = [75, 50, 50, 50, 50, 50, 75, 50, 50, 50, 10, 10, -25, -25, 20, -25, 50, 0, -25, 50, 10, -25, 30, 10, -25, -25, -25, -25, -25, -25, -25, -25, 10, 20, 10, 0, 25, 25, 60, 20, 75, 30, 50, 70, 25, 60, 60, 60, -25, 50, # <Day 50>
	50, 75, 60, 135, 70, 60, 100, 50, 
	
	];
opusScores = [33, 33, 33, 66, 66, 110, 100, 66, 66, 66, 66, 66, 133, 66, 0, 33, 100, 33, 33, 100, 0, 66, 100, 66, 0, 33, -25, -25, 33, -25, -25, 33, 66, 33, 0, 0, 0, -25, 0, 100, 0, 133, -25, 33, 33, 100, 66, 0, 33, 100, # <Day 50>
	0, 100, -25, 66, 33, 77, 66, 66,
	];
kismetScores = [33, -25, 100, 33, 0, 33, 33, 66, 0, 33, 33, 66, 66, 100, 0, 0, 33, -25, 0, 0, 33, -25, -25, 66, -25, -25, -25, 66, -25, 33, 0, -25, 0, 0, -25, 33, 0, 33, -25, 33, 33, 100, 0, 33, -25, -25, 0, 0, -25, -25, # <Day 50>
	-25, -25, -25, 33, 0, 0, 33, 33, 
	]; 
	
	
class domain_pneuma:
	domain_title = 'Pneuma'
	id = domain_title
	tasks = ["Sangfroid conditioning (deep calm 3x)/ Set a time-space for yourself (`shut out the world`)",
	"1 simple idea a day",
	"* To maintain the will to do the impossible and daunting",
	"+ focusing 3x20 mins a day (`flow` induction)"
	];
	
	weights = [.60, .10, .15, .15]; # in percentages: [60%, 10%, 15%, 15%]
	
	# sample score of the day
	percentage_done_for_each_task = [
		float(60)/float(60), 
		float(0)/float(10), 
		float(5)/float(15), 
		float(15)/float(15),	
	]; 
	
	def __init__(self, id = domain_title):
		print ("domain_pneuma object [%s] is born\n" % self.id)		
	
	def __del__(self, id = domain_title):
		print ("[%s] object removed\n" % self.id);	
		
class domain_psyche:
	domain_title = 'Psyche'
	id = domain_title
	tasks = ["2 pages (physics)", # [50%]"
	"lecture (5 min)", # [33%]"
	];
	
	weights = [.50, .50]; # in percentages: [50%, 50%]
	
	# sample score of the day
	percentage_done_for_each_task = [
		float(0)/float(50), 
		float(0)/float(50), 
	]
	
	def __init__(self, id = domain_title):
		print ("domain_pneuma object [%s] is born\n" % self.id)		
	
	def __del__(self, id = domain_title):
		print ("[%s] object removed\n" % self.id)
		
class domain_soma:
	domain_title = 'Soma'
	id = domain_title
	tasks = ["horse stance (5 min)", # [33%]"
	"30 pull-ups", # [33%]"
	"50 dips", # [33%]"
	];
	
	weights = [.33, .33, .33]; # in percentages: [33.33%, 33.33%, 33.33%]
	
	# sample score of the day
	percentage_done_for_each_task = [
		float(33)/float(33), 
		float(33)/float(33), 
		float(33)/float(33*5), 
	]
	
	def __init__(self, id = domain_title):
		print ("domain_pneuma object [%s] is born\n" % self.id)		
	
	def __del__(self, id = domain_title):
		print ("[%s] object removed\n" % self.id)

		
class domain_opus:
	domain_title = 'Opus';
	id = domain_title
	tasks = ["1 pg reference code review", # [33%]"
	"2 pg system review", # [33%]"
	"1 `trick shot` code/logic module a day", # [33%]"
	];
	
	weights = [.33, .33, .33]; # in percentages: [33.33%, 33.33%, 33.33%]
	
	# sample score of the day
	percentage_done_for_each_task = [
		float(0)/float(5), 
		float(33)/float(33), 
		float(33)/float(33), 
	]
	
	def __init__(self, id = domain_title):
		print ("domain_pneuma object [%s] is born\n" % self.id)		
	
	def __del__(self, id = domain_title):
		print ("[%s] object removed\n" % self.id)
		
	
class domain_kismet:
	domain_title = 'Kismet';
	id = domain_title
	tasks = ["1 event that leads to possible progress for forming organization to do good.", # [33%]"
	"Build intelligent / assisting entities/ modules in daily life.", # [33%]"
	"1 strategic approach/ insight (put a * indicator)", # [33%]"
	];
	
	weights = [.33, .33, .33]; # in percentages: [33.33%, 33.33%, 33.33%]
	
	# sample score of the day
	percentage_done_for_each_task = [
		float(33)/float(33), 
		float(0)/float(33), 
		float(0)/float(33), 
	]
	
	def __init__(self, id = domain_title):
		print ("domain_pneuma object [%s] is born\n" % self.id)		
	
	def __del__(self, id = domain_title):
		print ("[%s] object removed\n" % self.id)
	
	

		