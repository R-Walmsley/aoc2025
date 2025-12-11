fileloc = "data/day9.txt"
f = open(fileloc, "r")

vals = []
for x in f: 
    split = [int(a) for a in x.split(",")]
    vals += [split]

# PART ONE 
areas = []
for i in range(len(vals)): 
    for j in range(i+1, len(vals)):
        vali = vals[i]
        valj = vals[j]
        len_ax1 = abs(vali[0] - valj[0]) + 1
        len_ax2 = abs(vali[1] - valj[1]) + 1
        areas += [[(i, j), len_ax1*len_ax2]]

sorted_areas = sorted(areas, key = lambda x: x[1])
indices = [x[0] for x in sorted_areas][::-1]

# PART TWO 
# This is a bit slow! Need a better idea... 
# Think would be refactoring to not use whole shape boundary coordinate wise
# but just check segments
shape_boundary = [vals[0]]
for nextval in vals[1:] + [vals[0]]: 
    currentval = shape_boundary[len(shape_boundary)-1]
    if currentval[0] == nextval[0]: 
        if currentval[1] < nextval[1]:
            shape_boundary += [[currentval[0], i] for i in range(currentval[1]+1, nextval[1])] + [nextval]
        else:
            shape_boundary += [currentval] + [[currentval[0], i] for i in range(nextval[1], currentval[1])][::-1]
    if currentval[1] == nextval[1]: 
        if currentval[0] < nextval[0]: 
            shape_boundary += [[i, currentval[1]] for i in range(currentval[0]+1, nextval[0])] + [nextval]
        else: 
            shape_boundary += [currentval] + [[i, currentval[1]] for i in range(nextval[0], currentval[0])][::-1]

def check_val_in_axes(val, vali, valj): 
    minval_ax0 = min([vali[0], valj[0]])
    maxval_ax0 = max([vali[0], valj[0]])
    minval_ax1 = min([vali[1], valj[1]])
    maxval_ax1 = max([vali[1], valj[1]])
    if (val[0] > minval_ax0) and (val[0] < maxval_ax0): 
        if (val[1] > minval_ax1) and (val[1] < maxval_ax1): 
            return True
    return False
            

for (i,j) in indices: 
    print((i, j))
    vali = vals[i]
    valj = vals[j]
    pure = True
    for val in shape_boundary:
        if check_val_in_axes(val, vali, valj): 
            pure = False
            break
    if pure: 
        len_ax1 = abs(vali[0] - valj[0]) + 1
        len_ax2 = abs(vali[1] - valj[1]) + 1
        print(len_ax1*len_ax2)
        break 
