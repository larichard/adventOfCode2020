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
        # the password
        psw = x[2]

        for element in psw:
            if(element == char):
                times += 1 

        #print (nums[1])
        if (times >= nums[0] and times <= nums[1]):
            valid += 1

    print(valid)

def validByPosition(policy):
    valid = 0


def main():
    print("Part 1:")
    validByNum(splitfile)

if __name__ == "__main__":
    main()