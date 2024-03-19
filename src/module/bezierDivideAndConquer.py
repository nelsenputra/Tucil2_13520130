from dataclasses import dataclass
from module.timeFunc import timeHere

@dataclass
class Point :

    x : float
    y : float

    def __add__(self, other) :
        return Point(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other) :
        return Point(self.x - other.x, self.y - other.y)
    
    def __mul__(self, k: float) :
        return Point(self.x * k, self.y * k)
    
    def __truediv__(self, k: float) :
        return Point(self.x / k, self.y / k)
    
    def __str__(self) :
        return f"({self.x}, {self.y})"

def midPoint(p1: Point, p2: Point) -> Point :
    return (p1 + p2) / 2

def weightedPoint(p1: Point, p2: Point, t: float) -> Point :
    return (p1 * t) + (p2 * (1 - t))


def quadraticBezier(p0, p2, p1, iter: int) -> list[Point]:
    # p2 is control point

    if iter == 0 :
        return [p0,p2,p1]
    
    elif iter == 1 : 
        q0 = midPoint(p0, p2)
        q1 = midPoint(p2, p1)
        r0 = midPoint(q0, q1)
        return [p0,r0,p1]

    else :
        p02 = midPoint(p0, p2)
        p21 = midPoint(p2, p1)
        r0 = midPoint(p02, p21)
        
        # divide and conquer
        l = (quadraticBezier(p0, p02, r0, iter - 1))[:-1]
        m = [r0]
        r = (quadraticBezier(r0, p21, p1, iter - 1))[1:]
        
        return l + m + r

def nDegreeBezier(points: list[Point], iter: int) -> list[Point] :

    if iter == 0 :
        return points
    
    elif iter == 1 :

        prevPoints = points.copy()
        for i in range(len(points) - 1) :
            newPoints = list()
            for j in range(1, len(prevPoints)) :
                newPoints.append(midPoint(prevPoints[j], prevPoints[j-1]))
            prevPoints = newPoints

        p0 = points[0]
        r0 = prevPoints[0]
        p1 = points[-1]

        return [p0,r0,p1]
    
    else :

        p0 = points[0]
        p1 = points[-1]

        leftPoints = [p0]
        rightPoints = [p1]

        # Process all bezier points up to nth degree
        prevPoints = points.copy()
        for i in range(len(points) - 1) :
            newPoints = list()
            for j in range(1, len(prevPoints)) :
                newPoints.append(midPoint(prevPoints[j], prevPoints[j-1]))

            leftPoints.append(newPoints[0])
            rightPoints.append(newPoints[-1])
            
            prevPoints = newPoints

        rightPoints.reverse()
        r0 = prevPoints[0]
        
        # divide and conquer
        l = nDegreeBezier(leftPoints, iter - 1)[:-1]
        m = [r0]
        r = nDegreeBezier(rightPoints, iter - 1)[1:]
        
        return l + m + r

# nDegreeBezier is a recursive function so we need a helper to time it from the beginning to the end
@timeHere
def helper(points: list[Point], iter: int) :
    return nDegreeBezier(points, iter)