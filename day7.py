import numpy as np
import re

fileloc = "data/day7.txt"
mat = np.genfromtxt(fileloc, delimiter=1, dtype=str)

# PART ONE 
split = 0
for i in range(1, mat.shape[0]): 
    for j in range(mat.shape[1]): 
        if mat[i-1, j] == ".": 
            continue
        if (mat[i-1, j] == "|") or (mat[i-1, j] == "S"): 
            if mat[i, j] == ".": 
                mat[i, j] = "|"
            if mat[i, j] == "^":
                split += 1 
                if j >= 1: 
                    mat[i, j-1] = "|"
                if j < mat.shape[1] - 1: 
                    mat[i, j+1] = "|"

print(split)

# PART TWO 
mat = np.genfromtxt(fileloc, delimiter=1, dtype=str)
mat = mat.astype(object)
for i in range(1, mat.shape[0]): 
    for j in range(mat.shape[1]): 
        if mat[i-1, j] == ".": 
            continue
        if (mat[i-1, j] == "S"): 
            mat[i, j] = "1"
        if (re.match("^[0-9]+$", mat[i-1, j])): 
            if re.match( "^[0-9]+$", mat[i, j]): 
                mat[i, j] = str(int(mat[i, j]) + int(mat[i-1, j]))
            if mat[i, j] == ".": 
                mat[i, j] = str(int(mat[i-1, j]))
            if mat[i, j] == "^":
                if j >= 1: 
                    if re.match("^[0-9]+$", mat[i, j-1]): 
                        mat[i, j-1] = str(int(mat[i, j-1]) + int(mat[i-1, j]))
                    else: 
                        mat[i, j-1] = str(int(mat[i-1, j]))
                if j < mat.shape[1] - 1: 
                    if re.match( "^[0-9]+$", mat[i, j+1]): 
                        mat[i, j+1] =  str(int(mat[i, j+1]) + int(mat[i-1, j]))
                    else: 
                        mat[i, j+1] = str(int(mat[i-1, j]))

sum([int(x) for x in mat[mat.shape[0]-1, :] if x != "."])      



