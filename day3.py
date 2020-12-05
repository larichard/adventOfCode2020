file = open("data3.txt", "r")
lines = list(map(lambda x:x.strip(), file.readlines()))

#get # of trees hit using a given slope
def slope(x, y):
    # of trees hit
    trees = 0
    # last recursion
    fin_depth = len(lines) - 2

    cur_depth = 0
    loc_in_row = 0

    while cur_depth <= fin_depth:
        cur_depth += y
        loc_in_row = (loc_in_row + x) % (len(lines[0]))

        if lines[cur_depth][loc_in_row] == "#":
            trees += 1

    return trees

def main():
    print("Part 1:")
    print(slope(3, 1))
    print("Part 2:")
    print(slope(3, 1) * slope(1, 1) * slope(5,1) * slope(7,1) * slope(1,2))
    
if __name__ == "__main__":
    main()