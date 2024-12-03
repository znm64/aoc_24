import re

raw = open("3.txt", "r").read()


def getmultis(raw):
    a = sum((i[0] * i[1]) for i in [[int(i2) for i2 in i.replace("mul(", "").replace(")", "").split(",")] for i in re.findall("mul\([0-9]*,[0-9]*\)", raw)])
    print(a)

if __name__ == "__main__":
    getmultis(raw)


# or
print(sum((i[0] * i[1]) for i in [[int(i2) for i2 in i.replace("mul(", "").replace(")", "").split(",")] for i in re.findall("mul\([0-9]*,[0-9]*\)", open("3.txt", "r").read())]))