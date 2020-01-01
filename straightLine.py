#You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.

def straightLine(coordinates):
    epsilon=0.00001
    p0 = coordinates[0]
    p1 = coordinates[1]

    if p0[0]-p1[0]==0:
        return False
    else:
        m = (p0[1]-p1[1])/(p0[0]-p1[0])
        b = p0[1] - m * p0[0]

        for p in coordinates[2:]:
            if abs(p[1]-m*p[0]-b)>epsilon:
                return False

        return True
