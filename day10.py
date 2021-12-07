from typing import List


def get_data(filename):
    with open(filename) as f:
        return [int(ele) for ele in f]

   
RAW = [int(ele) for ele in """28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3""".splitlines()]

def f1(data : List[int])->int:
    Counter = {i : 0 for i in range(4)}
    data = sorted(data)
    
    for idx in range(1, len(data) ):
        Counter[data[idx] - data[idx-1]] += 1
        
    return Counter[1] * (Counter[3] + 1)
    
 
def find_number(adapter, data, HT):
    
    num = 0
        
    if adapter in HT:
        return HT[adapter]
    
    if len(data) <= 1:
        return 1
    
    for idx in range(3):
        if adapter < data[idx] <= adapter + 3:
            num += find_number(data[idx], data[idx+1:], HT)
        else:
            break
        
    HT[adapter] = num
            
    return num
    
    
           
def f2(data : List[int])->int:
    data = sorted(data)
    data.append(data[-1]+3)
    
    S = 0
    HT = dict()
    for idx in range(3):
        if data[idx] <= 3:
            S += find_number(data[idx], data[idx+1:], HT)
            
    return S
    
    
            
        



            
if __name__ == "__main__":
    data = get_data("Data\data10.txt")
    print(f"Puzzle1: {f1(RAW)}")
    print(f"Puzzle2: {f2(data)}")