#count if bag has shiny gold bag
def has_shiny_gold(bag, dict):
    if bag == 'shiny gold':
        return True
    else:
        #print (bag)
        return any(has_shiny_gold(c,dict) for _,c in dict[bag])

def shiny_gold_count(dict):
    bag_count = 0
    for bag in dict:
        if has_shiny_gold(bag, dict):
            bag_count += 1

    #subtract one from total because dont want to count shiny gold bag itself
    print(bag_count - 1)

#count # of bags in a bag
def count_bags(bag, dict):
    # add 1 to count each bag as it is processed
    bag_count = 1
    # recurse and multiply
    for num, color in dict[bag]:
        bag_count += num * count_bags(color, dict)

    return bag_count

def main():
    file = open("data7.txt", "r")
    lines = list(map(lambda x: x.split(), file.readlines()))

    nums = list('123456789')
    unwanted = ['bag', 'bag.', 'bag,', 'bags', 'bags,', 'bags.', 'contain']
    dict = {}

    #parse
    for i in lines:
        #concat first two elems
        i[0] += ' ' 
        i[0] += (i[1])
        i.remove(i[1])

        #remove unwanted words
        i[:] = [word for word in i if word not in unwanted]

        #if bag has no other bags
        if 'no' in i:
            i[1] = (0, i[2])      
            i.remove(i[2])
            i = [i[0]]

        #make tuples of number and color
        for idx, j in enumerate(i):
            if j in nums and not j == i[-1]:
                i[idx+1] += ' '
                i[idx+1] += i[idx+2]
                i.remove(i[idx+2])
                i[idx] = (int(j), i[idx+1])
                i.remove(i[idx+1])

        dict[i[0]] = i[1:]
    
    print("Part 1:")
    shiny_gold_count(dict)
    print("Part 2:")
    # subtract 1 for original gold bag
    print(count_bags('shiny gold', dict) - 1)

if __name__ == "__main__":
    main()