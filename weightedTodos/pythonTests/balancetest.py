import time
starts = [0,1,3]
fins   = [6,5,6]
times  = [7,10,11]
tempTimes = [7,10,11]
total = 28
soonestFinish = [0,1,2]
lengths = [0,0,0]

aSch = [0,0,0,0,0,0,0]
bSch = [0,0,0,0,0,0,0]
cSch = [0,0,0,0,0,0,0]
Sch = [aSch, bSch, cSch]
total /= 7
diff = [total-1, total-1, total+1, total+1, total+2, total+1, total-3]
def PossibleSchedule():
    ts = diff[0]
    for i in range(0,3):
        ds = 1 + fins[i] - starts[i]
        if times[i]/ds > ts:
            return(0)
    return(1)
        
        
def isNow(td, da):
    return (starts[td] <= da and fins[td] >= da)
        
def displaceinto(curr, left, tots):
    if curr >= 7:
        return()
    
    tempTotal = tots
    change = [1,1,1]
    addin = [0,0,0]
    st = diff[curr]
    for i in range(0,3):        
        if not isNow(i, curr):
            tempTotal -= left[i]
            change[i] = 0
    for i in soonestFinish:
        if not change[i] or left[i] <= 0:
            continue
        if st <= left[i]:
            addin[i] = st
            left[i] -= st
            tots -= st
            break
        st -= left[i]
        addin[i] = left[i]
        tots -= left[i]
        left[i] = 0
    for i in range(0,3):
        Sch[i][curr] = addin[i]
    
    
    displaceinto(curr+1, left, tots)


def displayNewSch(u, d, i):
    for i in range(0,3):
        for x in range(0,7):
            print(Sch[i][x], end='\t')
        print()
    print('---------------------------------------------------------')
    time.sleep(1)
    
#displayNewSch(1,1,1)
print("Possible Schedule:",PossibleSchedule())
displaceinto(0, times, total)
            
displayNewSch(-1,-1,-1)
for i in range(0,3):
    te = 0
    for x in range(0,7):
        te += Sch[i][x]
    print(te, end='\t')
print()
