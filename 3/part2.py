import part1
import re

raw = open("3.txt", "r").read()
go, stop = [i.start() for i in re.finditer("do", raw)], [i.start() for i in re.finditer("don't", raw)]
for i in stop:
    if i in go: go.remove(i)

pos = []
for i in range(len(raw)):
    if i in go: pos.append([1, i])
    elif i in stop: pos.append([0, i])
pos.append([0, len(raw) - 1])

valid, command, read, i = [], [], 1, 0

for instr in pos:
    if read: valid += [i2 for i2 in range(i, instr[1])]
    read, i = instr[0], instr[1]

allowed = "".join([raw[i] for i in valid])

part1.getmultis(allowed)
