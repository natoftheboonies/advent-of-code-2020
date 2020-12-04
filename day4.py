#!/usr/bin/env python3


def parse_passports(lines):
    passports = list()
    passport = dict()
    for line in lines:
        if not line:  # blank line indicates next passport
            passports.append(passport)
            passport = dict()
        else:
            fields = line.split()
            for field in fields:
                k, v = field.split(":")
                passport[k] = v
    # append the last passport (no blank line at end)
    passports.append(passport)
    return passports


REQUIRED_FIELDS = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}


def check_passports(passports):
	"""counts passports containing all REQUIRED_FIELDS"""
    valid_count = 0
    for passport in passports:
        if set(passport.keys()) >= REQUIRED_FIELDS:
            valid_count += 1
    return valid_count


def check_passports2(passports):
	"""counts passports satisfying all field validations"""

    def check_height(hgt):
        if hgt.endswith("cm"):
            return 150 <= int(hgt.split("cm")[0]) <= 193
        if hgt.endswith("in"):
            return 59 <= int(hgt.split("in")[0]) <= 76
        return False

    def check_hair(hcl):
    	"""hex code"""
        if hcl[0] == "#" and len(hcl) == 7:
        	return all(c.isdigit() or c.lower() in "abcdef" for c in hcl[1:])
        return False

    valid_count = 0
    for passport in passports:
        if set(passport.keys()) >= REQUIRED_FIELDS:
            if (
                (1920 <= int(passport["byr"]) <= 2002)
                and (2010 <= int(passport["iyr"]) <= 2020)
                and (2020 <= int(passport["eyr"]) <= 2030)
                and check_height(passport["hgt"])
                and check_hair(passport["hcl"])
                and passport["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
                and len(passport["pid"]) == 9
                and int(passport["pid"]) > 0
            ):
                valid_count += 1
    return valid_count


with open("input4") as fp:
    input_lines = fp.readlines()

passports = parse_passports([line.strip() for line in input_lines])
print("#1", check_passports(passports))
print("#2", check_passports2(passports))

sample = """\
ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in
""".splitlines()

passports = parse_passports([line.strip() for line in sample])
assert len(passports) == 4
assert check_passports(passports) == 2


invalid_sample = """\
eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007
""".splitlines()

passports = parse_passports([line.strip() for line in invalid_sample])
assert check_passports2(passports) == 0


valid_sample = """\
pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719
""".splitlines()

passports = parse_passports([line.strip() for line in valid_sample])
assert check_passports2(passports) == 4
