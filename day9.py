from typing import List


def get_data(filename):
    with open(filename) as f:
        return [int(ele) for ele in f]

   


def f1(data : List[int])->int:
    HT = dict()
    
    for idx, ele in enumerate(data):
        
        if idx >= 25:
            if not any([ ele - summ1 in HT and HT[ele-summ1] >= idx-25 for summ1 in data[idx-25:idx]]):
                return ele
                
        HT[ele] = idx
        
def f2(data : List[int], find_num = 393911906)->int:
    min_idx, max_idx = 0,1
    
    while True:
        S = sum(data[min_idx : max_idx+1])
        
        if S == find_num and min_idx != max_idx:
            return min(data[min_idx : max_idx+1]) + max(data[min_idx : max_idx+1])
        
        elif S > find_num:
            min_idx += 1
            
        elif S <= find_num:
            max_idx += 1
            
            
        



            
if __name__ == "__main__":
    data = get_data("Data\data9.txt")
    print(f"Puzzle1: {f1(data)}")
    print(f"Puzzle2: {f2(data)}")