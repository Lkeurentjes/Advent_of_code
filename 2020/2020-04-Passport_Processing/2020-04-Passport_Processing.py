import re

def check_passport(passport, checks):
    for check in checks:
        if check not in passport:
            return False
    return True

def is_valid_byr(byr):
    return byr.isdigit() and 1920 <= int(byr) <= 2002

def is_valid_iyr(iyr):
    return iyr.isdigit() and 2010 <= int(iyr) <= 2020

def is_valid_eyr(eyr):
    return eyr.isdigit() and 2020 <= int(eyr) <= 2030

def is_valid_hgt(hgt):
    if hgt.endswith("cm"):
        value = hgt[:-2]
        return value.isdigit() and 150 <= int(value) <= 193
    elif hgt.endswith("in"):
        value = hgt[:-2]
        return value.isdigit() and 59 <= int(value) <= 76
    return False

def is_valid_hcl(hcl):
    return bool(re.fullmatch(r"#[0-9a-f]{6}", hcl))

def is_valid_ecl(ecl):
    return ecl in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}

def is_valid_pid(pid):
    return pid.isdigit() and len(pid) == 9

def check_passport_stats(passport, validation):
    for check in validation.keys():
        if not validation[check](passport[check]):
            return False
    return True

with open('2020-04-Passport_Processing.txt') as f:
    passports = [p.replace("\n", " ") for p in f.read().split("\n\n")]
    passports_dict = [{item.split(":")[0] :item.split(":")[1] for item in p.split()} for p in passports]

    validation_functions = {
        "byr": is_valid_byr,
        "iyr": is_valid_iyr,
        "eyr": is_valid_eyr,
        "hgt": is_valid_hgt,
        "hcl": is_valid_hcl,
        "ecl": is_valid_ecl,
        "pid": is_valid_pid,
    }

    total = 0
    total_stats = 0
    for passport in passports_dict:
        if check_passport(passport, validation_functions.keys()):
            total += 1
            if check_passport_stats(passport, validation_functions):
                total_stats += 1


    print("Part 1, valid passports:", total)
    print("Part 2, valid passports:", total_stats)
