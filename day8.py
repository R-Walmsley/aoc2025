fileloc = "data/day8.txt"
f = open(fileloc, "r")

vals = []
for x in f: 
    split = [int(a) for a in x.split(",")]
    vals += [split]

dists = []
for i in range(len(vals)): 
    for j in range(len(vals)):
        if j > i: 
            vali = vals[i]
            valj = vals[j]
            dist = ((vali[0]-valj[0])**2 + (vali[1]-valj[1])**2 + (vali[2]-valj[2])**2)**(1/2)
            dists += [((i, j), dist)]

sorted_dists = sorted(dists, key = lambda x: x[1])
n_additions = 10
joining_dists = [x[0] for x in sorted_dists[:n_additions]]

groups = [set(joining_dists[0])]
for i in range(1, n_additions): 
    current_val = joining_dists[i]
    j_group = None
    k_group = None
    
    # Find which groups overlap with
    for j in range(len(groups)): 
        if groups[j] is not None: 
            if current_val[0] in groups[j]: 
                j_group = j
    for k in range(len(groups)): 
        if groups[k] is not None: 
            if current_val[1] in groups[k]: 
                k_group = k
            
    # Dp different cases for joining     
    if (k_group is None) and (j_group is None): 
        groups += [set(current_val)]
    if k_group is not None: 
        if j_group is not None: 
            if j_group != k_group: 
                groups[k_group] = groups[j_group].union(groups[k_group])
                groups[j_group] = None
        groups[k_group] = groups[k_group].union(set(current_val))
    if (k_group is None) and (j_group is not None): 
        groups[j_group] = groups[j_group].union(set(current_val))
                
set_descs = sorted([(len(x), x) for x in groups if x is not None], key = lambda x: x[0], reverse=True)
set_descs[0][0]*set_descs[1][0]*set_descs[2][0]

# PART TWO
further_dists = [x[0] for x in sorted_dists[n_additions:]] 
for current_val in further_dists: 
    j_group = None
    k_group = None
    
    # Find which groups overlap with
    for j in range(len(groups)): 
        if groups[j] is not None: 
            if current_val[0] in groups[j]: 
                j_group = j
    for k in range(len(groups)): 
        if groups[k] is not None: 
            if current_val[1] in groups[k]: 
                k_group = k
            
    # Dp different cases for joining     
    if (k_group is None) and (j_group is None): 
        groups += [set(current_val)]
    if k_group is not None: 
        if j_group is not None: 
            if j_group != k_group: 
                groups[k_group] = groups[j_group].union(groups[k_group])
                groups[j_group] = None
        groups[k_group] = groups[k_group].union(set(current_val))
    if (k_group is None) and (j_group is not None): 
        groups[j_group] = groups[j_group].union(set(current_val))
    
    non_none_groups = [x for x in groups if x is not None]
    if (len(non_none_groups) == 1) and (len(non_none_groups[0]) == len(vals)): 
        print(vals[current_val[0]][0]*vals[current_val[1]][0])
        break 