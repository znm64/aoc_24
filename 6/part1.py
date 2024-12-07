map =[[i2 for i2 in i.strip()] for i in open("6.txt", "r").readlines()]
from utils import *

width, height = len(map[0]), len(map)

for a, row in enumerate(map):
    if "^" in row:
        b = row.index("^")
        pos = Point(b,a, dir=2)

while True:
    next_x, next_y = pos.next_pos()
    if next_x<0 or next_x>=width or next_y<0 or next_y>=height:
        map[pos.y][pos.x] = "X"
        break

    elif map[next_y][next_x] in [".", "X"]:
        map[pos.y][pos.x] = "X"
        pos.x, pos.y = next_x, next_y

    elif map[next_y][next_x] == "#":
        pos.dir = (pos.dir-1)%4
    
print(sum(row.count("X") for row in map))