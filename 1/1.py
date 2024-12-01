raw = [i.strip() for i in open('1.txt', "r").readlines()]

left, right = [],[]
for i in raw:
    both = i.split()
    left.append(int(both[0]))
    right.append(int(both[1]))

left.sort()

right.sort()
sumdif = 0
for count, i in enumerate(left):
    sumdif+=abs(i-(right[count]))

print(sumdif)

#part 2

sumdif = 0
for count, i in enumerate(left):
    sumdif+=i*right.count(i)

print(sumdif)