from typing import *

class Point:
    def __init__(self, x, y, z = 0, dir = 0):
        self.x = x
        self.y = y
        self.z = z
        self.dir = dir
    
    def find_dist(self, target) -> float:
        return ((target.x-self.x)**2 + (target.y-self.y)**2 + (target.z-self.z)**2)**0.5
    
    def step_vector(self):
        x_vector, y_vector = 0,0
        if self.dir % 2:
            #1, 3
            x_vector = (self.dir*-1)+2
        else:
            #0, 2
            y_vector = 1-self.dir
            
        return x_vector, y_vector
    
    def next_pos(self):
        a = self.step_vector()

        return self.x + a[0], self.y + a[1]

def get_col(arr, colnum):
    return [row[colnum] for row in arr]

#return a square of dimensions size * size, of adjacent elements around a position in a 2d array
def get_adj(arr, size, point):
    result = []
    for x_offset in range(-1*size, size+1):
        for y_offset in range(-1*size, size+1):
            result.append(arr[point.x+x_offset][point.y+y_offset])
    return result

def display_arr(map):
    for row in map:
        print("".join(row))