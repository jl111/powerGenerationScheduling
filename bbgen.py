import math
import copy


potentialSchedules = set([])


MAX_STARTS = 1 
MIN_ON = 3
MIN_OFF = 2
TOTAL_HOURS = 6 
MIN_FULL = MIN_ON + MIN_OFF
SCHEDULE =  TOTAL_HOURS * [0]
LAST_INDEX = TOTAL_HOURS - 1
"""
elif not schedule.minOnHoursMet():
            newSchedule = copy.copy(schedule)
            newSchedule.updateOne()
            newSchedule.updateIndex()

            BB(newSchedule)
        elif not schedule.minOffHoursMet():
            newSchedule = copy.copy(schedule)
            newSchedule.updateIndex()
            BB(newSchedule)
"""



class schedule:

    def __init__(self, index = 0, schedule = SCHEDULE, 
        numStarts = 0, onIndex = None, offIndex = None):
        self.index = index
        self.schedule = schedule
        self.numStarts = numStarts
        self.onIndex = onIndex
        self.offIndex = offIndex

    def updateIndex(self):
        self.index += 1

    def updateOnIndex(self):
        if (self.onIndex == None):
            self.onIndex = 0
        else: 
            self.onIndex += 1

    def updateOffIndex(self):
        if (self.offIndex == None):
            self.offIndex = 0
        else: 
            self.offIndex += 1

    def updateNumStarts(self):
        self.numStarts += 1
    
    def getIndex(self):
        return self.index
    def getStarts(self):
        return self.getStarts
    def getOnIndex(self):
        return self.onIndex
    def getOffIndex(self):
        return self.offIndex
    def getSchedule(self):
        return self.schedule
    def getStatus(self):
        #returns status at the hour
        return self.schedule[self.index]

    def minOnHoursMet(self):
        if (self.onIndex == None) and (self.offIndex == None):
            #never been on
            return True
        elif (self.offIndex == None):
            #currently on
            if (self.onIndex != None):
                if (self.index - self.onIndex) > MIN_ON:
                    return True
        elif (self.onIndex < self.offIndex):
            #was on, now off, mostly for error handling

            if (self.offIndex != None and self.onIndex != None):
                if (self.offIndex - self.onIndex) >= MIN_ON:
                    return True 
        else:
            return False

    def minOffHoursMet(self):
        if (self.onIndex == None) and (self.offIndex == None):
            #never been on
            return True
        elif (self.onIndex == None):
            return True
        elif self.offIndex != None:
            if (self.index - self.offIndex + 1) > MIN_OFF: 
                return True
        else:
            return False
    def maxStartsMet(self):
        return self.maxStartsMet == MAX_STARTS
            

    def minCycleLeft(self):
        return (self.current + MIN_FULL < 23)

    def updateOne(self):
        self.schedule[self.index] = 1
        if self.onIndex == None:
            self.onIndex = self.index

    def updateOffIndex(self):
         
        self.offIndex = self.index

def BB(schedule):
    if (schedule.getIndex() == LAST_INDEX):
        potentialSchedules.add(tuple(schedule.getSchedule()))
        return
    
    else:

        if schedule.maxStartsMet():
            potentialSchedules.add(tuple(schedule.getSchedule()))

        elif schedule.getStatus() == 1:
            if schedule.minOnHoursMet():
                newScheduleOne = copy.copy(schedule)
                newScheduleZero = copy.copy(schedule)

                newScheduleOne.updateIndex()
                newScheduleZero.updateIndex()
                newScheduleZero.updateOffIndex()
                BB(newScheduleZero)
                BB(newScheduleOne) 

        
        else:
            newScheduleOne = copy.copy(schedule)
            newScheduleZero = copy.copy(schedule)
            newScheduleOne.updateOne()
            newScheduleOne.updateIndex()
            newScheduleOne.updateOnIndex()
            newScheduleZero.updateIndex()

            BB(newScheduleOne)
            BB(newScheduleZero)

if __name__ == '__main__':
    BB(schedule())
    print(potentialSchedules)