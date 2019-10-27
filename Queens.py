#  File: Queens.py

#  Description:

#  Student Name: Andrew Chen

#  Student UT EID: ac68644

#  Partner Name: Saaketh Palchuru

#  Partner UT EID: srp2992

#  Course Name: CS 313E

#  Unique Number: 50210

#  Date Created: 10/19/19

#  Date Last Modified: 10/20/19


class Queens(object):
    # initialize the board
    def __init__(self, n=8):
        self.board = []
        self.count = 0
        self.n = n
        for i in range(self.n):
            row = []
            for j in range(self.n):
                row.append('*')
            self.board.append(row)

    # print the board
    def print_board(self):
        for i in range(self.n):
            for j in range(self.n):
                print(self.board[i][j], end=' ')
            print()

    # check if no queen captures another
    def is_valid(self, row, col):
        for i in range(self.n):
            if self.board[row][i] == 'Q' or self.board[i][col] == 'Q':
                return False
        for i in range(self.n):
            for j in range(self.n):
                row_diff = abs(row - i)
                col_diff = abs(col - j)
                if (row_diff == col_diff) and (self.board[i][j] == 'Q'):
                    return False
        return True

    # do a recursive backtracking solution
    def recursive_solve(self, col):
        if col == self.n:
            self.count += 1
            self.print_board()
            print()

        else:
            for i in range(self.n):
                if self.is_valid(i, col):
                    self.board[i][col] = 'Q'
                    self.recursive_solve(col + 1)
                    self.board[i][col] = '*'

    def print_count(self):
        print('There are ', self.count, 'solutions for a', self.n, 'x', self.n, 'board.')


def main():
    board_size = int(input('Enter the size of the board: '))
    while board_size < 1 or board_size > 8:
        board_size = int(input('Enter the size of the board: '))
    # create a regular chess board
    game = Queens(board_size)

    # place the queens on the board
    game.recursive_solve(0)
    game.print_count()


main()