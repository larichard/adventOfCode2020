import string

def counter(forms):
    count = 0
    for group in forms:
        alphabet = list(string.ascii_lowercase)
        for word in group:
            for letter in word:
                if letter in alphabet:
                    count += 1
                    alphabet.remove(letter)
    return count

def all_yes(forms):
    #count letters that are in all answers in a group
    count = 0
    for group in forms:
        max = len(group)
        alphabet = list(string.ascii_lowercase)
        for i in alphabet:
            tmp = 0
            for indiv in group:
                if i in indiv:
                    tmp += 1
            if tmp == max:
                count += 1

    return count


def main():

    file = open("data6.txt", "r")
    lines = list(map(lambda x: x.split(), file.readlines()))

    groups = []
    index = 0

    #need to add two lines at end of input file to work (??)
    while index < len(lines):
        split = []
        while lines[index] != []:
            split.extend(lines[index])
            index += 1
        groups.append(split)
        index += 1
    
    print("Part 1:")
    print(counter(groups))
    print("Part 2:")
    print(all_yes(groups))

if __name__ == "__main__":
    main()