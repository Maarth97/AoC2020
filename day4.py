from typing import List


def get_data(filename):
    with open(filename) as f:
        return [i[:-1].strip() for i in f]

def f1(data : List[int])->int:
    # Count Valid passboards
    cnt = 0
    PB = dict()
    keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    for idx, line in enumerate(data):
        
        
        if line != "":
            PBline = line.split(" ")
            PBline = [ele.split(":") for ele in PBline]
            PB.update({key : value for key, value in PBline})
            
        if line == "" or (idx == len(data)-1):
            # Check
            cnt += int( all([(key in PB) for key in keys])) 
            # Update new
            PB = dict()
            
    return cnt
    

def f2(data : List[int])->int:
    # Count Valid passboards
    cnt = 0

    
    PB = dict()
    keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    for idx, line in enumerate(data):
        
        if line != "":
            PBline = line.split(" ")
            PBline = [ele.split(":") for ele in PBline]
            PB.update({key : value for key, value in PBline})
            
        if line == "" or (idx == len(data)-1):
            
            if int( all([(key in PB) for key in keys])) and \
                1920 <= int(PB["byr"]) <= 2002 and \
                2010 <= int(PB["iyr"]) <= 2020 and \
                2020 <= int(PB["eyr"]) <= 2030 and \
                (( PB["hgt"][-2:] == "cm" and 150 <= int(PB["hgt"][:-2]) <= 193) or \
                ( PB["hgt"][-2:] == "in" and 59 <= int(PB["hgt"][:-2]) <= 76)) and \
                PB["hcl"][0] == "#" and \
                len(PB["hcl"]) == 7 and \
                all([True if ele in "abcdef0123456789" else False for ele in PB["hcl"][1:]]) and \
                (PB["ecl"] in ["amb","blu" ,"brn", "gry", "grn", "hzl", "oth"]) and \
                len(PB["pid"]) == 9 and \
                all([True if ele in "0123456789" else False for ele in PB["pid"]]):
                    cnt += 1
                    
            PB = dict()

    return cnt
    
            
if __name__ == "__main__":
    data = get_data("Data\data4.txt")
    print(f"Puzzle1: {f1(data)}")
    print(f"Puzzle2: {f2(data)}")