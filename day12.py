from typing import List
import numpy as np

def get_data(filename):
    with open(filename) as f:
        return [ele.replace("\n","") for ele in f]

RAW = """F10
N3
F7
R90
F11""".splitlines()

class Ship():
    def __init__(self):
        self.pos = np.array([0,0])
        self.angle = 0
        
    def command(self, com, val):
        if com in ["N", "S", "W", "E"]:
            self.move_dir(com, val)
        elif com in ["L", "R"]:
            self.change_angle(com, val)
        elif com == "F":
            self.move_forward(val)
        else:
            assert False
            
        
    def move_dir(self, dir, val):
        if dir == "N": self.pos[1] += val
        if dir == "S": self.pos[1] -= val
        if dir == "W": self.pos[0] -= val
        if dir == "E": self.pos[0] += val
        
    def move_forward(self, val):
     
        self.pos[0] += int(np.cos(self.angle * 2 * np.pi / 360) * val)
        self.pos[1] += int(np.sin(self.angle * 2 * np.pi / 360) * val)
        
        
    def change_angle(self, dir, val):
        if dir == "L": self.angle += val
        if dir == "R": self.angle -= val
        
        self.angle = self.angle % 360
        
        
        
def f1(data : List[int])->int:
    ship = Ship()
    for line in data:
        com = line[0]
        val = int(line[1:])
        ship.command(com, val)
        
    return abs(ship.pos[0]) + abs(ship.pos[1])
           
           
           
class Ship2():
    def __init__(self):
        self.pos = np.array([0,0])
        self.wp = np.array([10,1])
        self.angle = 0
        
    def command(self, com, val):
        if com in ["N", "S", "W", "E"]:
            self.move_dir(com, val)
        elif com in ["L", "R"]:
            self.change_angle(com, val)
        elif com == "F":
            self.move_forward(val)
        else:
            assert False
        
    def move_dir(self, dir, val):
        if dir == "N": self.wp[1] += val
        if dir == "S": self.wp[1] -= val
        if dir == "W": self.wp[0] -= val
        if dir == "E": self.wp[0] += val
        
    def move_forward(self, val):
        
        self.pos += (self.wp) * val
        
        
    def change_angle(self, dir, val):
        if val == 180:
            self.wp = - self.wp
        elif (val == 90 and dir == "L") or (val == 270 and dir == "R"):
            self.wp[0], self.wp[1] = - self.wp[1], self.wp[0]
            
        elif (val == 90 and dir == "R") or (val == 270 and dir == "L"):
            self.wp[0], self.wp[1] =  self.wp[1], - self.wp[0]
        
        
def f2(data : List[int])->int:
    ship = Ship2()
    for line in data:
        com = line[0]
        val = int(line[1:])
        ship.command(com, val)
        
    return abs(ship.pos[0]) + abs(ship.pos[1])
        



            
if __name__ == "__main__":
    data = get_data("Data\data12.txt")
    print(f"Puzzle1: {f1(data)}")
    print(f"Puzzle2: {f2(data)}")