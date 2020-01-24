#  File: Triangle.py

#  Description: Use brute force, greedy, divide & conquer, and dynamic programming algorithms to find greatest sum path

#  Student's Name: Andrew Chen

#  Student's UT EID: ac68644

# Partner's Name: Edoardo Palazzi

# Partner's UT EID: emp2587

#  Course Name: CS 313E

#  Unique Number: 50210

#  Date Created: 12/3/19

#  Date Last Modified: 12/7/19

import time


# returns the greatest path sum using exhaustive search
def exhaustive_search(grid):
    sums = []
    exhaustive_search_helper(grid, 0, 0, sums, 0)
    return max(sums)


def exhaustive_search_helper(grid, row, col, sums, value):
    if row == len(grid):
        sums.append(value)
        return
    else:
        exhaustive_search_helper(grid, row + 1, col, sums, value + grid[row][col])
        exhaustive_search_helper(grid, row + 1, col + 1, sums, value + grid[row][col])


# returns the greatest path sum using greedy approach
def greedy(grid):
    greed_sum = grid[0][0]
    index = 0
    for i in range(1, len(grid)):
        if grid[i][index + 1] > grid[i][index]:
            index += 1
        greed_sum += grid[i][index]
    return greed_sum


# returns the greatest path sum using divide and conquer (recursive) approach
def rec_search(grid):
    left = 0
    right = 0
    return divide_and_conquer(grid, left, right)


def divide_and_conquer(grid, row, col):
    # if at the end return the value at the end
    if row == len(grid) - 1:
        return grid[row][col]
    else:
        # add the first and the max of each recursive call going down triangle
        return grid[row][col] + max(divide_and_conquer(grid, row + 1, col), divide_and_conquer(grid, row + 1, col + 1))


# returns the greatest path sum and the new grid using dynamic programming
def dynamic_prog(grid):
    # bottom up approach starting from second to last row
    for i in range(len(grid) - 2, -1, -1):
        # go through each column and add max of either the one below or the one next to it
        for j in range(len(grid[i])):
            grid[i][j] += max(grid[i + 1][j], grid[i + 1][j + 1])
    # eventually the max will be at the top
    return grid[0][0]


# reads the file and returns a 2-D list that represents the triangle
def read_file():
    # read triangular grid from file
    infile = open('triangle.txt', 'r')
    triangle = []

    # we don't really need the first line, so throw it out
    num = int(infile.readline())

    # build our triangle
    for i in range(num):
        line = infile.readline()
        line = line.strip().split()
        for j in range(len(line)):
            line[j] = int(line[j])
        triangle.append(line)
    # close file
    infile.close()

    return triangle


def main():
    # read triangular grid from file
    triangle = read_file()

    ti = time.time()
    # output greatest path from exhaustive search
    print('The greatest path sum through exhaustive search is ' + str(exhaustive_search(triangle)) + '.')
    tf = time.time()
    del_t = tf - ti
    # print time taken using exhaustive search
    print('The time taken for exhaustive approach is ' + str(del_t) + ' seconds.\n')

    ti = time.time()
    # output greatest path from greedy approach
    print('The greatest path sum through greedy search is ' + str(greedy(triangle)) + '.')
    tf = time.time()
    del_t = tf - ti
    # print time taken using greedy approach
    print('The time taken for greedy approach is ' + str(del_t) + ' seconds.\n')

    ti = time.time()
    # output greatest path from divide-and-conquer approach
    print('The greatest path sum through recursive search is ' + str(rec_search(triangle)) + '.')
    tf = time.time()
    del_t = tf - ti
    # print time taken using divide-and-conquer approach
    print('The time taken for recursive search is ' + str(del_t) + ' seconds.\n')

    ti = time.time()
    # output greatest path from dynamic programming
    print('The greatest path sum through dynamic programming is ' + str(dynamic_prog(triangle)) + '.')
    tf = time.time()
    del_t = tf - ti
    # print time taken using dynamic programming
    print('The time taken for dynamic programming is ' + str(del_t) + ' seconds.')


if __name__ == "__main__":
    main()
