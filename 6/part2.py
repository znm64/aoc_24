import copy
map =[[i2 for i2 in i.strip()] for i in open("6.txt", "r").readlines()]
from utils import *

width, height = len(map[0]), len(map)

for a, row in enumerate(map):
    if "^" in row:
        b = row.index("^")
        originalpos = Point(b,a, dir=2)

def check_visited(x, y, dir, past):
    return (True in [(x == pos.x and y == pos.y and dir == pos.dir) for pos in past])

def walk(map):
    pastpos = [originalpos]
    pos = copy.deepcopy(originalpos)
    while True:
        next_x, next_y = pos.next_pos()

        if next_x<0 or next_x>=width or next_y<0 or next_y>=height:
            map[pos.y][pos.x] = "X"
            return False

        elif map[next_y][next_x] in [".", "X"]:
            if check_visited(next_x, next_y, pos.dir, pastpos):
                return True
            map[pos.y][pos.x] = "X"
            
            pos.x, pos.y = next_x, next_y
            pastpos.append(copy.deepcopy(pos))

        elif map[next_y][next_x] == "#":
            pos.dir = (pos.dir-1)%4

result = []
for y, row in enumerate(map):
    for x, element in enumerate(row):
        if (x, y) == (originalpos.x, originalpos.y):
            continue
        altered = copy.deepcopy(map)
        altered[y][x] = "#"
        if walk(altered):
            result.append([y, x])
    
print(len(result))

#if this took longer to run i would optimise by only adding obstacles if they were on the original path - reduces the cases to roughly 5000, so about 70% faster