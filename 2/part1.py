raw = [[int(i2) for i2 in i.strip().split()] for i in open("2.txt", "r").readlines()]
allsafe = 0
for count, report in enumerate(raw):
    safe = ""
    decreasing, increasing = [], []
    prev = report[0]
    for i in report[1:]:
        if i > prev:
            increasing.append(1), decreasing.append(0)
        elif i < prev:
            increasing.append(0), decreasing.append(1)
        if abs(i - prev) == 0 or abs(i - prev) > 3:
            safe = 0
            break

        prev = i
    if safe == 0:
        continue
    if (increasing == ([1] * len(decreasing))) or (
        increasing == ([0] * len(increasing))
    ):
        safe = 1
    if safe:
        allsafe += 1


print(allsafe)
