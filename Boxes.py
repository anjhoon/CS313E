#  File: Boxes.py

#  Description: Find largest subset(s) of nests lists and print them out

#  Student Name: Andrew Chen

#  Student UT EID: ac68644

#  Partner Name: Saaketh Palchuru

#  Partner UT EID: srp2992

#  Course Name: CS 313E

#  Unique Number: 50210

#  Date Created: 10/15/19

#  Date Last Modified: 10/16/19


def does_fit(box1, box2):
    return box1[0] < box2[0] and box1[1] < box2[1] and box1[2] < box2[2]


lst = []


def subsets(a, b, lo):
    global lst
    hi = len(a)
    if lo == hi:
        if len(b) >= 2:
            counter = 0
            for i in range(len(b) - 1):
                if does_fit(b[i], b[i + 1]):
                    counter += 1
                    if counter == len(b) - 1:
                        lst.append(b)
                else:
                    return
    else:
        c = b[:]
        b.append(a[lo])
        subsets(a, b, lo + 1)
        subsets(a, c, lo + 1)


def main():
    # open file for reading
    infile = open('boxes.txt', 'r')
    line = infile.readline()
    line = line.strip()
    num_boxes = int(line)

    # empty list for boxes
    box_list = []
    # read all boxes into the list
    for line in range(num_boxes):
        line = infile.readline()
        line = line.strip()
        box = line.split()
        for j in range(len(box)):
            box[j] = int(box[j])
        box.sort()
        box_list.append(box)

    infile.close()
    box_list.sort()
    new_list = []
    # find subsets of box_list
    subsets(box_list, new_list, 0)
    # sort the subsets in descending order
    lst.sort(key=len, reverse=True)
    # if no subsets in lst
    if len(lst) == 0:
        print('No Nesting Boxes')
    # if subsets in lst
    else:
        print('Largest Subset of Nesting Boxes')
        final_list = []
        # append the lists that are of the largest length
        for box in lst:
            max_len = len(lst[0])
            if len(box) == max_len:
                final_list.append(box)
        # print the nested boxes
        for box in final_list:
            for nest in box:
                print(nest)
            print()


main()
