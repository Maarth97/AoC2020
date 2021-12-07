from typing import List
import numpy as np
from collections import Counter

def get_data(filename):
    with open(filename) as f:
        return [i for i in f]

def f1(data : List[int])->int:
    # Count Valid Passwords
    cnt = 0
    for pw in data:
        schema = pw.split(" ")
        letter = schema[1][0]
        minV, maxV = [int(ele) for ele in schema[0].split("-")]
        
        # Check if password is valid
        if minV <= Counter(schema[2])[letter] <= maxV:
            cnt += 1
    return cnt

def f2(data : List[int])->int:
    # Count Valid Passwords
    cnt = 0
    for pw in data:
        schema = pw.split(" ")
        letter = schema[1][0]
        minV, maxV = [int(ele)-1 for ele in schema[0].split("-")]
        
        # Check if password is valid
        if (schema[2][minV] == letter) and not (schema[2][maxV] == letter):
            cnt += 1
        elif not (schema[2][minV] == letter) and (schema[2][maxV] == letter):
            cnt += 1
    return cnt
            
if __name__ == "__main__":
    data = get_data("Data\data2.txt")
    print(f"Puzzle1: {f1(data)}")
    print(f"Puzzle1: {f2(data)}")