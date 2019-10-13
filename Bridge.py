#  File: Bridge.py

#  Description: Find the fastest time that people can go over if only two people can go over at a time

#  Student Name: Andrew Chen

#  Student UT EID: ac68644

#  Partner Name: Saaketh Palchuru

#  Partner UT EID: srp2992

#  Course Name: CS 313E

#  Unique Number: 50210

#  Date Created: 10/2/19

#  Date Last Modified: 10/4/19


# first algorithm of moving with two fastest and two slowest
def move(people):
    time = 0
    cross = []

    while len(people) > 2:
        # bring over 2 fastest and bring back fastest

        cross.append(people[1])
        time += people[0] + people[1]
        people.pop(1)

        if len(people) <= 2:
            break
        # bring over 2 slowest and bring back fastest

        cross.append(people[-1])
        people.pop(-1)
        cross.append(people[-1])
        people.pop(-1)
        people.append(cross[-3])
        people.sort()
        time += cross[-2] + cross[-3]
        cross.pop(-3)

    if len(people) == 1:
        time += people[0]
    elif len(people) == 2:
        time += people[1]

    return time


# second algorithm with fastest and next fastest
def move2(people):
    time2 = 0
    cross = []

    while len(people) > 2:
        # bring over fastest 2 and take back fastest one

        cross.append(people[1])
        time2 += people[0] + people[1]
        people.pop(1)
    if len(people) == 1:
        time2 += people[0]
    elif len(people) == 2:
        time2 += people[1]

    return time2


def main():
    infile = open('bridge.txt', 'r')

    cases = int(infile.readline())

    # go through all cases
    for i in range(cases):
        infile.readline()
        people = int(infile.readline())
        # create list of times for people
        all_people = []
        for j in range(people):
            all_people.append(int(infile.readline().strip()))
        all_people.sort()
        # create a copy to use
        all_people2 = all_people[:]

        time2 = move2(all_people)
        time1 = move(all_people2)

        # print time depending on faster time from two algorithms
        if time1 < time2:
            print(time1)
        elif time2 < time1:
            print(time2)
        elif time2 == time1:
            print(time1)
        print()

    infile.close()


main()
