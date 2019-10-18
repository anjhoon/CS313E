#  File: EvenMagicSquare.py

#  Description: Prints out first 10 even magic squares through pruning certain paths that are impossible

#  Student Name: Andrew Chen

#  Student UT EID: ac68644

#  Partner Name: Saaketh Palchuru

#  Partner UT EID: srp2992

#  Course Name: CS 313E

#  Unique Number: 50210

#  Date Created: 10/12/19

#  Date Last Modified:


counter = 0


def even_magic_square(a, lo):
    global counter
    hi = len(a)
    if counter == 10:
        return
    if lo == 4 and a[0] + a[1] + a[2] + a[3] != 34:
        return
    elif lo == 8 and a[4] + a[5] + a[6] + a[7] != 34:
        return
    elif lo == 12 and a[8] + a[9] + a[10] + a[11] != 34:
        return
    elif lo == 13 and a[12] + a[9] + a[6] + a[3] != 34:
        return
    elif lo == 13 and a[0] + a[4] + a[8] + a[12] != 34:
        return
    elif lo == 14 and a[1] + a[5] + a[9] + a[13] != 34:
        return
    elif lo == 15 and a[2] + a[6] + a[10] + a[14] != 34:
        return
    elif lo == hi and a[15] + a[10] + a[5] + a[0] != 34:
        return
    elif lo == hi:
        print(a)
        counter += 1
    else:
        for i in range(lo, hi):
            a[lo], a[i] = a[i], a[lo]
            even_magic_square(a, lo + 1)
            a[lo], a[i] = a[i], a[lo]

def main():
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    lst2 = [1, 2, 3, 4]
    even_magic_square(lst, 0)


main()
