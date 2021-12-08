from typing import List
import numpy as np

def get_data(filename):
    with open(filename) as f:
        return [ele.replace("\n","") for ele in f]


RAW = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL""".splitlines()

def init_board(data):
    M = len(data) + 2
    N = len(data[0]) + 2
    
    board = np.zeros((M,N))
    
    for row in range(1, M-1):
        for col in range(1, N-1):
            if data[row-1][col-1] == "L":
                board[row, col] = 1
            elif data[row-1][col-1] == "#":
                board[row, col] = 2
            else:
                board[row, col] = 0
                
    return board

def check_board(board, row, col):
    pos = [(-1,-1),(-1,0), (-1,1) , (0, -1), (0,1) , (1,-1), (1,0), (1,1)]
    
    S = sum([1  for r,c in pos if board[r+row,c+col] == 2])
    return S

def rules(board, M, N):
    new_board = np.zeros(board.shape)
    
    for row in range(1, M-1):
        for col in range(1, N-1):
            # --> Occupied if empty and other placed empty
            if board[row, col] == 1 and check_board(board, row, col) == 0:
                new_board[row, col]  = 2
                
            elif board[row, col] == 2 and check_board(board, row, col) >= 4:
                new_board[row, col]  = 1
            
            else:
                new_board[row, col] = board[row, col]
                
    return new_board
    

def f1(data : List[int])->int:
    M = len(data) + 2
    N = len(data[0]) + 2
    
    initial_board = init_board(data)
    actual_board = np.array(initial_board)
    
    while True:

        new_board = rules(actual_board,M,N)
        
        if (new_board == actual_board).all():
            break
        else:
            actual_board = np.array(new_board)
        
    
    return len(new_board[new_board == 2])
    
    
def check_board2(board, row, col, M, N):
    S = 0
    pos = [(-1,-1),(-1,0), (-1,1) , (0, -1), (0,1) , (1,-1), (1,0), (1,1)]
    
    for r,c in pos:
        step = 0
        seat = 0
        while True:
            step +=1
            
            
            if row + r*step  < 0 or row + r*step >= M or col+c*step < 0 or col + c*step >= N:
                break
            # Check seat
           # print(f"{seat}: {row,col}, : {col + c *step}, {N,M}")
            seat =  board[row + r *step, col + c * step]
            
            if seat in [1,2]:
                
                break
            
           # print(row + r *step, col + c *step)
        S += int(seat == 2)
        
     
    return S

def rules2(board, M, N):
    new_board = np.zeros(board.shape)
    
    for row in range(1, M-1):
        for col in range(1, N-1):
            # --> Occupied if empty and other placed empty
            if board[row, col] == 1 and check_board2(board, row, col,M,N) == 0:
                new_board[row, col]  = 2
                
            elif board[row, col] == 2 and check_board2(board, row, col,M,N) >= 5:
                new_board[row, col]  = 1
            
            else:
                new_board[row, col] = board[row, col]
                
    return new_board
           
def f2(data : List[int])->int:
    M = len(data) + 2
    N = len(data[0]) + 2
    
    initial_board = init_board(data)
    actual_board = np.array(initial_board)
    
    while True:

        new_board = rules2(actual_board,M,N)
        
        if (new_board == actual_board).all():
            break
        else:
            actual_board = np.array(new_board)
        
    
    return len(new_board[new_board == 2])
        



            
if __name__ == "__main__":
    data = get_data("Data\data11.txt")
    #print(f"Puzzle1: {f1(data)}")
    print(f"Puzzle2: {f2(data)}")