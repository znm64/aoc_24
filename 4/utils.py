from typing import *

class Point:
    def __init__(self, x, y, z = 0):
        self.x = x
        self.y = y
        self.z = z
    def find_dist(self, target) -> float:
        return ((target.x-self.x)**2 + (target.y-self.y)**2 + (target.z-self.z)**2)**0.5

def getcol(arr, colnum):
    return [row[colnum] for row in arr]

#return a square of adjacent elements around a position in a 2d array
def getadj(arr, size, point):
    result = []
    for x_offset in range(-1*size, size+1):
        for y_offset in range(-1*size, size+1):
            result.append(arr[point.x+x_offset][point.y+y_offset])
    return result
