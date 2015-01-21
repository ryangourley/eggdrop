import math
import random

# Initialize Problem Parameters

numTrials = 50000
sumDrops = 0
sumFirstBreak = 0
global maxDrops
maxDrops = 0

def checkMax(drops):
	"""Compares an input number of drops to the current maximum number of drops so far.
	If the input is greater than the current running max, it becomes the new max."""
	global maxDrops
	if (drops > maxDrops):
		maxDrops = drops


for trial in range(numTrials):

	eggBreak = random.randint(0, 99)
	floors = [False if x < eggBreak else True for x in range(0, 100)]
	drops = 0


	#algorithm starts
	for evenFloor in range(1, 100, 2):
		#test the egg on every even floor
		drops +=1
		if (floors[evenFloor] == True):
			#egg 1 broke
			# need to test the odd floor below it
			drops+=1
			if (floors[evenFloor -1] == True):
				#egg 2 broke on the odd floor below it
				firstBreak = evenFloor-1
				sumFirstBreak += firstBreak
				sumDrops += drops
				checkMax(drops)
				break
			else:
				#egg 2 did not break on the odd floor below it
				firstBreak = evenFloor
				sumFirstBreak += firstBreak
				sumDrops += drops
				checkMax(drops)
				break
		

print '------------------------'
print 'Number of Trials: ', numTrials
print 'Average Break Floor: ', sumFirstBreak/numTrials
print 'Average Number of drops used: ', sumDrops/numTrials
print 'Max Number of drops in this trial set: ', maxDrops


