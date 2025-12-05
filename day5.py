import re 

fileloc = "data/day5.txt"
f = open(fileloc,  "r")

vals = []
foods = []
for x in f: 
    if "-" in x:
        print(x)
        input = x.split("-")
        vals += [(int(input[0]), int(input[1].rstrip()))] # rstrip strips newline
    if re.match("^[0-9]+$", x): 
        foods += [int(x.rstrip())] 
 
# PART ONE 
count = 0       
for food in foods: 
    for range_i in vals: 
        if (food >= range_i[0]) and (food <= range_i[1]): 
            count += 1
            break

# PART TWO 
# the issue is overlapping ranges
# and the real issue is memory if 
# we start unpacking everything 
# so we need to get continuous ranges
# efficiently
vals = sorted(vals, key = lambda x: x[0])
# vals sorted on first element    
cleaned_vals = [vals[0]]
for j in range(1, len(vals)): 
    lower = vals[j][0]
    upper = vals[j][1]
    overlaps = False
    range_i = cleaned_vals[len(cleaned_vals)-1]
    if lower <= range_i[1]:
        overlaps = True
        if upper > range_i[1]: 
            cleaned_vals[len(cleaned_vals)-1] = (range_i[0], upper)
    if not overlaps: 
        cleaned_vals += [(lower, upper)]

count = 0
for val in cleaned_vals: 
    count += val[1] - val[0] + 1
