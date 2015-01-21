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
	totalFloors = 100
	curFloor = 0
	floorJump = 13
	baseCount = 0
	while (curFloor < totalFloors):
		#test the egg on every even floor

		if (floorJump == 3):
			#the break floor must be the top floor, 99
			firstBreak = 99
			sumFirstBreak += firstBreak
			sumDrops += drops
			checkMax(drops)
			break
		else:
			curFloor+= floorJump
			drops +=1
			if (floors[curFloor] == True):
				#egg 1 broke
				# need to test the 13 floors below it
				if (baseCount == 0):

					for belowFloor in range(curFloor - floorJump, curFloor):
						drops+=1
						if (floors[belowFloor] == True):
							#egg 2 broke
							firstBreak = belowFloor
							sumFirstBreak += firstBreak
							sumDrops += drops
							checkMax(drops)
							break
						elif (floors[belowFloor] == False and belowFloor == curFloor-1):
							#the floor egg 1 broke on is the break floor
							firstBreak = curFloor
							sumFirstBreak += firstBreak
							sumDrops += drops
							checkMax(drops)
							break
					break
				else:
					for belowFloor in range((curFloor - floorJump)+1, curFloor):
						drops+=1
						if (floors[belowFloor] == True):
							#egg 2 broke
							firstBreak = belowFloor
							sumFirstBreak += firstBreak
							sumDrops += drops
							checkMax(drops)
							break
						elif (floors[belowFloor] == False and belowFloor == curFloor-1):
							#the floor egg 1 broke on is the break floor
							firstBreak = curFloor
							sumFirstBreak += firstBreak
							sumDrops += drops
							checkMax(drops)
							break
					break
			else:
				if (baseCount ==0):
					baseCount +=1
				else:
					floorJump -=1
				

print '------------------------'
print 'Number of Trials: ', numTrials
print 'Average Break Floor: ', sumFirstBreak/numTrials
print 'Average Number of drops used: ', sumDrops/numTrials
print 'Max Number of drops in this trial set: ', maxDrops