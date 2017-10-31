import math
potentialSchedules = set([])

MAX_STARTS = 2 
MIN_ON = 2
MIN_OFF = 2
ONE = "1"
ZERO = "0"
TOTAL_HOURS = 5
MIN_FULL = MIN_ON + MIN_OFF

#first version..  needto address conditionals more efficiently
def BB2(schedule):
	length = len(schedule)
	if length == TOTAL_HOURS: 
		potentialSchedules.add(schedule)
		return 
	else:
		#empty string
		if length == 0:
			BB2(schedule + ONE)
			BB2(schedule + ZERO)
		else: 
			last = schedule[-1]
			remainingHours = length + MIN_FULL
			if remainingHours == TOTAL_HOURS:
				if last == ZERO:
					print("0 to FULL")
					BB2(schedule + (ONE * MIN_ON) + (ZERO * MIN_OFF))
					BB2(schedule + (ZERO * MIN_FULL))
				else:
					BB2(schedule + ZERO * MIN_FULL)
					BB2(schedule + ONE)	
			elif remainingHours < TOTAL_HOURS:
				if length < MIN_ON:
					print("len < MIN_ON")
					if last == ONE:
						BB2(schedule + ONE)
			else: 
				print("ELSE")
				BB2(schedule + ONE)
				BB2(schedule + ZERO)


class schedule:

    def __init__(self, 
    	sequence, 
    	numStarts = 0,
    	currentOnStart = None,
    	currentOnEnd = None,
    	currentOffStart = None,
    	currentOffEnd = None,
    	currentIndex = 0,
    	potential = False
    	):

        self.sequence = sequence
        self.numStarts = numStarts
        self.currentOnStart = currentOnStart
        self.currentOnEnd = currentOnEnd
        self.currentOffStart = currentOffStart
        self.currentOffEnd = currentOffEnd
        self.currentIndex = currentIndex
        self.potential = potential
    
    def addZero(self):
    	self.sequence += ZERO

    def addOne(self):
    	self.sequence += ONE
    
    def length(self):
    	return len(self.sequence)
    
    def getSequence(self):
    	return self.sequence

    def checkMinOn(self):
    	return math.abs(self.currentOnEnd - self.currentOnStart) < MIN_ON 

    def checkOn(self):
    	return (self.currentOnStart != None)

    def checkOnNowOff(self):
    	return (self.currentOnEnd != None) and (self.currentOffStart != None)

    def checkMinOff(self):
    	return math.abs(self.currentOffEnd - self.currentOffStart) < MIN_OFF



def BB(S):
	length = S.length()
	if length == TOTAL_HOURS: 
		potentialSchedules.add(schedule)
		return 
	else:
		#empty string
		if length == 0:
			BB(schedule + ONE)
			BB(schedule + ZERO)
		else: 

			last = schedule[-1]
			remainingHours = length + MIN_FULL
			if remainingHours == TOTAL_HOURS:
				if last == ZERO:
					print("0 to FULL")
					BB(schedule + (ONE * MIN_ON) + (ZERO * MIN_OFF))
					BB(schedule + (ZERO * MIN_FULL))
				else:
					BB(schedule + ZERO * MIN_FULL)
					BB(schedule + ONE)
					
				
			elif remainingHours < TOTAL_HOURS:

				if length < MIN_ON:
					print("len < MIN_ON")
					if last == ONE:
						BB(schedule + ONE)
				
			else: 
				print("ELSE")
				BB(schedule + ONE)
				BB(schedule + ZERO)

if __name__ == '__main__':
	starting = schedule("010101").checkOn()
	print(starting)

	
	#BB2("")
	#print(potentialSchedules)
	#print(len(potentialSchedules))
	

