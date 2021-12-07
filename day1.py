from typing import List
import numpy as np

def get_data(filename):
    with open(filename) as f:
        return [int(i) for i in f]

def f1(data : List[int])->int:
    # Find 2 Entries that sum up to 2020
    
    for ele in data:
        if (2020-ele) in data:
            return ele * (2020-ele)

def f2(data : List[int])->int:
    # Find 3 Entries that sum up to 2020
    
    for idx1, ele in enumerate(data):
        for idx2, ele2 in enumerate(data):
            if idx1 == idx2:
                continue
            
            if (2020-ele-ele2) in data:
                return ele * ele2 * (2020-ele-ele2)
            
if __name__ == "__main__":
    data = get_data("Data\data1.txt")
    print(f"Puzzle1: {f1(data)}")
    print(f"Puzzle1: {f2(data)}")