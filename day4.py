import numpy as np
file = "data/day4.txt"

# Set up data and functions
mat = np.genfromtxt(file, delimiter=1, dtype=str, comments=None)

def check_loc_in_grid(next_loc, mat=mat):
    if next_loc[0] < 0:
        return False
    if next_loc[0] >= mat.shape[0]:
        return False
    if next_loc[1] < 0:
        return False
    if next_loc[1] >= mat.shape[1]:
        return False
    return True

def get_adj_vals(loc):
    cands = [
        (loc[0], loc[1] + 1),
        (loc[0], loc[1] - 1),
        (loc[0] + 1, loc[1]),
        (loc[0] - 1, loc[1]),
        (loc[0] + 1, loc[1] + 1),
        (loc[0] - 1, loc[1] - 1),
        (loc[0] + 1, loc[1] - 1),
        (loc[0] - 1, loc[1] + 1),
        
    ]
    return [x for x in cands if check_loc_in_grid(x)]

# PART 1
accessible_paper = 0
for i in range(mat.shape[0]):
    for j in range(mat.shape[1]): 
        print(mat[i, j])
        if mat[i, j] == "@": 
            cand_vals = get_adj_vals((i, j))
            count_paper = 0
            for val in cand_vals: 
                if mat[val[0], val[1]] == "@": 
                    count_paper += 1
            if count_paper < 4: 
                accessible_paper +=1 
                vals_to_change += [(i, j)]
                
# PART TWO 
vals_to_change = ["starting"]
accessible_paper = 0

while len(vals_to_change) > 0: 
    vals_to_change = []   
    for i in range(mat.shape[0]):
        for j in range(mat.shape[1]): 
            print(mat[i, j])
            if mat[i, j] == "@": 
                cand_vals = get_adj_vals((i, j))
                count_paper = 0
                for val in cand_vals: 
                    if mat[val[0], val[1]] == "@": 
                        count_paper += 1
                if count_paper < 4: 
                    accessible_paper +=1 
                    vals_to_change += [(i, j)]
    for val in vals_to_change: 
        mat[val[0], val[1]] = "."