file = open("data1.txt", "r")
lines = file.readlines()
nums = list(map(int, lines))

def twoSum2020(nums):
    for x in nums:
        for y in nums:
            if (x + y) == 2020:
                print(x * y)

def threeSum2020(nums):
    for x in nums:
        for y in nums:
            for z in nums:
                if(x+y+z == 2020):
                    print(x*y*z)

def main():
    print("Part 1:")
    twoSum2020(nums)
    print("Part 2")
    threeSum2020(nums)

if __name__ == "__main__":
    main()