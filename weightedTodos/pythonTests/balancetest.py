import time
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
diff = [total-1, total-1, total, total, total+2, total+1, total-1]

def initSch():
    for i in range(0,3):
        lengths[i] = fins[i] - starts[i]
        lengths[i] += 1
        for x in range(starts[i], fins[i]+1):
            Sch[i][x] = times[i] / lengths[i]
    for x in range(0, 7):
        for i in range(0, 3):
            diff[x] += Sch[i][x]

def miniumDiff():
    m = diff[0]
    for x in range(1,7):
        if diff[x] <= m:
            m = diff[x]
    return m
            
def displaceinto(dest):
    maxx = diff[dest]
    need = -maxx
    ind = dest
    for x in range(0,7):
        if x != dest:
            if diff[x] >= maxx:
                maxx = diff[x]
                ind = x
    while diff[dest] != 0:
        for i in range(0,3):
            maxx = miniumDiff()
            ind = -1
            for x in range(0,7):
                if x != dest:
                    if diff[x] >= maxx:
                        if starts[i] <= x and fins[i] >= x and Sch[i][x] > 0:
                            maxx = diff[x]
                            ind = x
                        
            if starts[i] <= dest and fins[i] >= dest and starts[i] <= ind and fins[i] >= ind:
                removal = 0
                
                if Sch[i][ind] <= 0:
                    continue
                #if 1 or diff[ind] > Sch[i][ind]:
                if need > Sch[i][ind]:
                    removal = Sch[i][ind]
                else:
                    removal = need
                '''else:
                if need > diff[ind]:
                    removal = diff[ind]
                else:
                    removal = need'''
                diff[ind] -= removal
                diff[dest] += removal
                Sch[i][dest] += removal
                Sch[i][ind] -= removal
                need = -diff[dest]
                
                displayNewSch(i, dest, ind)
                if diff[dest] == 0:
                    return()

def displayNewSch(u, d, i):
    print("todo-", u , "\tdest-" , d ,"\tfrom-" , i)
    for i in range(0,3):
        for x in range(0,7):
            print(Sch[i][x], end='\t')
        print()
    print('---------------------------------------------------------')
    for x in range(0,7):
        print(diff[x], end='\t')
    print('\n=========================================================')
    time.sleep(1)
    
initSch()
displayNewSch(1,1,1)
for y in range(0,20):
    for x in range(0,7):
        if diff[x] < 0:
            displaceinto(x)
            
            

    
            
print ('DONE')
displayNewSch(-1,-1,-1)
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
