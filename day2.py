file = open("data2.txt", "r")
lines = list(map(str, file.readlines()))
splitfile = list(map(lambda x: x.split(), lines))

# of valid passwords

def validByNum(policy):
    valid = 0
    for x in policy:
        # number of times char is in password
        times = 0
        # char required
        char = x[1][0]
        # list of times char must be in password 
        nums = list(map(int, x[0].split("-")))
        lo = nums[0]
        hi = nums[1]
        # the password
        psw = x[2]

        for element in psw:
            if(element == char):
                times += 1 

        if (times >= lo and times <= hi):
            valid += 1

    print(valid)

def validByPosition(policy):
    valid = 0
    for x in policy:
        # if char is in correct position
        times = False
        # char required
        char = x[1][0]
        # list of locations char must be in password
        nums = list(map(int, x[0].split("-")))
        posLo = nums[0]
        posHi = nums[1]
        # the password
        psw = x[2]

        if ((psw[posLo-1] == char and psw[posHi-1] != char) or 
            (psw[posLo-1] != char and psw[posHi-1] == char)):
            times = True
        
        if times:
            valid += 1
    
    print(valid)



def main():
    print("Part 1:")
    validByNum(splitfile)
    print("Part 2:")
    validByPosition(splitfile)

if __name__ == "__main__":
    main()