raw =[i.strip() for i in open("5.txt", "r").readlines()]
rules = [[int(i2) for i2 in i.split("|")] for i in raw[:raw.index("")]]
orders = [[int(i2) for i2 in i.split(",")] for i in raw[raw.index("")+1:]]
rules_1 = [i[0] for i in rules]
rules_2 = [i[1] for i in rules]

def find_before(val):
    before = []
    for pos, i in enumerate(rules_2):
        if i == val:
            before.append(rules_1[pos])
    return before

def find_after(val):
    after = []
    for pos, i in enumerate(rules_1):
        if i == val:
            after.append(rules_2[pos])
    return after

correct_reports = []
for count, order in enumerate(orders):
    valid = 1
    for index, value in enumerate(order):
        values_after = order[index+1:]
        values_before = order[:index]
        for i in find_after(value):
            if i in values_before:
                valid = 0
        for i in find_before(value):
            if i in values_after:
                valid = 0
    if valid:
        correct_reports.append(order)

print(sum([i[len(i)//2] for i in correct_reports]))