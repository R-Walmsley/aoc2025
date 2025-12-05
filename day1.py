import numpy as np

# PART ONE -----------------------------
def parse_instruction(string): 
    letter = string[0]
    number = np.float64(string[1:])
    if letter == "L": 
        return 100 - number
    if letter == "R": 
        return number

def calculate_number_of_zeroes(fileloc): 
    f = open(fileloc,  "r")
    count_zero = 0
    start_count = 50
    for x in f: 
        start_count += parse_instruction(x)
        if start_count % 100 == 0: 
            count_zero += 1
    return count_zero

calculate_number_of_zeroes("data/day1test.txt") 
number_of_zeroes = calculate_number_of_zeroes("data/day1.txt") 

# PART TWO ---------------------------
def parse_instruction_parttwo(current_loc, string): 
    letter = string[0]
    number = np.float64(string[1:])
    if letter == "L": 
        current_loc_complement = (100 - current_loc) % 100
        zeroes = np.floor((current_loc_complement + number)/100)
        current_loc = (current_loc - number) % 100
    if letter == "R": 
        zeroes = np.floor((current_loc + number)/100)
        current_loc = (current_loc + number) % 100
    return zeroes, current_loc


def calculate_number_of_zeroes_parttwo(fileloc): 
    f = open(fileloc,  "r")
    count_zero = 0
    current_loc = 50
    for x in f:
        zeroes, current_loc = parse_instruction_parttwo(current_loc, x)
        count_zero += zeroes
    return count_zero

calculate_number_of_zeroes_parttwo("data/day1test.txt")
calculate_number_of_zeroes_parttwo("data/day1.txt")