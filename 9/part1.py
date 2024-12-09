from utils import *
raw = open("9.txt", "r").read().strip()
print(raw)
blocks = []
for id, num in enumerate(raw):
    if id %2:
        blocks += ["."]*int(num)
    else:
        blocks += ([str((id+1)//2)]* int(num))

print(blocks)

while True:
    try:
        a = blocks.index('.')
    except ValueError:
        break
    blocks[a] = blocks[-1]
    blocks.pop()

sum = sum([count*int(i) for count, i in enumerate(blocks)])
print(sum)