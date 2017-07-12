#simple PERT projection
#with givn weekly inputs
import math

weeks_left  = 25
week_invest = 50
init        = 1170
rates       = [0.00, 0.001, 0.002, 0.003, 0.004]
gains       = [init,  init,  init,  init, init]

for i in range(0,weeks_left):
	ind = 0
	for r in rates:
		t = gains[ind] + week_invest
		gains[ind] = t*math.exp(r * 5)
		ind = ind + 1

print (gains)
ind = 0
growth = [0.0, 0.0, 0.0, 0.0, 0.0]
for g in gains:
	gains[ind] = g - ((week_invest*weeks_left) + init)
	growth[ind] = gains[ind] / ((week_invest*weeks_left) + init)
	ind = ind + 1

print (gains)
print (growth)