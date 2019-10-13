#  File: Intervals.py
#  Description: Collapse intersecting intervals in a text file
#  Student Name: Andrew Chen
#  Student UT EID: ac68644
#  Partner Name: Saaketh Palchuru
#  Partner UT EID: srp2992
#  Course Name: CS 313Ez
#  Unique Number: 50210
#  Date Created: 9/5/19
#  Date Last Modified: 9/9/19


def createList(file):

    interval_list = []

    # get rid of whitespace and make strings into lists
    for line in file:
        if not line.strip():
            continue
        num = line.strip().split()
        interval_list.append(num)
    # make strings into ints in 2-D list
    interval_list = [[int(string) for string in line] for line in interval_list]
    print(interval_list)
    # make tuples out of intervals in 2-D list
    tuple_list = [tuple(interval) for interval in interval_list]
    print(tuple_list)
    # sort the tuples in 2-D list
    sorted_list = sorted(tuple_list)
    print(sorted_list)

    return sorted_list


def collapseInterval(tuple_list):
    # establish list with first interval to compare
    collapsed_list = [tuple_list[0]]
    print(collapsed_list)

    for next_int in tuple_list:
        first = collapsed_list[-1]
        # if next interval is already inside the current interval, continue
        if next_int[0] >= first[0] and next_int[1] <= first[1]:
            continue
        # if next interval is partially outside the current interval,
        # make a new interval and assign that as current interval
        elif next_int[0] <= first[1]:
            # list literal
            new_interval = [first[0], next_int[1]]
            collapsed_list[-1] = tuple(new_interval)
        # if next interval cannot be collapsed add that to collapsed_list
        else:
            collapsed_list.append(next_int)

    return collapsed_list


def printCollapsedList(collapsed_list):
    # print out tuples in collapsed list every line
    print("Non-intersecting Intervals:")
    for tup in collapsed_list:
        print(tup)


def printSizeList(collapsed_list):

    collapsed_list.sort(key=lambda interval: abs(interval[0] - interval[1]))
    print("Non-intersecting Intervals in order of size:")
    for tup in collapsed_list:
        print(tup)


def main():
    input_file = open("Intervals.txt", "r")
    first_list = createList(input_file)
    second_list = collapseInterval(first_list)
    printCollapsedList(second_list)
    print()
    printSizeList(second_list)



main()
