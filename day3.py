def get_max_in_range(start_index, final_index, ints): 
    running_max = ints[start_index]
    running_index = start_index
    for i in range(start_index+1, final_index+1): 
        if ints[i] > running_max: 
            running_index = i
            running_max = ints[i]
    return running_index, running_max

# Part one and part two are done by controlling nbatteries argument
def calculate_max_joltage(fileloc, nbatteries=2): 
    f = open(fileloc,  "r")
    joltages = []
    for x in f: 
        ints = [int(d) for d in list(str(x)) if d != "\n"]
        joltage = 0
        running_index = -1
        for j in range(1, nbatteries+1):
            running_index, digit_j = get_max_in_range(running_index+1, len(ints) - (nbatteries - j) - 1, ints)
            joltage += digit_j*(10**(nbatteries-j))
        joltages += [joltage]
    return joltages

sum(calculate_max_joltage("data/day3.txt", 12))