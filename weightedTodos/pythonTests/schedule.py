class min:
    n = [0,"0"]
    def __init__(self, x, hap):
        self.mN = x
        self.name = hap
        self.busy = 0

    def __init__(self, x):
        self.mN = x
        self.name = n[1]
        self.busy = 0

    def __init__(self):
        self.mN = n[0]
        self.name = n[1]
        self.busy = 0

class day:
    sD = ["Su", "Mo", "Tu", "We", "Th", "Fr", "Sa"]
    
    def __init__(self):
        for i in range(0,1440):
            self.mins[i] = min(i)
        self.week = 0
        self.day = 0
        self.sDay = "Su"

    def __init__(self, w):
        for i in range(0,1440):
            self.mins[i] = min(i)
        self.week = w
        self.day = 0
        self.sDay = "Su"

    def __init__(self, w, d):
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
    defaultWeek = [day(-1,0), day(-1,1), day(-1,2), day(-1,3), day(-1,4), day(-1,5), day(-1,6)]

    def __init__(self):
        self.numb = 0
        self.days = [day(), day(), day(), day(), day(), day(), day()]

    def __init__(self, n):
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
