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
	for floor in range(0, 100):
		#test the egg on every even floor
		drops +=1
		if (floors[floor] == True):
			#egg 1 broke
				firstBreak = floor
				sumFirstBreak += firstBreak
				sumDrops += drops
				checkMax(drops)
				break

print '------------------------'
print 'Number of Trials: ', numTrials
print 'Average Break Floor: ', sumFirstBreak/numTrials
print 'Average Number of drops used: ', sumDrops/numTrials
print 'Max Number of drops in this trial set: ', maxDrops


