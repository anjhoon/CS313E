#  File: ConvexHull.py

#  Description: A file that takes in a list of points and returns the convex hull points of those points

#  Student Name: Andrew Chen

#  Student UT EID: ac68644

#  Partner Name: Saaketh Palchuru

#  Partner UT EID: srp2992

#  Course Name: CS 313E

#  Unique Number: 50210

#  Date Created: 9/25/19

#  Date Last Modified: 9/26/19


import math


class Point(object):
    # constructor
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # get the distance to another Point object
    def dist(self, other):
        return math.hypot(self.x - other.x, self.y - other.y)

    # string representation of a Point
    def __str__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'

    # equality tests of two Points
    def __eq__(self, other):
        tol = 1.0e-8
        return (abs(self.x - other.x) < tol) and (abs(self.y - other.y) < tol)

    def __ne__(self, other):
        tol = 1.0e-8
        return (abs(self.x - other.x) >= tol) or (abs(self.y - other.y) >= tol)

    def __lt__(self, other):
        tol = 1.0e-8
        if abs(self.x - other.x) < tol:
            if abs(self.y - other.y) < tol:
                return False
            else:
                return self.y < other.y
        return self.x < other.x

    def __le__(self, other):
        tol = 1.0e-8
        if abs(self.x - other.x) < tol:
            if abs(self.y - other.y) < tol:
                return True
            else:
                return self.y <= other.y
        return self.x <= other.x

    def __gt__(self, other):
        tol = 1.0e-8
        if abs(self.x - other.x) < tol:
            if abs(self.y - other.y) < tol:
                return False
            else:
                return self.y > other.y
        return self.x > other.x

    def __ge__(self, other):
        tol = 1.0e-8
        if abs(self.x - other.x) < tol:
            if abs(self.y - other.y) < tol:
                return True
            else:
                return self.y >= other.y
        return self.x >= other.x


# compute and return the determinant of the coordinates of three points
# p, q, and r are Point objects
def det(p, q, r):
    return p.x * q.y + q.x * r.y + r.x * p.y - p.y * q.x - q.y * r.x - r.y * p.x


# computes and returns the convex hull of a sorted list of Points
# convex hull is a list of Point objects starting at the extreme
# left point and going clockwise in order
def convex_hull(sorted_points):
    num_lines = len(sorted_points)
    upper_hull = [sorted_points[0], sorted_points[1]]

    for i in range(2, num_lines):
        upper_hull.append(sorted_points[i])
        while len(upper_hull) >= 3 and det(upper_hull[-3], upper_hull[-2], upper_hull[-1]) >= 0:
            upper_hull.pop(-2)

    lower_hull = [sorted_points[-1], sorted_points[-2]]

    for i in range(num_lines - 2, 1, -1):
        lower_hull.append(sorted_points[i])

        while len(lower_hull) >= 3 and det(lower_hull[-3], lower_hull[-2], lower_hull[-1]) >= 0:
            lower_hull.pop(-2)

    lower_hull.pop(-1)
    lower_hull.pop(0)

    for point in lower_hull:
        upper_hull.append(point)

    return upper_hull


# compute and return the area of a convex polygon
# convex_poly is a list of Point objects that define the vertices
# of a convex polygon in order
def area_poly(convex_poly):
    pos_total = 0
    neg_total = 0

    convex_poly.append(convex_poly[0])

    for num in range(len(convex_poly) - 1):
        pos_total += convex_poly[num].x * convex_poly[num + 1].y

        neg_total += convex_poly[num].y * convex_poly[num + 1].x

    area = (1 / 2) * abs(pos_total - neg_total)

    return area


def main():
    # create an empty list of Point objects
    point_object_list = []

    # open file points.txt for reading
    file = open("points.txt", 'r')
    num_lines = int(file.readline())

    # read file line by line, create Point objects and store in file
    for line in file:
        line = line.strip().split()
        x = int(line[0])
        y = int(line[1])
        point = Point(x, y)
        point_object_list.append(point)

    file.close()
    # sort the list according to x-coordinates
    point_object_list.sort(key=lambda point: point.x)

    # get the convex hull

    actual_hull = convex_hull(point_object_list)

    # print the convex hull
    print("Convex Hull")
    for num in actual_hull:
        print(num)

    # get the area of the convex xull
    area = area_poly(actual_hull)

    # print the area of the convex hull
    print("\nArea of convex hull = ", area)


# YOU MUST WRITE THIS LINE AS IS
if __name__ == "__main__":
    main()