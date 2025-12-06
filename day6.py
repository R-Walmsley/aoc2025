import numpy as np
fileloc = "data/day6.txt"
f = open(fileloc, "r")

# Read input
mat = []
for x in f: 
    nums = x.split()
    if ("+" in nums) or ("*" in nums): 
        continue
    mat += [[int(a) for a in nums]]
    
mat = np.matrix(mat, dtype=object) # object datatype to 
# avoid np coercion which leads to overflow issues
# See: https://stackoverflow.com/questions/70349371/how-to-deal-with-large-integers-in-numpy

# PART ONE ----------------------
total = 0
for i in range(len(nums)):
    val = nums[i]
     
    if val == "+": 
        total += np.sum(mat[:, i])
    if val == "*": 
        total += np.prod(mat[:, i])
        
# PART TWO --------------------
# Reread input as now alignment matters
mat = np.genfromtxt(fileloc, delimiter=1, dtype=object)
mat = mat.astype(str)

index_row = mat[mat.shape[0]-1, :]
rest_of_mat = mat[0:mat.shape[0]-1, :]
nums = [rest_of_mat[:, j] for j in range(rest_of_mat.shape[1])]
nums_collapsed = [''.join(x.tolist()) for x in nums]

total = 0
count = 0
operation = None
for i in range(len(index_row)):
    if index_row[i] != " ":
        print(count)
        total += count
        count = int(nums_collapsed[i])
        if index_row[i] == "*": 
            operation = "product"
        if index_row[i] == "+": 
            operation = "sum"
    else: 
        if not nums_collapsed[i].isspace(): 
            if operation == "product":    
                count = count*int(nums_collapsed[i])
            if operation == "sum": 
                count += int(nums_collapsed[i])
                
total += count