from typing import List


def get_data(filename):
    with open(filename) as f:
        return [ele.replace("\n","") for ele in f]


def f1(data : List[int])->int:
    Sum = 0
    s = ""
    for idx, line in enumerate(data):
        
        if line != "":
            s += line
            
        if line == "" or idx == len(data)-1:
            Sum += len(set(s))
            s = ""
    return Sum


def f2(data : List[int])->int:
    Sum = 0
    s = []
    for idx, line in enumerate(data):
        
        if line != "":
            s.append(set(line))
            
        if line == "" or idx == len(data)-1:
            newSet = s[0]
            for ele in s:
                newSet = newSet.intersection(ele)

            Sum += len(newSet)
            s = []
            
    return Sum




            
if __name__ == "__main__":
    data = get_data("Data\data6.txt")
    print(f"Puzzle1: {f1(data)}")
    print(f"Puzzle2: {f2(data)}")