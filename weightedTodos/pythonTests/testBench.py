import time

def toM(h, m):
    return h*60 + m
#DAY 0, give static Schedule
schedule.giveClass([1,3,5], toM(10,10), toM(11,00), "PSYCH 1101")
schedule.giveClass([1,3,5], toM(11,15), toM(12,5),  "ECON 2040" )
schedule.giveClass([1,3,5], toM(12,20), toM(13,10), "ECE 4760")
schedule.giveClass([1,4],   toM(16,30), toM(19,30), "TA LAB")
schedule.giveClass([2],     toM(16,30), toM(19,30), "4760LAB")

schedule.setMeals(30, 45, 60) #sets minutes for each meal?
schedule.setSleep(toM(8,0)) #Set amount of sleep id like on average


#DAY 1, give first set of 
