
from utils import *

raw =[[i2 for i2 in i.strip()] for i in open("4.txt", "r").readlines()]

count = 0
log=[]
for x in range(len(raw[0])):
    for y in range(len(raw)):
        startpos = Point(x,y)
        result = ""
        for y_vector in range(-1, 2):
            for x_vector in range(-1, 2):
                coords = Point(startpos.x+x_vector, startpos.y+y_vector)
                if 0<=coords.x<len(raw[0]) and 0<=coords.y<len(raw):
                    result+=raw[coords.y][coords.x]
        resultant = "".join([i if ((count%2) == 0) else "" for count, i in enumerate(result)])
        if resultant in ["MSAMS", "SMASM","MMASS", "SSAMM"]:
            count+=1
print(count)