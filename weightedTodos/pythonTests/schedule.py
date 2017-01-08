import datetime.date

class min:
    n = [0,"0"]
    def __init__(self, x = n[0], hap = n[1]):
        self.mN = x
        self.name = hap
        self.busy = 0
        
    def isBusy(self):
        return self.busy > 0

class day:
    sD = ["Su", "Mo", "Tu", "We", "Th", "Fr", "Sa"]
    
    def __init__(self, w = 0, d = 0):
        for i in range(0,1440):
            self.mins[i] = min(i)
        self.week = w
        self.day = d
        self.sDay = sD[d]

    def setMins(self, rng, wha, bus):
        for i in rng:
            self.mins[i].name = wha
            self.mins[i].busy = bus
        

class week:
    defaultWeek = [day(w = -1,d = 0), day(w = -1,d = 1), day(w = -1,d = 2), day(w = -1,d = 3), day(w = -1,d = 4), day(w = -1,d = 5), day(w = -1,d = 6)]

    def __init__(self, n = 0):
        self.numb = n
        self.days = [day(), day(), day(), day(), day(), day(), day()]
        
    def setDay(self, d, rng, wha):
        self.days[d].setMins(rng,wha)

class Schedule:
    
    
    def __init__(self,iWeek):
        self.iWeek = iWeek
        self.weeks = [week(0),week(1)]

    def giveClass(days, froT, tilT, name):
        for i in days:
            for j in range(froT, tilT+1):
                defaultWeek[i][j]


    def toWeeks(yr, mn, da):
        #someMathIDKAbout
        return(1)
