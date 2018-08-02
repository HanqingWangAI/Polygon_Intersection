import numpy as np 

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self, p):
        return Point(self.x + p.x, self.y + p.y)
    
    def __sub__(self, p):
        return Point(self.x - p.x, self.y - p.y)
    
    def __rmul__(self, scalar):
        return Point(self.x*scalar, self.y*scalar)

    def __mul__(self, scalar):
        return Point(self.x*scalar, self.y*scalar)

    def __matmul__(self, p):
        return self.x*p.y - self.y*p.x

    def dot(self, p):
        return Point(self.x * p.x, self.y * p.y)
    

    

# alpha * a1 + (1 - alpha) * a2 = beta * b1 + (1 - beta) * b2

def cross_point(a1,a2,b1,b2):
    x2_x2 = b2.x - a2.x
    y2_y2 = b2.y - a2.y
    x1x2 = a1.x - a2.x 
    y1y2 = a1.y - a2.y 
    y1_y2_ = b1.y - b2.y
    x1_x2_ = b1.x - b2.x
    beta = (x2_x2*y1y2 - y2_y2*x1x2)/(y1_y2_*x1x2 - x1_x2_*y1y2)
    if x1x2 == 0:
        alpha = (y2_y2+y1_y2_*beta)/y1y2
    else:
        alpha = (x2_x2+x1_x2_*beta)/x1x2
    
    return alpha,beta,alpha*a1+(1-alpha)*a2

def area(points):
    num = len(points)
    for i in range(num):
        

if __name__ == '__main__':
    a1 = Point(-1,0)
    a2 = Point(1,0)
    b1 = Point(3,-1)
    b2 = Point(3,1)

    a,b,p = cross_point(a1,a2,b1,b2)
    print(a,b,p.x,p.y)
    # print(a2@b2)