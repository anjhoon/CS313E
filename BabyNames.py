#  File: BabyNames.py
#  Description: Creates a menu that gives info on baby name rankings through a dictionary
#  Student Name: Andrew Chen
#  Student UT EID: ac68644
#  Course Name: CS 313E
#  Unique Number: 50210
#  Date Created: 9/9/19
#  Date Last Modified: 9/13/19


# search up a name in the dictionary
def search_name(name, dictionary):
    name = name.capitalize()
    return name in dictionary


# returns a list of all ranks for a particular name
def name_rank(name, dictionary):
    name = name.capitalize()
    rank_list = []
    # if name is in dictionary add rank to list
    if name in dictionary:
        for i in dictionary[name]:
            # turn 1001 back to 0
            if i == 1001:
                rank_list.append("0")
            # add rank
            else:
                rank_list.append(str(i))
        return rank_list
    else:
        return


# return a list of sorted names that appear in a particular decade
def one_decade(decade, dictionary):
    # get index of value for particular decade
    year = decade % 1900 // 10
    names = {}
    ranks = [value[year] for value in dictionary.values() if value[year] != 1001]

    # add key value pair to names dictionary if the rank is in top 1000
    for name, value in dictionary.items():
        if value[year] != 1001:
            names[name] = value[year]

    # sort dictionary keys in ascending order by values
    sorted_names = sorted(names.items(), key=lambda rank: rank[1])

    for names in sorted_names:
        print(names[0] + ':', names[1])


# return names if values were in top 1000 every decade
def all_decades(dictionary):
    names = []
    for name, value in dictionary.items():
        count = 0
        for rank in value:
            # if rank was not outside 1000
            if rank != 1001:
                count += 1
        # if there were values for all decades add name to list
        if count == 11:
            names.append(name)
    names.sort()
    return names


# return a list of names that got more popular over time
def more_popular(dictionary):
    names = []

    for name, values in dictionary.items():
        for i in range(len(values) - 1):
            # if rank of first was less than rank of second (higher rank means less popular) stop for loop
            if values[i] <= values[i + 1]:
                break
            # if iterated all the way to second to last one add to list
            # don't need to iterate to last since it would eventually go out of index by comparing i + 1
            if i == (len(values) - 2):
                names.append(name)

    return names


# return a list of names that got less popular over time
def less_popular(dictionary):
    names = []

    for name, values in dictionary.items():
        for i in range(len(values) - 1):
            # if rank of first was greater than rank of second (lower rank means more popular) stop for loop
            if values[i] >= values[i + 1]:
                break
            # if iterated all the way to second to last one add to list
            # don't need to iterate to last since it would eventually go out of index by comparing i + 1
            if i == (len(values) - 2):
                names.append(name)
    return names


def main():
    name_dict = {}

    # open file
    infile = open("names.txt", "r")

    # read file line by line
    for line in infile:
        name = line.strip().split()

        # iterate through list and change where element == 0 to 1001
        for i in range(1, len(name)):
            name[i] = int(name[i])
            if name[i] == 0:
                name[i] = 1001

        # add key value pair into empty dictionary
        name_dict.update({name[0]: name[1:]})

    infile.close()

    menu = True

    # loop menu
    while menu:
        print("Enter 1 to search for baby names. ")
        print("Enter 2 to display all rankings for one name.")
        print("Enter 3 to display all names that appear in a decade.")
        print("Enter 4 to display names that appear in all decades.")
        print("Enter 5 to display names that are more popular in every decade.")
        print("Enter 6 to display all names that are less popular in every decade.")
        print("Enter 7 to quit the program.")

        # try the input
        try:
            choice = int(input("Choose an option: "))

            # if user wants to see if name is in dictionary
            if choice == 1:
                name = input("Enter a name to search: ").capitalize()
                # if search_name returns True print that the name is in dictionary
                if search_name(name, name_dict):
                    year = 1900
                    # list comprehension for finding index of value when value equals highest rank
                    high = [i for i, value in enumerate(name_dict[name]) if value == min(name_dict[name])]
                    # list comprehension for making a list of decades
                    maximum = [year + index * 10 for index in high]
                    print("\nThe matches with their highest ranking decade are:")
                    print(name, end=' ')
                    for number in maximum:
                        print(number, end=' ')

                    print()
                    print()
                # if search_name returns False print that the name is not in dictionary
                else:
                    print(name, "does not appear in any decade.\n")

            # if user wants to show all data for one name
            elif choice == 2:
                name = input("Enter a name to search: ").capitalize()
                print()
                rank = name_rank(name, name_dict)
                years = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000]
                i = 0

                # if name is not in dictionary
                if not rank:
                    print(name, "is not in the dictionary.")
                # join together list of strings from name_rank
                else:
                    ranking = " ".join(rank)
                    name_ranking = name + ": " + ranking
                    print(name_ranking)

                    # print the year and rank
                    for year in years:
                        print(str(year) + ": " + rank[i])
                        i += 1
                    print()

            # if user wants to show names in order by rank for particular decade
            elif choice == 3:
                decade = int(input("Enter decade: "))
                print("The names are in order of rank:")
                one_decade(decade, name_dict)

            # if user wants names that appear during every decade
            elif choice == 4:
                all_names = all_decades(name_dict)
                print(len(all_names), "names that appear in every decade. They are: ")
                for name in all_names:
                    print(name)
                print()

            # if user wants the names that got more popular every decade
            elif choice == 5:
                popular = more_popular(name_dict)
                print(len(popular), "names are getting more popular in every decade: ")
                for name in popular:
                    print(name)
                print()

            # if user wants the names that got less popular every decade
            elif choice == 6:
                not_popular = less_popular(name_dict)
                print(len(not_popular), "names are getting less popular: ")
                for name in not_popular:
                    print(name)
                print()

            # if user wants to quit
            elif choice == 7:
                print("\nGoodbye.")
                menu = False

        # catch if value entered was not a number
        except ValueError:
            print("Not a number. Please enter a number. \n")


main()
