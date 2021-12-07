from typing import List


def get_data(filename):
    with open(filename) as f:
        return [ele.replace("\n","") for ele in f]

RAW = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.""".splitlines()

def get_HT(data):
    HT = dict()
    RHT = dict()
    for line in data:
        FB, SB = line.split("contain")
        SB = SB.replace(".", "").strip()
        FB = FB.strip()
        FB = FB.replace("bags","").replace("bag","").strip()
        
        if SB == "no other bags":
            SB = {}
        else:
            SB = SB.replace("bags","").replace("bag","").strip()
            SB = { ele[2:].strip() : int(ele[0]) for ele in SB.split(", ")}
            
        for bag in SB:
            if bag not in RHT:
                RHT[bag] = {FB : SB[bag]}
            else:
                RHT[bag].update({FB : SB[bag]})
                 
        HT[FB] = SB
        
    return HT, RHT
        
def count_bag(bag_name : str, HT, RHT, visited = None):
    if visited == None:
        visited = [bag_name]
        
    if bag_name in RHT:
        for bag in RHT[bag_name]:
            if bag not in visited:
                visited.append(bag)
                count_bag(bag, HT, RHT, visited)
                
                
    return len(visited) - 1
                
def count_bag_numbers(bag_name : str, HT, RHT, visited = None):
    if visited == None:
        visited = [bag_name]
    Numbers = 0
   # print(bag_name)
    if bag_name in HT:
        
       # if len(HT[bag_name]) == 0:
       #     return 0
        
        print(bag_name, "Start: \n")
        for bag in HT[bag_name]:
           # if bag not in visited:
            visited.append(bag)
            new = HT[bag_name][bag] * (count_bag_numbers(bag, HT, RHT, visited)+1)
            print(bag_name, ":", bag, ":", new ,"+", Numbers)
            Numbers += new
        return Numbers 
    
    else:
        return 0
                
                
    
    

def f1(data : List[int])->int:
    HT, RHT = get_HT(data)
    return count_bag("shiny gold", HT, RHT)


def f2(data : List[int])->int:
    HT, RHT = get_HT(data)
    return count_bag_numbers("shiny gold", HT, RHT)



            
if __name__ == "__main__":
    data = get_data("Data\data7.txt")
    print(f"Puzzle1: {f1(data)}")
    print(f"Puzzle2: {f2(data)}")