#  File: Josephus.py

#  Description: Utilize a circular linked list to find the last link left after deleting links one by one

#  Student Name: Andrew Chen

#  Student UT EID: ac68644

#  Partner Name: Saaketh Palchuru

#  Partner UT EID: srp2992

#  Course Name: CS 313E

#  Unique Number: 50210

#  Date Created: 10/31/19

#  Date Last Modified: 11/4/19


class Link(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class CircularList(object):
    # Constructor
    def __init__(self):
        self.first = None

    # Insert an element (value) in the list
    def insert(self, data):
        new_link = Link(data)
        current = self.first

        if current == None:
            self.first = new_link
            self.first.next = new_link
            return

        while current.next != self.first:
            current = current.next

        current.next = new_link
        new_link.next = self.first

    # Find the link with the given data (value)
    def find(self, data):

        current = self.first

        if current == None:
            return False

        while current.data != data:
            current = current.next

        return current

    # Delete a link with a given data (value)
    def delete(self, data):
        current = self.first
        previous = self.first

        if current == None:
            return

        # if data is in the first link
        if self.first.data == data:
            while previous.next != self.first:
                previous = previous.next
            previous.next = current.next
            self.first = previous.next
            return current
        # if data is not in the first link
        else:
            while current.next != self.first:
                previous = current
                current = current.next
                if current.data == data:
                    previous.next = current.next

                    return current

    # Delete the nth link starting from the Link start
    # Return the next link from the deleted Link
    def delete_after(self, start, n):

        current = self.find(start)

        if current.data == current.next.data:
            print(current.data)
            self.delete(current.data)
            return

        for i in range(n-1):
            current = current.next

        print(current.data)
        self.delete(current.data)

        return current.next

    # Return a string representation of a Circular List
    def __str__(self):

        current = self.first
        string = ''
        if current == None:
            return

        # traverse until we reach the starting link
        while current.next != self.first:
            string += str(current.data)
            string += '\n'
            current = current.next

        if current.next == self.first:
            string += str(current.data)

        return string


def main():
    infile = open('josephus.txt', 'r')

    number = int(infile.readline())
    start = int(infile.readline())
    elimination = int(infile.readline())
    infile.close()

    soldiers = CircularList()

    for i in range(1, number+1):
        soldiers.insert(i)

    start = soldiers.delete_after(start, elimination)
    while soldiers.first.next != soldiers.first:
        start = soldiers.delete_after(start.data, elimination)

    print(soldiers)


main()
