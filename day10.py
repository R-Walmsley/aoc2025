import numpy as np
from scipy.optimize import milp
from scipy.optimize import LinearConstraint


from itertools import product
import datetime
now = datetime.datetime.now()
fileloc = "data/day10.txt"
f = open(fileloc, "r")

# PART ONE --------------------------------
# This is sort of a constrained integer programming problem 
# except where the solution is modulo 2 
# or Ax = ref + 2n * (vector of 1s)
# Where A is the battery matrix 
# However, always 2 presses of any button is same as 0 
# so we actually only need to check the 1s and 0s
# So we can just manually check everything
totalminsum = 0
for x in f: 
    vals = x.split(" ")
    target = vals[0]
    target = np.array([int(a) for a in list(target.replace('[', '').replace(']', '').replace('.', '0').replace('#', '1'))])
    batteries = vals[1:(len(vals)-1)]
    battery_matrix = np.zeros((len(target), len(batteries)))
    for j in range(len(batteries)):
        battery = batteries[j] 
        battery_vals = [int(a) for a in list(battery.replace("(", "").replace(")", "").split(","))]
        for i in battery_vals: 
            battery_matrix[(i, j)] = 1
    battery_matrix_reduced = 
    candidates = [np.array(x) for x in product(range(0, 2), repeat=len(batteries))]
    minsum = len(batteries)
    for candidate in candidates: 
        res = np.matmul(battery_matrix, candidate)
        if (res % 2 == target.transpose()).all(): 
            minsum = min([minsum, sum(candidate)])
    totalminsum += minsum
    
    
# PART TWO --------------------------------
# Now this is actually the constrained integer programming 
# Solve Ax = b minimising x 
fileloc = "data/day10.txt"
f = open(fileloc, "r")
countrows = 0
totalminsum = 0
for row in f: 
    print(countrows)
    countrows += 1
    vals = row.split(" ")
    target = vals[len(vals)-1]
    target = np.array([int(a) for a in target.replace('{', '').replace('}', '').split(',')])
    batteries = vals[1:(len(vals)-1)]
    battery_matrix = np.zeros((len(target), len(batteries)))
    for j in range(len(batteries)):
        battery = batteries[j] 
        battery_vals = [int(a) for a in battery.replace("(", "").replace(")", "").split(",")]
        for i in battery_vals: 
            battery_matrix[(i, j)] = 1
    c = np.ones(len(batteries))
    constraints = LinearConstraint(battery_matrix, target, target)        
    res = milp(c=c, constraints=constraints, integrality=np.ones_like(c))
    totalminsum += sum(res.x)
    