from utils import *
raw = open("9.txt", "r").read().strip()
print(raw)
blocks = []
for id, num in enumerate(raw):
    if id %2:
        blocks += ["."]*int(num)
    else:
        blocks += ([str((id+1)//2)]* int(num))

finalid = blocks[-1]
def find_space(blocks, target_length):
    #take the argument of the lenght of the block that needs to be found - either rturn that or -1 .
    offset = 0
    while True:
        try:
            a = blocks.index(".")
        except ValueError:
            return -1
        b = a
        while True:
            if b>=len(blocks): break
            if blocks[b]!=".": break
            b += 1
        if b-a>=target_length:
            break
        else:
            blocks = blocks[a+1:]
            offset+=(a+1)
    return a+offset

print(finalid)
for num in range(int(finalid), -1, -1):
    if num%100 == 0:
        print(num)
    occurencecount = blocks.count(str(num))
    space = find_space(blocks, occurencecount)

    if space!=-1 and space < (blocks.index(str(num))):
        blocks = rp_all(str(num), ".", blocks)
        blocks[space:space+occurencecount] = [num]*(occurencecount)
        
    
sum = sum([(count*int(i)) if i!= '.' else 0 for count, i in enumerate(blocks)])
print(sum)