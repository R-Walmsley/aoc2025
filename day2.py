import numpy as np 

# READ DATA
ftest = open("data/day2.txt",  "r")
x = ftest.readline()
xvals = x.split(",")
allvals = []
for elt in xvals: 
    elts = [int(val) for val in elt.split("-")]
    allvals += [x for x in range(elts[0], elts[1] + 1)]

# Quickly eliminate anything with just 1 of any digit in
for i in range(0, 10): 
    allvals = [x for x in allvals if str(x).count(str(i)) != 1]

# PART ONE
badvals = 0
for val in allvals: 
    str_length = len(str(val))
    # take out all of uneven length
    if str_length % 2 == 1:
        continue
    first_half = str(val)[0:int((str_length/2))]
    second_half =  str(val)[int((str_length/2)):str_length]
    if first_half == second_half: 
        badvals += val
        
        
# PART TWO
badvals = []
for val in allvals:
    str_length = len(str(val))
    for substr_length in range(1, 1+int(np.floor((str_length)/2))):
        if str_length % substr_length == 0: 
            substrs = [str(val)[i:(i+substr_length)] for i in range(0, str_length, substr_length)]
            if len(set(substrs)) == 1: 
                badvals += [val]
                
sum(set(badvals))

