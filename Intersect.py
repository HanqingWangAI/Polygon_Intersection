import numpy as np 
from math import *
EPS = 1e-8
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
    
    # operator @
    def __matmul__(self, p):
        return self.x*p.y - self.y*p.x

    def dot(self, p):
        return self.x * p.x + self.y * p.y
    
    def length(self):
        return sqrt(pow(self.x,2.0)+pow(self.y,2.0))

    def cmp(self, p):
        return fabs(self.x - p.x) + fabs(self.y - p.y)
    

# alpha * a1 + (1 - alpha) * a2 = beta * b1 + (1 - beta) * b2
def cross_point(a1,a2,b1,b2):
    x2_x2 = b2.x - a2.x
    y2_y2 = b2.y - a2.y
    x1x2 = a1.x - a2.x 
    y1y2 = a1.y - a2.y 
    y1_y2_ = b1.y - b2.y
    x1_x2_ = b1.x - b2.x

    if fabs(y1_y2_*x1x2 - x1_x2_*y1y2) < EPS:
        beta = 1.0
    else:
        beta = (x2_x2*y1y2 - y2_y2*x1x2)/(y1_y2_*x1x2 - x1_x2_*y1y2)
    
    if x1x2 == 0:
        alpha = (y2_y2+y1_y2_*beta)/(y1y2+EPS)
    else:
        alpha = (x2_x2+x1_x2_*beta)/(x1x2+EPS)
    
    return alpha,beta,alpha*a1+(1-alpha)*a2

def polygon_area(points):
    num = len(points)
    area = 0
    for i in range(num):
        a = points[i-1]
        b = points[i]
        area += a@b

    return area*0.5


# Convex polygon intersection area
def CPIA(pa, pb):
    sa = polygon_area(pa)
    sb = polygon_area(pb)
    print('sa sb',sa,sb)
    if sa * sb < 0:
        sign = -1
    else:
        sign = 1
    na = len(pa)
    nb = len(pb)
    ps = [] # point set
    for i in range(na):
        a1 = pa[i-1]
        a2 = pa[i]
        flag = False
        sum_s = 0
        for j in range(nb):
            b1 = pb[j-1]
            b2 = pb[j]
            sum_s += fabs(polygon_area([a1,b1,b2]))
            
        if fabs(fabs(sum_s) - fabs(sb)) < EPS:
            flag = True

        if flag:
            ps.append(a1)
        for j in range(nb):
            b1 = pb[j-1]
            b2 = pb[j]
            a,b,p = cross_point(a1,a2,b1,b2)
            if a > 0 and a < 1 and b > 0 and b < 1:
                ps.append(p)
    
    for i in range(nb):
        a1 = pb[i-1]
        a2 = pb[i]
        flag = False
        sum_s = 0
        # print('a1',(a1.x,a1.y))
        for j in range(na):
            b1 = pa[j-1]
            b2 = pa[j]
            sum_s += fabs(polygon_area([a1,b1,b2]))
            # print('b1',(b1.x,b1.y),'b2',(b2.x,b2.y),(a1-b1)@(b2-b1))
        if fabs(fabs(sum_s) - fabs(sa)) < EPS:
            flag = True
        if flag:
            ps.append(a1)
    
    def unique(ar):
        res = []
        num = len(ar)
        for i,_ in enumerate(ar):
            if _.cmp(ar[i-1]) > EPS:
                res.append(_)

        return res
    
    ps = sorted(ps,key=lambda x:(x.x+EPS*x.y))
    ps = unique(ps)
    for _ in ps:
        print('x,y ',(_.x,_.y))
    print("============================")
    
    if len(ps) == 0:
        return 0
    
    tmp = ps[0]

    res = []
    res.append(tmp)
    ps = sorted(ps[1:],key = lambda x: -((x-tmp).dot(Point(0,1))/(x-tmp).length()))

    for _ in ps:
        res.append(_)
    
    
    # for _ in res:
    #     print('x,y',(_.x,_.y))

    return polygon_area(res) * sign

# Normal polygon intersection area
def NPIA(pa, pb):
    na = len(pa)
    nb = len(pb)
    res = 0
    for i in range(1,na-1):
        sa = []
        sa.append(pa[0])
        sa.append(pa[i])
        sa.append(pa[i+1])
        for j in range(1,nb-1):
            sb = []
            sb.append(pb[0])
            sb.append(pb[j])
            sb.append(pb[j+1])
            tmp = CPIA(sa,sb)
            print(i,j,tmp)
            res += tmp

    return fabs(res)


if __name__ == '__main__':
    # a1 = Point(-1,0)
    # a2 = Point(1,0)
    # b1 = Point(-0.5,0)
    # b2 = Point(2,0)

    # a,b,p = cross_point(a1,a2,b1,b2)
    # # print(a,b,p)
    # print(a,b,p.x,p.y)
    # # print(a2@b2)

    pa = []
    pb = []
    # pa.append(Point(-1,0))
    # pa.append(Point(1,1))
    # pa.append(Point(1,-1))

    # pb.append(Point(-1,1))
    # pb.append(Point(1,0))
    # pb.append(Point(-1,-1))
    # pa.append(Point(-1,1))
    # pa.append(Point(2,0))
    # pa.append(Point(-1,-1))

    # pb.append(Point(-2,0))
    # pb.append(Point(1,1))
    # pb.append(Point(1,-1))
    pa.append(Point(-1,1))
    pa.append(Point(1,1))
    pa.append(Point(1,-1))
    pa.append(Point(-1,-1))

    pb.append(Point(-1,1))
    pb.append(Point(1,1))
    pb.append(Point(1,-1))
    pb.append(Point(-1,-1))
    print(NPIA(pa,pb))
    # print(polygon_area(pa),polygon_area(pb),CPIA(pa,pb))
