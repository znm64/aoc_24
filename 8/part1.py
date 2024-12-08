from utils import *
raw =[[i2 for i2 in i.strip()] for i in open("8.txt", "r").readlines()]

#getting all the antenna locations
all_antennae = {}
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
            result = Point((2*start.x)-end.x, (2*start.y)-end.y)
            if result.x>=0 and result.y>=0 and result.x<len(raw[0]) and result.y<len(raw):
                antinodes.add((result.x, result.y))

        
print(len(antinodes))
