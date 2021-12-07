from typing import List


def get_data(filename):
    with open(filename) as f:
        return [ele.replace("\n","") for ele in f]


def f1(data : List[int])->int:
    IDS = []
    for ele in data:
        row = int(ele[:7].replace("B","1").replace("F","0"),2)
        col = int(ele[-3:].replace("R","1").replace("L","0"),2)
        IDS.append(row*8+col)
    return max(IDS)


def f2(data : List[int])->int:
    HT = []
    print(len(data))
    for ele in data:
        row = int(ele[:7].replace("B","1").replace("F","0"),2)
        col = int(ele[-3:].replace("R","1").replace("L","0"),2)
        HT.append(row*8+col)
        
    for row in range(1,126):
        for col in range(8):
            ID = row*8+col
        
            if (ID not in HT) and (ID-1 in HT) and (ID+1 in HT):
                return ID




            
if __name__ == "__main__":
    data = get_data("Data\data5.txt")
    print(f"Puzzle1: {f1(data)}")
    print(f"Puzzle2: {f2(data)}")