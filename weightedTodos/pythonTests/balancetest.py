starts = [0,1,3]
fins   = [6,5,6]
times  = [7,10,11]
tempTimes = [7,10,11]
total = times[0] + times[1] + times[2]

lengths = [0,0,0]

aSch = [0,0,0,0,0,0,0]
bSch = [0,0,0,0,0,0,0]
cSch = [0,0,0,0,0,0,0]
Sch = [aSch, bSch, cSch]
total /= -7
diff = [total, total, total, total, total, total, total]

def initSch():
    for i in range(0,3):
        lengths[i] = fins[i] - starts[i]
        lengths[i] += 1
        for x in range(starts[i], fins[i]+1):
            Sch[i][x] = times[i] / lengths[i]
    for x in range(0, 7):
        for i in range(0, 3):
            diff(x) += Sch[i][x]


def displaceinto(dest):
    max = diff[dest]
    need = max
    ind = dest
    for x in range(0,7):
        if x ~= dest:
            if diff[x] >= max:
                max = diff[x]
                ind = x
    for i in range(0,3):
        if starts[i] <= i and fins[i] >= i:
            removal = 0
            if diff[ind] > Sch[i][x]:
                if need > Sch[i][x]:
                    removal = Sch[i][x]
                else:
                    removal = need
            else:
                if need > diff[ind]:
                    removal = diff[ind]
                else:
                    removal = need
            diff[ind] -= removal
            diff[dest] += removal
            Sch[i][dest] += removal
            Sch[i][x] -= removal
            if diff[dest] == 0:
                return()
initSch()
for x in range(0,7):
    if diff[x] < 0:
        displaceinto(x)                
                    
            
print ('DONE')
print (aSch)
print (bSch)
print (cSch)
print (tempTimes)

"""
for t in times:
    total = total+t
    
total = total / 7
division = 0
multiplicity = [0,0,0]
for i in range(0,7):
    
    division = 0
    for j in range(0,3):
        multiplicity[j] = 0
        
        if starts[j] <= i and fins[j] >= i:
            division = division + tempTimes[j]
            multiplicity[j] = tempTimes[j]
    multi = [0,0,0]
    
    multi = [total * t / division for t in multiplicity]
    aSch[i] = multi[0]
    bSch[i] = multi[1]
    cSch[i] = multi[2]
    for j in range(0,3):
        tempTimes[j] = tempTimes[j] - multi[j]

"""
