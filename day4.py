import re

file = open("data4.txt", "r")
lines = list(map(lambda x: x.split(), file.readlines()))

passports = []
index = 0
required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']



# !!! doesn't read last input
while index < len(lines)-3:
    split = []
    while lines[index] != []:
        split.extend(lines[index])
        index += 1
    passports.append(split)
    index += 1

def validByField(in_passports):
    valid = 0
    for single in in_passports:
        count = 7
        fields = []
        for elem in single:
            field = elem.split(':')
            fields.append(field[0])
        for elem in fields:
            if elem in required:
                count -= 1
        if count == 0:
            valid += 1
    return valid

def validByValue(in_passports):
    new_passports = []
    for single in in_passports:
        count = 7
        fields = []
        for elem in single:
            field = elem.split(':')
            fields.append(field[0])
        for elem in fields:
            if elem in required:
                count -= 1
        if count == 0:
            new_passports.append(single)
    return check(new_passports)

eye_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

def check(in_passports):
    valid = 0
    for single in in_passports:
        count = 0
        for elem in single:
            field = elem.split(':')
            #match to fields
            category = field[0]
            if(category == 'byr'):
                value = int(field[1])
                if 2002 >= value >= 1920:
                    count += 1
            if(category == 'iyr'):
                value = int(field[1])
                if 2020 >= value >= 2010:
                    count += 1
            if(category == 'eyr'):
                value = int(field[1])
                if 2030 >= value >= 2020:
                    count += 1
            if(category == 'hgt'):
                value = (field[1])
                if 'in' in value or 'cm' in value:
                    temp = re.compile("([0-9]+)([a-zA-Z]+)")
                    res = temp.match(value).groups()
                    value = int(res[0])
                    if res[1] == 'cm':
                        if 193 >= value >= 150:
                            count += 1
                    if res[1] == 'in':
                        if 76 >= value >= 59:
                            count += 1
            if(category == 'hcl'):
                value = field[1]
                if re.fullmatch("#[0-9a-f]{6}", value):
                    #print(value)
                    count += 1
            if(category == 'ecl'):
                value = field[1]
                if value in eye_colors:
                    count += 1
            if(category == 'pid'):
                value = (field[1])
                if re.fullmatch("[0-9]{9}", value):
                    count += 1         
        if count == 7:
            valid += 1
    return valid


def main():
    print("Part 1:")
    print(validByField(passports))
    print("Part 2:")
    print(validByValue(passports))
if __name__ == "__main__":
    main()