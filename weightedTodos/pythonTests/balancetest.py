starts = [0,1,3]
fins   = [6,5,6]
times  = [7,10,11]
tempTimes = [7,10,11]
total = 0

lengths = [0,0,0]

aSch = [0,0,0,0,0,0,0]
bSch = [0,0,0,0,0,0,0]
cSch = [0,0,0,0,0,0,0]
Sch = [aSch, bSch, cSch]
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
def maximum(d,i):
    m = 0
    dd = 0
    for x in range(0,7):
        if startx[i] <= x and fins[i] >= x:
            if d[x] > m:
                m = d[x]
                dd = x
    return dd

for i in range(0,3):
    lengths[i] = fins[i] - starts[i]
    total = total + times[i]
total = total / 7
diff = [total, total, total, total, total, total, total]


for i in range(0,7):
    for j in range(0,3):
        if starts[j] <= i and fins[j] >= i:
            Sch[j][i] = times[j] / lengths[j]
    for j in range (0,3):
        diff[i] = diff[i] - sch[j][i]

for i in range(0,7):
    while diff[i] < total:
        for j in range(0,3):
            if starts[j] <= i and fins[j] >= i:
                    
            
print ('DONE')
print (aSch)
print (bSch)
print (cSch)
print (tempTimes)
