# think of 10 neighbors handshaking each other, there are 45 total handshakes

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

    # test for equality of two Point objects
    def __eq__(self, other):
        tol = 1.0e-16
        return ((abs(self.x - other.x) < tol) and (abs(self.y - other.y) < tol))


def main():
    # create an empty list of Point objects
    points = []
    # open file points.txt for reading
    infile = open("points.txt", "r")
    # read the file line by line, create Point objects and add to the list
    for line in infile:
        n = line.strip().split()
        point = Point(int(n[0]), int(n[1]))
        points.append(point)

    # initialize a variable to hold the shortest distance
    shortest = 999999
    # Use a pair of nested loops to go through all pairs of Point objects
    for i in range(len(points)):
        for j in range(len(points) - 1):
            distance = (points[i].dist(points[j]))

            # Find the minimum distance between all pairs
            if distance < shortest and distance != 0:
                shortest = distance
    # print the shortest distance
    print(shortest)


main()
