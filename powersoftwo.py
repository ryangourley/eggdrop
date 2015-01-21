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
	numDiv = int(math.ceil(math.log(100, 2)))
	for check in range(0, numDiv):
		drops +=1
		floor = int(math.pow(2, check))
		#test the egg on every even floor
		if (floors[floor] == True):
			#egg 1 broke
			for newFloor in range(int(math.floor(floor/2))+1, floor):
				drops+=1
				if (floors[newFloor] == True):
					#egg 2 broke
					firstBreak = newFloor
					sumFirstBreak += firstBreak
					sumDrops += drops
					checkMax(drops)
					break
				elif (floors[newFloor] == False and newFloor == floor-1):
					#the floor egg 1 broke on is the break floor
					firstBreak = floor
					sumFirstBreak += firstBreak
					sumDrops += drops
					checkMax(drops)
					break
			break
		elif (floor == 64 and floors[floor] == False):
			for newFloor in range(floor+1, 99):
				drops+=1
				if (floors[newFloor] == True):
					#egg 2 broke
					firstBreak = newFloor
					sumFirstBreak += firstBreak
					sumDrops += drops
					checkMax(drops)
					break
				elif (floors[newFloor] == False and newFloor == 98):
					firstBreak = newFloor+1
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


