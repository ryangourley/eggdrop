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
	for tenFloor in range(10, 100, 10):
		#test the egg on every even floor
		drops +=1
		if (floors[tenFloor] == True):
			#egg 1 broke
			#need to test the 9 floors below it
			for belowFloor in range(tenFloor-9, tenFloor):
				drops+=1
				if (floors[belowFloor] == True):
					#egg 2 broke
					firstBreak = belowFloor
					sumFirstBreak += firstBreak
					sumDrops += drops
					checkMax(drops)
					break
				elif (floors[belowFloor] == False and belowFloor == tenFloor-1):
					#the floor egg 1 broke on is the break floor

					firstBreak = tenFloor
					sumFirstBreak += firstBreak
					sumDrops += drops
					checkMax(drops)
					break
			break
		elif (tenFloor == 90 and floors[tenFloor] == False):
			for aboveFloor in range(tenFloor+1, 100):
				drops+=1
				if (floors[aboveFloor] == True):
					#egg 1 broke on break floor
					firstBreak = aboveFloor
					sumFirstBreak += firstBreak
					sumDrops += drops
					checkMax(drops)
					break
			break

print '------------------------'
print 'Number of Trials: ', numTrials
print 'Average Break Floor: ', sumFirstBreak/numTrials
print 'Average Number of drops used: ', sumDrops/numTrials
print 'Max Number of drops in this trial set: ', maxDrops


