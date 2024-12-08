from utils import *
raw =[[i2 for i2 in i.strip()] for i in open("8.txt", "r").readlines()]
all_antennae = {}
#getting all the antenna locations
for y, row in enumerate(raw):
    for x, element in enumerate(row):
        if element != SPACE:
            if element in all_antennae:
                all_antennae[element].append(Point(x, y))
            else:
                all_antennae[element] = [Point(x, y)]

antinodes = set()
for symbol in all_antennae:
    antennae = all_antennae[symbol]
    for start in antennae:
        for end in antennae:
            if start.same_point(end):
                continue
            dist_amp = 1
            while True:
                result = Point(start.x+dist_amp*(end.x-start.x), start.y+dist_amp*(end.y-start.y))
                if result.x>=0 and result.y>=0 and result.x<len(raw[0]) and result.y<len(raw):
                    antinodes.add((result.x, result.y))
                    dist_amp+=1

                else:
                    break

print(len(antinodes))