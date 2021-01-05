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
    #i = (i[0], i[1:])
    #make list of tuples
    """if len(i) > 1:
        for j in range(1, len(i)-1):
            i[j]"""

    dict[i[0]] = i[1:]

#count if has shiny gold bag
def has_shiny_gold(bag):
    if bag == 'shiny gold':
        return True
    else:
        #print (bag)
        return any(has_shiny_gold(c) for _,c in dict[bag])

bag_count = 0
for bag in dict:
    if has_shiny_gold(bag):
        bag_count += 1

#subtract one from total because dont want to count shiny gold bag itself
print(bag_count - 1)
