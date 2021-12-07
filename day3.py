from typing import List


def get_data(filename):
    with open(filename) as f:
        return [i[:-1] for i in f]

def f1(data : List[int], dy= 1, dx = 3)->int:
    # how many trees
    cnt_trees = 1 if data[0][0] == "#" else 0
    x,y = 0,0
    N = len(data[0])
    
    while y < len(data):
        # Check for Tree
        cnt_trees = cnt_trees + 1 if data[y][x % N] == "#" else cnt_trees
            
            
        # Nex Pos
        y += dy
        x += dx
    return cnt_trees

def f2(data : List[int])->int:
    # Multiplication of different Slopes
    res = 1
    
    N = len(data[0])
    
    slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]
    for dx, dy in slopes:
        res *= f1(data, dy, dx)
    return res
    
            
if __name__ == "__main__":
    data = get_data("Data\data3.txt")
    print(f"Puzzle1: {f1(data)}")
    print(f"Puzzle1: {f2(data)}")