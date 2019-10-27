#  File: Work.py

#  Description:  Manipulate binary search to find out the minimum n lines of code needed to finish the program

#  Student Name: Andrew Chen

#  Student UT EID: ac68644

#  Course Name: CS 313E

#  Unique Number: 50210

#  Date Created: 9/29/19

#  Date Last Modified: 9/30/19


def binarySearch(a, x):
    lo = 0
    hi = a

    while lo <= hi:
        mid = (lo + hi) // 2
        number = findSum(mid, x)
        number2 = findSum(mid -1, x)
        if number > hi and number2 > hi:
            hi = mid - 1
        elif number < hi and number2 < hi:
            lo = mid + 1
        elif number >= hi and number2 == hi:
            return mid - 1
        else:
            return mid


def findSum(n, x):
    exp = 0
    sums = 0
    stop = 1

    while stop != 0:
        eq = n // x ** exp
        sums += eq
        exp += 1
        if eq == 0:
            stop = 0

    return sums


def main():
    infile = open('work.txt', 'r')

    loops = infile.readline()
    loops = int(loops)

    for i in range(loops):
        line = infile.readline()
        line = line.strip().split()
        for j in range(len(line)):
            line[j] = int(line[j])

        answer = binarySearch(line[0], line[1])
        print(answer)

    infile.close()


main()
