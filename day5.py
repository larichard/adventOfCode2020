file = open("data5.txt", "r")
lines = list(map(lambda x: x.strip(), file.readlines()))

def ret_seat_ids(input):
    ids = []
    for i in input:
        row_max = 127
        row_min = 0
        col_max = 7
        col_min = 0

        fin_row = 0
        fin_col = 0
        seat_id = 0

        for j in i:
            row_diff = (row_max - row_min) / 2
            col_diff = (col_max - col_min) / 2
            #take smallest row
            if j == 'F':
                row_max = int(row_max - row_diff)
                fin_row = row_min
            #take largest row
            if j == 'B':
                row_min = int(row_max - row_diff) + 1
                fin_row = row_max
            #take largest col
            if j == 'R':
                col_min = int(col_max - col_diff) + 1
                fin_col = col_max
            #take smallest col
            if j == 'L':
                col_max = int(col_max - col_diff)
                fin_col = col_min

        seat_id = fin_row * 8 + fin_col
        ids.append(seat_id)
        
    return ids

def highest(seat_ids):
    max = 0
    for i in seat_ids:
        if i > max:
            max = i
    return max

def adjacent(seat_ids):
    for i in seat_ids:
        plus = i + 2
        minus = i - 2
        if plus in seat_ids and i + 1 not in seat_ids or minus in seat_ids and i - 1 not in seat_ids:
            return i+1

def main():
    print('Part 1: highest seat id')
    print(highest(ret_seat_ids(lines)))
    print('Part 2: id with +1 and -1')
    print(adjacent(ret_seat_ids(lines)))
    
if __name__ == "__main__":
    main()