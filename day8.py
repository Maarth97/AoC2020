from typing import List


def get_data(filename):
    with open(filename) as f:
        return [ele.replace("\n","") for ele in f]

   
def check_instructions(data, changeIdx = None):
    HT = [0 for _ in data]
    
    idx, acc = 0,0
    while True:
        if idx >= len(data):
            return True, acc
        elif HT[idx] == 1:
            return False, acc
        
        com, val = data[idx].split(" ")
        
        if idx == changeIdx and com == "jmp":
            com = "nop"
        elif idx == changeIdx and com == "nop":
            com = "jmp"
            
        HT[idx] = 1
        
        if com == "acc":
            acc += int(val)
            idx += 1
        elif com == "jmp":
            idx += int(val)
        else:
            idx += 1  

def f1(data : List[int])->int:
    return check_instructions(data)[1]


def f2(data : List[int])->int:
    for idx, line in enumerate(data):
        com, val = line.split(" ")
        
        if com in ["jmp", "nop"]:
            flag, acc = check_instructions(data, idx)
            if flag:
                return acc



            
if __name__ == "__main__":
    data = get_data("Data\data8.txt")
    print(f"Puzzle1: {f1(data)}")
    print(f"Puzzle2: {f2(data)}")