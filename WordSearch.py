#  File: WordSearch.py
#  Description: A program that finds words in a nxn matrix and returns the index position of the word into a text file
#  Student Name: Andrew Chen
#  Student UT EID: ac68644
#  Partner Name: Saaketh Palchuru
#  Partner UT EID: srp2992
#  Course Name: CS 313E
#  Unique Number: 50210
#  Date Created: 9/9/19
#  Date Last Modified: 9/16/19


# creates strings of each row of the matrix for other functions to find the word
def make_strings(matrix):
    row_list = []
    # joins together each letter of the row into one spot of a list
    for row in matrix:
        temp_row = ''.join(row)
        row_list.append(temp_row)
    return row_list


# read the file and makes dimensions, a list out of the word search, and a list out of the words to be found
def make_list():
    # read file and get dimensions
    file = open("hidden.txt", 'r')
    first_line = file.readline()
    dimensions = first_line.strip().split()
    file.readline()

    i = 0
    word_matrix = []
    # read word search and turn into a list
    while i < int(dimensions[0]):
        line = file.readline()
        line = line.strip().split()
        word_matrix.append(line)
        i += 1

    file.readline()
    # number of words to be found
    number_of_words = file.readline()
    number_of_words = int(number_of_words)

    word_list = []
    # put words to be found into a list
    for i in range(number_of_words):
        line = file.readline().strip()
        word_list.append(line)

    file.close()

    return dimensions, word_matrix, word_list


# find word inside a row going one way
def row_finder(row_matrix, words):
    # make strings for rows in word search
    row_list = make_strings(row_matrix)

    found_words_row = []
    # go through words needed to be found
    for word in words:
        i = 0
        # go through the strings made from make_strings
        for string in row_list:
            # if word is there .find returns index and append word, i + 1 for row, index + 1 for columns
            if string.find(word) != -1:
                index = string.find(word)
                found_words_row.append(word)
                found_words_row.append(i + 1)
                found_words_row.append(index + 1)
            i += 1
    return found_words_row


# find word inside the strings going the other way
def backwards_row_finder(row_matrix, words):
    # make strings for row in word search
    row_list = make_strings(row_matrix)

    # reverse the words that need to be found
    reversed_found_words_row = []
    reverse_word_list = [word[::-1] for word in words]

    # go through words that are reversed
    for word in reverse_word_list:
        i = 0
        # go through strings made from make_strings
        for string in row_list:
            # if word is found, add original word, row found + 1, and index + length of word
            if string.find(word) != -1:
                index = string.find(word)
                reversed_found_words_row.append(word[::-1])
                reversed_found_words_row.append(i + 1)
                reversed_found_words_row.append(index + len(word))
            i += 1
    return reversed_found_words_row


# make the strings necessary to find words in columns
def make_column_matrix(beginning_matrix):
    col_list = []

    # iterate for how long word seach is
    for i in range(len(beginning_matrix)):
        col = []
        # append the i index element of each row
        for row in beginning_matrix:
            col.append(row[i])

        # append the row of column indexes into col_list
        col_list.append(col)

    return col_list


# find words in the columns
def col_finder(col_matrix, words):
    # make strings out of column list
    col_list = make_strings(col_matrix)

    found_words_column = []
    found_words_column = []
    # iterate through words needed to be found
    for word in words:
        i = 0
        # iterate through the strings in the list
        for string in col_list:
            # if found append the word, the index + 1, and i + 1 for row and columns
            if string.find(word) != -1:
                index = string.find(word)
                found_words_column.append(word)
                found_words_column.append(index + 1)
                found_words_column.append(i + 1)
            i += 1
    return found_words_column


# find the words in columns going the other way
def backwards_col_finder(col_matrix, words):
    # make strings out of columns
    col_list = make_strings(col_matrix)
    # reverse words to be find
    reversed_found_words_row = []
    reverse_word_list = [word[::-1] for word in words]

    # go through each reversed word to find
    for word in reverse_word_list:
        i = 0
        # go through strings for columns in word search
        for string in col_list:
            # if found append the original word, index + length of word for row, and i + 1 for columns
            if string.find(word) != -1:
                index = string.find(word)
                reversed_found_words_row.append(word[::-1])
                reversed_found_words_row.append(index + len(word))
                reversed_found_words_row.append(i + 1)
            i += 1
    return reversed_found_words_row


# finds words going on diagonals from bottom left to top right
def diagonal_creator(big_matrix, words):
    # number of rows and length of rows
    length, row_length = len(big_matrix), len(big_matrix[0])

    diagonal_list = []
    # iterate for length of n x n -1
    for p in range(length + row_length - 1):
        inner_list = []
        # iterate for range from max of p - length + 1 or 0 to minimum of p + 1 or row length and append the element
        for q in range(max(p - length + 1, 0), min(p + 1, row_length)):
            inner_list.append(big_matrix[length - p + q - 1][q])
        # append list of diagonal elements into diagonal list
        diagonal_list.append(inner_list)

    row_list = make_strings(diagonal_list)
    found_words = []
    # iterate through words to find
    for word in words:
        counter = len(big_matrix)
        diff_counter = 1
        i = 0
        # iterate through strings made
        for string in row_list:
            # if i goes over half of matrix start adding onto different counter
            if i > (len(row_list) // 2):
                diff_counter += 1
            # if word is found
            if string.find(word) != -1:
                # if word was before or at the half diagonal of the list
                # append the word, counter + j_pos for i, and j_pos + 1
                if i <= (len(row_list) // 2):
                    j_pos = string.find(word)
                    found_words.append(word)
                    found_words.append(counter + j_pos)
                    found_words.append(j_pos + 1)
                # if word was after the half diagonal of the list
                # append the word, i_pos + 1 for i, and diff_counter + i_pos for j
                else:
                    i_pos = string.find(word)
                    found_words.append(word)
                    found_words.append(i_pos + 1)
                    found_words.append(diff_counter + i_pos)
            i += 1
            counter -= 1

    return found_words


# finds words going on diagonals from left to right backwards
def reverse_diagonal_creator(big_matrix, words):
    # reverse the words to find
    reverse_word_list = [word[::-1] for word in words]
    # length of matrix and length of row
    length, row_length = len(big_matrix), len(big_matrix[0])

    diagonal_list = []
    # iterate through p which is from the range of n x n matrix - 1
    for p in range(length + row_length - 1):
        inner_list = []
        # iterate through q which is the max of p - length of matrix +1 or 0 to the minimum of p + 1 or row_length
        # and append the element at [length - p + 1 - 1] [q]
        for q in range(max(p - length + 1, 0), min(p + 1, row_length)):
            inner_list.append(big_matrix[length - p + q - 1][q])

        diagonal_list.append(inner_list)

    # make strings out of diaognal_list
    row_list = make_strings(diagonal_list)

    found_words = []
    # iterate through the reversed list
    for word in reverse_word_list:
        counter = len(big_matrix)
        diff_counter = 1
        i = 0
        # iterate through string list
        for string in row_list:
            # if row is greater than half of the diagonals add to counter
            if i > (len(row_list) // 2):
                diff_counter += 1
            # if string is found
            if string.find(word) != -1:
                # if word was found before or at the half of the diagonals
                # append the original word, coumter + index of find + len(word -1 for row
                # and j_pos + len(word_ for column
                if i <= (len(row_list) // 2):
                    j_pos = string.find(word)
                    found_words.append(word[::-1])
                    found_words.append(counter + j_pos + len(word) - 1)
                    found_words.append(j_pos + len(word))
                # if word was found after the half of the diagonals append the original word,
                # index of find + length of word for row, and counter + index of find + length of word -1 for column
                else:
                    i_pos = string.find(word)
                    found_words.append(word[::-1])
                    found_words.append(i_pos + len(word))
                    found_words.append(diff_counter + i_pos + len(word) - 1)
            i += 1
            counter -= 1

    return found_words


# get the diagonals from top left to bottom right
def anti_diag(big_matrix, words):
    # length of matrix and of row
    length, row_length = len(big_matrix), len(big_matrix[0])

    diagonal_list = []
    # iterate through p which p is equal to range n + n -1
    for p in range(length + row_length - 1):
        inner_list = []
        # iterate through q which q is equal to the range from max of p - length + 1 or 0
        # and min of p + 1 and length of row
        for q in range(max(p - length + 1, 0), min(p + 1, row_length)):
            inner_list.append(big_matrix[p - q][q])
        diagonal_list.append(inner_list)

    # make strings out of diagonal list
    row_list = make_strings(diagonal_list)

    found_words = []
    # iterate through words to find
    for word in words:
        counter = 0
        diff_counter = 1
        i = 0
        # iterate through strings in list
        for string in row_list:
            # if counter is greater than the diagonal at half start adding counter
            if i > (len(row_list) // 2):
                diff_counter += 1
            # if word is found
            if string.find(word) != -1:
                # if it is found before the half then append the word, counter - index of find + 1 for row,
                # and index of find + 1 for column
                if i <= (len(row_list) // 2):
                    j_pos = string.find(word)
                    found_words.append(word)
                    found_words.append(counter - j_pos + 1)
                    found_words.append(j_pos + 1)
                # append the word, length of the matrix - index of find for row, and counter + index of find for column
                else:
                    i_pos = string.find(word)
                    found_words.append(word)
                    found_words.append(len(big_matrix) - i_pos)
                    found_words.append(diff_counter + i_pos)
            i += 1
            counter += 1

    return found_words


# get the diagonals from top left to bottom right going the other way
def reverse_anti_diag(big_matrix, words):
    reverse_word_list = [word[::-1] for word in words]

    # length of matrix and of row
    length, row_length = len(big_matrix), len(big_matrix[0])

    diagonal_list = []

    # iterate through p which is the range from n + n -1
    for p in range(length + row_length - 1):
        inner_list = []
        # iterate though q which is the range from the max of p = length + 1 or 0 to the min of p + 1 or row_length
        for q in range(max(p - length + 1, 0), min(p + 1, row_length)):
            inner_list.append(big_matrix[p - q][q])
        diagonal_list.append(inner_list)
    # make strings out of the diagonal list
    row_list = make_strings(diagonal_list)

    found_words = []
    # iterate through reversed words to find
    for word in reverse_word_list:
        counter = 0
        second_counter = 1
        diff_counter = 1
        i = 0
        # iterate through strings in row list
        for string in row_list:
            # after going over half of the diagonals start counter
            if i > (len(row_list) // 2):
                diff_counter += 1
            # if word is found
            if string.find(word) != -1:
                # if word was found before or at helf append the original word,
                # counter - index of find - length of word + 2 for row, and index of find + length of word for column
                if i <= (len(row_list) // 2):
                    j_pos = string.find(word)
                    found_words.append(word[::-1])
                    found_words.append(counter - j_pos - len(word) + 2)
                    found_words.append(j_pos + len(word))
                # if word was found after the half append the original word, the other counter - length of the word -
                # index of find - counter after half + 2 for row, and other counter - length of matrix + index of find
                # + length of the word for column
                else:
                    i_pos = string.find(word)
                    found_words.append(word[::-1])
                    found_words.append(second_counter - len(word) - i_pos - diff_counter + 2)
                    found_words.append(second_counter - length + i_pos + len(word))
            i += 1
            counter += 1
            second_counter += 1

    return found_words


def output_file(searched_list, words):
    # split the list into three lists of word, row index, and column index
    found_words = searched_list[0::3]
    found_words_i = searched_list[1::3]
    found_words_j = searched_list[2::3]

    # if a word was not found append it to the end of the word list
    words_not_found = []
    for word in words:
        if word not in found_words:
            words_not_found.append(word)

    # append 0, 0 for every word that was not found
    for x in range(len(words_not_found)):
        found_words_i.append(0)
        found_words_j.append(0)

    # add both word lists together
    final_words = found_words + words_not_found
    # make a 2-D list out of each word, row, and column again then sort it by word
    final_matrix = []
    for i in range(len(final_words)):
        final_matrix.append([final_words[i], str(found_words_i[i]), str(found_words_j[i])])
    sorted_final_matrix = sorted(final_matrix, key=lambda word:word[0])

    # write to the file and format
    outfile = open("found.txt", "w")
    for i in range(len(sorted_final_matrix)):
        outfile.write("{:<12}".format(sorted_final_matrix[i][0]) + "%5s" % sorted_final_matrix[i][1] +
                      "%5s" % sorted_final_matrix[i][2] + "\n")


def main():
    dimension, word_matrix, word_list = make_list()
    row = row_finder(word_matrix, word_list)
    back_row = backwards_row_finder(word_matrix, word_list)
    make_col = make_column_matrix(word_matrix)
    col = col_finder(make_col, word_list)
    back_col = backwards_col_finder(make_col, word_list)
    diag1 = diagonal_creator(word_matrix, word_list)
    diag2 = reverse_diagonal_creator(word_matrix, word_list)
    diag3 = anti_diag(word_matrix, word_list)
    diag4 = reverse_anti_diag(word_matrix, word_list)

    total = row + back_row + col+ back_col+ diag1 + diag2 + diag3 + diag4
    output_file(total, word_list)


main()

