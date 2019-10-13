#  File: MagicSquare.py
#  Description: Create an odd NxN magic square using a 2-D list
#  Student's Name: Andrew Chen
#  Student's UT EID: ac68644
#  Partner's Name: Saaketh Palchuru
#  Partner's UT EID: srp2992
#  Course Name: CS 313E
#  Unique Number: 50210
#  Date Created: 9/1/19
#  Date Last Modified: 9/5/19

# Create the 2-D list that will be a magic square
def make_square(n):
    # make a matrix NxN that is filled with 0's
    my_nested_list = [[0 for i in range(n)] for i in range(n)]

    # create coordinates for the first value of '1' to be placed in and create the number that will be placed there
    x_counter = len(my_nested_list) - 1
    y_counter = int(len(my_nested_list) / 2)
    number_counter = 1

    # fill the matrix with the first number
    my_nested_list[x_counter][y_counter] = number_counter

    # make sure the number counter only goes up to how many ever spots are in the square
    while number_counter < (n * n):
        # start by adding 1 to each coordinate and the number value then run through loops to check where to put the number
        x_counter += 1
        y_counter += 1
        number_counter += 1

        # apply the logical rules to the square: always go down and to the right and wrap around if ouside the box and go above
        # if diagonally down or a number is already there. Wrap arounds are accomplsohed by setting the x or y coordinate to 0

        if x_counter not in range(0, len(my_nested_list)) and y_counter not in range(0, len(my_nested_list[0])):
            x_counter -= 2
            y_counter -= 1
        elif x_counter not in range(0, len(my_nested_list)):
            x_counter = 0
        elif y_counter not in range(0, len(my_nested_list[0])):
            y_counter = 0
        elif my_nested_list[x_counter][y_counter] != 0:
            x_counter -= 2
            y_counter -= 1
        my_nested_list[x_counter][y_counter] = number_counter

    return my_nested_list


def print_square(magic_square):
    # print the magic square in a clean format that is 6 units apart for each number
    length = len(magic_square[0])
    print("\nHere is a", length, "by", length, "matrix: \n")
    print('\n'.join([''.join(['{:6}'.format(num) for num in data])
                     for data in magic_square]))


def check_square(magic_square):
    # initialize several variables and lists to be used in the checking of the squares rows, columns, and diagonals
    row_sum = False
    col_sum = False
    diag_sum = False
    row_length = len(magic_square[0])
    col_length = len(magic_square)
    row_sum_list = []
    col_sum_list = []
    diag_sum_list = []

    # add the sum of each row to a list to be used later
    for row in magic_square:
        row_sum_list.append(sum(row))

    # add the sum of each column to a list to be used later
    col_sum_list = [sum(x) for x in zip(*magic_square)]

    # initialize variables for the diagonal test
    diag_total = 0
    reverse_diag_total = 0
    reverse_diag_width = 0
    reverse_diag_column = -1

    # append each number along the inital diagonal (0,0), (1,1), (2,2) to a list for later use
    for num in range(len(magic_square)):
        diag_total += magic_square[num][num]
    diag_sum_list.append(diag_total)

    # same as above but the other diagonal
    for num in range(len(magic_square)):
        reverse_diag_total += magic_square[reverse_diag_width][reverse_diag_column]
        reverse_diag_width += 1
        reverse_diag_column -= 1
    diag_sum_list.append(reverse_diag_total)

    # set up a temporary variable that equals the first number of the first row
    rTemp = row_sum_list[0]

    # check if this first item is equal to all the other items in the row_sum_list from earlier, if they
    # all are change row_sum to True
    for item in row_sum_list:
        if rTemp != item:
            row_sum = False
            break;
        else:
            row_sum = True

    # same as above but with column list
    cTemp = col_sum_list[0]
    for item1 in col_sum_list:
        if cTemp != item1:
            col_sum = False
            break;
        else:
            col_sum = True

    # same as above but with diagonal list
    dTemp = diag_sum_list[0]
    for item2 in diag_sum_list:
        if dTemp != item2:
            diag_sum = False
            break;
        else:
            diag_sum = True

    # if any of the booleans are false print that it is not a magic square
    if (row_sum == False) or (col_sum == False) or (diag_sum == False):
        print('\nThis is not a magic square')

    # if all booleans are true AND and first sum in all the lists are equal then print out that the magic square is magic
    elif (row_sum == col_sum == diag_sum == True) and (row_sum_list[0] == col_sum_list[0] == diag_sum_list[0]):
        print("\nThis is a magic square")


def main():
    # Prompt the user to enter an odd number 1 or greater
    odd_number = int(input("Enter an odd number 1 or greater: "))
    # Check the user input
    while odd_number % 2 == 0:
        odd_number = int(input("The number was not odd or greater than 1. Enter an odd number 1 or greater: "))
    # Create the magic square
    make_square(odd_number)
    print()
    print("This is a", odd_number,"by",odd_number,"magic square", end=".")
    print()
    # Print the magic square
    print()
    print_square(make_square(odd_number))
    print()
    # Verify that it is a magic square
    check_square(make_square(odd_number))

# This line above main is for grading purposes. It will not affect how
# your code will run while you develop and test it.
# DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
  main()
