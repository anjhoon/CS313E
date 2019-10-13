#  File: OfficeSpace.py
#  Description:
#  Student Name: Andrew Chen
#  Student UT EID: ac68644
#  Partner Name: Saaketh Palchuru
#  Partner UT EID: srp2992
#  Course Name: CS 313E
#  Unique Number: 50210
#  Date Created: 9/19/19
#  Date Last Modified: 9/23/19


def main():
    infile = open('office.txt', 'r')
    loop = True

    # keep going until loop is False
    while loop:
        # get dimensions
        first_line = infile.readline()
        if first_line == '':
            break
        first_line = first_line.strip().split()
        for i in range(len(first_line)):
            first_line[i] = int(first_line[i])

        # get number of employees
        number = infile.readline()
        number = number.strip()
        number = int(number)
        file_list = []
        # read in employee coordinates
        for i in range(number):
            line = infile.readline()
            line = line.strip().split()
            for j in range(len(line) - 1):
                line[j + 1] = int(line[j + 1])
            file_list.append(line)

        # make matrix of 0's for the x-y grid
        matrix = [[int(0) for j in range(first_line[0])] for i in range(first_line[1])]

        # increment 1 for for the range of employee coordinates
        for i in range(number):
            for row in range(file_list[i][2], file_list[i][4]):
                for col in range(file_list[i][1], file_list[i][3]):
                    matrix[row][col] += 1

        unallocated_counter = 0
        contested_counter = 0

        # add up 0's for unallocated space and 1's for contested space
        for row in matrix:
            for spot in row:
                if spot == 0:
                    unallocated_counter += 1
                elif spot > 1:
                    contested_counter += 1

        # code to see who has contested space or not
        outer_list = []
        for i in range(number):
            inner_list = []
            for row in range(file_list[i][2], file_list[i][4]):
                for col in range(file_list[i][1], file_list[i][3]):
                    inner_list.append(matrix[row][col])
            outer_list.append(inner_list)

        print("Total", first_line[0] * first_line[1])
        print("Unallocated", unallocated_counter)
        print("Contested", contested_counter)

        # print each employee's totals depending on if they have contested space or not
        j = 0
        for item in file_list:
            if any(i > 1 for i in outer_list[j]):
                print(item[0], ((abs(item[3] - item[1]) * abs(item[4] - item[2])) - contested_counter))

            else:
                print(item[0], abs(item[3] - item[1]) * abs(item[4] - item[2]))
            j += 1

        print()


main()