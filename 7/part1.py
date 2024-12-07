from itertools import permutations 
from utils import *
raw =[i.strip().split(": ") for i in open("7.txt", "r").readlines()]
result_arr, inputs_arr = [int(i[0]) for i in raw], [[int(i2) for i2 in i[1].split()] for i in raw]

possible = []
for count, result in enumerate(result_arr):
    print(count)
    #each line
    breakflag = 0
    inputs = inputs_arr[count]
    for i in range(len(inputs)):
        #each amount of * or + is adjusted
        a = ["*"]*(i)
        a+=["+"]*(len(inputs)-i-1)
        for perm in set(permutations(a)):
            #get all possible expressions out, with duplicates removed
            if perm[-1] == "*" and (result%inputs[-1]) != 0:
                continue
            calc = [[inputs[count], b] for count, b in enumerate(perm)]
            calc.append([inputs[-1]])
            a = [str(k) for k in flatten_2d(calc)]
            #take the result of the expression
            for i in range(len(inputs)-1):
                temp = str(eval("".join(a[0:3])))
                a[2] = temp
                a = a[2:]
                if int(temp)>result:
                    break
            #check result
            if int(a[0]) == result:
                possible.append(result)
                breakflag = 1
                break
        if breakflag:
            break
    
print("final ans", sum(possible))