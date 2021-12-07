import unittest
import day1
import day2
import day3
import day4

class Test_Day1(unittest.TestCase):
    
    def test_f1(self):
        inp = [1721,979,366,299,675,1456]
        self.assertEqual(day1.f1(inp), 514579)
    
    def test_f2(self):
        inp = [1721,979,366,299,675,1456]
        self.assertEqual(day1.f2(inp), 241861950)
        

class Test_Day2(unittest.TestCase):
    
    def test_f1(self):
        inp = ["1-3 a: abcde",
                "1-3 b: cdefg",
                "2-9 c: ccccccccc"]
        self.assertEqual(day2.f1(inp), 2)
    
    def test_f2(self):
        inp = ["1-3 a: abcde",
                "1-3 b: cdefg",
                "2-9 c: ccccccccc"]
        self.assertEqual(day2.f2(inp), 1)
        
class Test_Day3(unittest.TestCase):
    
    def test_f1(self):
        inp = ["..##.......",
                "#...#...#..",
                ".#....#..#.",
                "..#.#...#.#",
                ".#...##..#.",
                "..#.##.....",
                ".#.#.#....#",
                ".#........#",
                "#.##...#...",
                "#...##....#",
                ".#..#...#.#"]
        
        self.assertEqual(day3.f1(inp), 7)
    
    def test_f2(self):
        inp = ["..##.......",
                "#...#...#..",
                ".#....#..#.",
                "..#.#...#.#",
                ".#...##..#.",
                "..#.##.....",
                ".#.#.#....#",
                ".#........#",
                "#.##...#...",
                "#...##....#",
                ".#..#...#.#"]
        
        self.assertEqual(day3.f2(inp), 336)
        
class Test_Day4(unittest.TestCase):
    
    def test_f1(self):
        inp = ["ecl:gry pid:860033327 eyr:2020 hcl:#fffffd",
            "byr:1937 iyr:2017 cid:147 hgt:183cm",
            "",
            "iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884",
            "hcl:#cfa07d byr:1929",
            "",
            "hcl:#ae17e1 iyr:2013",
            "eyr:2024",
            "ecl:brn pid:760753108 byr:1931",
            "hgt:179cm",
            "",
            "hcl:#cfa07d eyr:2025 pid:166559648",
            "iyr:2011 ecl:brn hgt:59in"]
        
        self.assertEqual(day4.f1(inp), 2)
        
    def test_f2(self):
        inp = ["ecl:gry pid:860033327 eyr:2020 hcl:#fffffd",
            "byr:1937 iyr:2017 cid:147 hgt:183cm",
            "",
            "iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884",
            "hcl:#cfa07d byr:1929",
            "",
            "hcl:#ae17e1 iyr:2013",
            "eyr:2024",
            "ecl:brn pid:760753108 byr:1931",
            "hgt:179cm",
            "",
            "hcl:#cfa07d eyr:2025 pid:166559648",
            "iyr:2011 ecl:brn hgt:59in"]
        
        self.assertEqual(day4.f2(inp), 2)
        
        invalid = """eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007""".splitlines()
        self.assertEqual(day4.f2(invalid), 0)
    