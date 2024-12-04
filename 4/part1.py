
raw =[[i2 for i2 in i.strip()] for i in open("4.txt", "r").readlines()]
from utils import *
count = 0

for x in range(len(raw[0])):
    for y in range(len(raw)):
        startpos = Point(x,y)
        for x_vector in range(-1, 2):
            for y_vector in range(-1, 2):
                result = ""
                for i in range(4):
                    coords = Point(startpos.x + i*(x_vector),startpos.y+i*(y_vector))
                    if 0<=coords.x<len(raw[0]) and 0<=coords.y<len(raw):
                        result+=raw[coords.y][coords.x]
                    else:
                        break
                if result == "XMAS":
                    count+=1

print(count)