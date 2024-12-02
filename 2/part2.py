# same logic as part 1, but iterated over each possible version of the report with an entry missing
# i may have gone insane after not remembering that .remove() takes away all instances of the number being removed (line 11)
# in my defence that bug only affected 4 times in the entire input data - took me ages to realise it :cry
raw = [[int(i2) for i2 in i.strip().split()] for i in open("2.txt", "r").readlines()]
allsafe = 0
for report_original in raw:
    results = [[], []]
    for count, section in enumerate(report_original + ["!"]):
        report = report_original.copy()
        if section != "!":
            report.pop(count)

        safe = ""
        decreasing, increasing = [], []
        prev = report[0]
        for i in report[1:]:
            if i > prev:
                increasing.append(1), decreasing.append(0)
            elif i < prev:
                increasing.append(0), decreasing.append(1)
            if (abs(i - prev) == 0) or (abs(i - prev) > 3):
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
            if section == "!":
                results[1].append(1)
            else:
                results[0].append(1)
    if (results[0].count(1) >= 1) or (1 in results[1]):
        allsafe += 1


print(allsafe)
