#  File: TestLinkedList.py

#  Description: Make a single linked list and create some methods

#  Student Name: Andrew Chen

#  Student UT EID: ac68644

#  Partner Name: Saaketh Palchuru

#  Partner UT EID: srp2992

#  Course Name: CS 313E

#  Unique Number: 50210

#  Date Created: 10/28/19

#  Date Last Modified: 11/1/19


class Link(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList(object):
    def __init__(self):
        self.first = None

    # get number of links
    def get_num_links(self):
        current = self.first
        length = 0

        if current == None:
            return length

        while current != None:
            length += 1
            current = current.next

        return length

    # add an item at the beginning of the list
    def insert_first(self, data):
        new_link = Link(data)
        new_link.next = self.first
        self.first = new_link

    # add an item at the end of a list
    def insert_last(self, data):
        new_link = Link(data)
        current = self.first

        # if list is empty
        if current == None:
            self.first = new_link
            return

        # traverse linked list until the last link
        while current.next != None:
            current = current.next

        current.next = new_link

    # add an item in an ordered list in ascending order
    def insert_in_order(self, data):
        new_link = Link(data)
        current = self.first
        previous = self.first

        # if list is empty
        if current == None:
            self.first = new_link
            return
        # if first link is larger than item
        if current.data > data:
            new_link.next = self.first
            self.first = new_link
            return

        # traverse linked list to last link
        while current.next != None:
            # if link is smaller than item
            if current.data <= data:
                previous = current
                current = current.next
            # else link item to current then link previous to item
            else:
                new_link.next = previous.next
                previous.next = new_link
                return

        # if at last link and link is less than item item is new last link
        if current.data <= data:
            current.next = new_link
        # if at last link and link is greater than item insert item before last link
        else:
            new_link.next = previous.next
            previous.next = new_link
            return

    # search in an unordered list, return None if not found
    def find_unordered(self, data):
        current = self.first

        if current == None:
            return None

        # traverse until data is found or not found
        while current.data != data:
            if current.next == None:
                return None
            else:
                current = current.next

        return current

    # Search in an ordered list, return None if not found
    def find_ordered(self, data):
        current = self.first

        if current == None:
            return None

        # traverse list until list's data is greater than data to find
        while current.data != data:
            if current.data > data:
                return None
            else:
                current = current.next

        return current

    # Delete and return Link from an unordered list or None if not found
    def delete_link(self, data):
        previous = self.first
        current = self.first

        if current == None:
            return None

        # traverse until you find or don't find data
        while current.data != data:
            if current.next == None:
                return None
            else:
                previous = current
                current = current.next

        # if linked list is on first link
        if current == self.first:
            self.first = self.first.next
        # else delete the link
        else:
            previous.next = current.next

        return current

    # String representation of data 10 items to a line, 2 spaces between data
    def __str__(self):

        current = self.first
        string = ''
        item = 0
        counter = 0

        if current == None:
            return string

        while current != None:

            string += str(current.data)
            current = current.next
            item += 1
            counter += 1

            if item == 10:
                string += '\n'
                item = 0
            elif counter == self.get_num_links():
                return string
            else:
                string += '  '

    # Copy the contents of a list and return new list
    def copy_list(self):
        new_list = LinkedList()
        current = self.first

        # traverse until the current is None to insert every link
        while current != None:
            new_list.insert_last(current.data)
            current = current.next

        return new_list

    # Reverse the contents of a list and return new list
    def reverse_list(self):
        new_list = LinkedList()
        current = self.first

        # insert the data into linked list in first position every time
        while current != None:
            new_list.insert_first(current.data)
            current = current.next

        return new_list

    # Sort the contents of a list in ascending order and return new list
    def sort_list(self):
        new_list = LinkedList()
        current = self.first

        while current != None:
            new_list.insert_in_order(current.data)
            current = current.next

        return new_list

    # Return True if a list is sorted in ascending order or False otherwise
    def is_sorted(self):
        current = self.first

        # check if next link's data is greater than current links data
        while current.next != None:
            if current.next.data <= current.data:
                return False
            else:
                current = current.next

        return True

    # Return True if a list is empty or False otherwise
    def is_empty(self):

        # check if first link is None
        if self.first == None:
            return True
        return False

    # Merge two sorted lists and return new list in ascending order
    def merge_list(self, other):
        new_list = LinkedList()
        current1 = self.first
        current2 = other.first

        # if first is empty return a copy of the other list
        if self.is_empty():
            return other.copy_list()
        # if second is empty return a copy of the first list
        elif other.is_empty():
            return self.copy_list()
        elif self.is_empty() and other.is_empty():
            return new_list

        # if both linked lists have links
        while current1 != None and current2 != None:

            if current1.data <= current2.data:
                new_list.insert_last(current1.data)
                current1 = current1.next
            elif current2.data < current1.data:
                new_list.insert_last(current2.data)
                current2 = current2.next

        # if only one linked list still has links
        while current1 != None:
            new_list.insert_last(current1.data)
            current1 = current1.next

        # if only the other linked list still has links
        while current2 != None:
            new_list.insert_last(current2.data)
            current2 = current2.next

        return new_list

    # Test if two lists are equal, item by item and return True
    def is_equal(self, other):
        current1 = self.first
        current2 = other.first

        # if one is empty and the other is not return False
        if current1 == None and current2 != None:
            return False
        elif current1 != None and current2 == None:
            return False

        # if both have links traverse and see if each is equal
        while current1 != None and current2 != None:
            if current1.data != current2.data:
                return False
            else:
                current1 = current1.next
                current2 = current2.next
        return True

    # Return a new list, keeping only the first occurrence of an element
    # and removing all duplicates. Do not change the order of the elements.
    def remove_duplicates(self):
        new_list = LinkedList()
        current = self.first

        # if list is empty return empty linked list
        if self.is_empty():
            return new_list

        # if linked list is not empty check if the new list has the data, if not then add it to the list
        while current != None:
            if new_list.find_unordered(current.data) == None:
                new_list.insert_last(current.data)
            current = current.next

        return new_list


def main():
    testList = [56, 84, 32, 91, 27, 45, 88, 36, 19, 23, 48, 54]
    testList2 = [21, 36, 1, 34, 86, 34, 90, 85, 64, 21, 21]
    testList3 = [31, 51, 5, 31, 90, 87, 58, 44, 39, 68, 75]

    # Test methods insert_first() and __str__() by adding more than
    # 10 items to a list and printing it.
    lst1 = LinkedList()
    for item in testList:
        lst1.insert_first(item)
    print('test insert_first')
    print(lst1)
    print()

    # Test method insert_last()
    lst2 = LinkedList()
    for item in testList:
        lst2.insert_last(item)
    print('test insert_last')
    print(lst2)
    print()

    # Test method insert_in_order()
    lst3 = LinkedList()
    for item in testList:
        lst3.insert_in_order(item)
    print('test insert_in_order')
    print(lst3)
    print()

    # Test method get_num_links()
    lst4 = LinkedList()
    lst5 = LinkedList()
    for item in testList:
        lst4.insert_last(item)
    print("test method get_num_links")
    print(lst4.get_num_links())
    print(lst5.get_num_links())
    print()

    # Test method find_unordered()
    # Consider two cases - data is there, data is not there
    lst5 = LinkedList()

    for item in testList:
        lst5.insert_last(item)
    print("Test method findUnordered")
    print(lst5.find_unordered(95) != None)
    print(lst5.find_unordered(95) == None)
    print()

    # Test method find_ordered()
    # Consider two cases - data is there, data is not there
    lst6 = LinkedList()

    for item in testList:
        lst6.insert_in_order(item)
    print("Test method findOrdered")
    print(lst6.find_ordered(28) != None)
    # item there
    print(lst6.find_ordered(28) == None)
    print()

    # Test method delete_link()
    # Consider two cases - data is there, data is not there

    lst7 = LinkedList()

    for item in testList:
        lst7.insert_last(item)

    print("Test method delete")
    # Consider two cases - item is there, item is not there
    # item not there
    print('Current list')
    print(lst7)
    print('Can delete 23?')
    print(lst7.delete_link(23) != None)
    print(lst7)
    # item there
    print('Can delete 23?')
    print(lst7.delete_link(23) != None)
    print('No, 23 is not there anymore')
    print(lst7)
    print()

    # Test method copy_list()
    lst8 = LinkedList()

    for item in testList:
        lst8.insert_first(item)
    print('testing copy_list')
    print(lst8)
    print('next is copy')
    print(lst8.copy_list())
    print()

    # Test method reverse_list()
    lst9 = LinkedList()

    for item in testList:
        lst9.insert_first(item)
    print('testing reverse_list')
    print(lst9)
    print('next is reversed')
    print(lst9.reverse_list())
    print()

    # Test method sort_list()
    lst10 = LinkedList()

    for item in testList:
        lst10.insert_first(item)
    print('testing sort_list')
    print(lst10)
    print('next is sorted')
    print(lst10.sort_list())
    print()

    # Test method is_sorted()
    # Consider two cases - list is sorted, list is not sorted
    lst11 = LinkedList()
    lst12 = LinkedList()

    for item in testList:
        lst11.insert_first(item)
        lst12.insert_in_order(item)

    print('testing is_sorted')
    print(lst11)
    print(lst11.is_sorted())
    print(lst12)
    print(lst12.is_sorted())
    print()
    # Test method is_empty()
    lst13 = LinkedList()
    lst14 = LinkedList()

    for item in testList:
        lst13.insert_first(item)

    print('testing is_empty')
    print(lst13.is_empty())
    print(lst14.is_empty())
    print()

    # Test method merge_list()

    list19 = LinkedList()
    for item in testList:
        list19.insert_in_order(item)

    merge = LinkedList()
    for item in testList3:
        merge.insert_in_order(item)

    print("Test method mergeList")
    print(list19.merge_list(merge))
    print()

    # Test method is_equal()
    # Consider two cases - lists are equal, lists are not equal
    lst15 = LinkedList()
    for item in testList:
        lst15.insert_in_order(item)

    lst16 = LinkedList()
    for item in testList:
        lst16.insert_in_order(item)

    lst17 = LinkedList()
    lst18 = LinkedList()

    # Test method isEqual()
    print("testing method is_equal")
    print(lst15)
    print(lst16)

    # Consider two cases - lists are equal, lists are not equal
    print(lst15.is_equal(lst16))
    print(lst15.is_equal(lst17))
    print(lst16.is_equal(lst17))
    print(lst17.is_equal(lst18))
    print()

    # Test remove_duplicates()
    lst18 = LinkedList()
    for item in testList2:
        lst18.insert_last(item)
    print('testing remove duplicates')
    print(lst18)
    print('after removing duplicates')
    print(lst18.remove_duplicates())



if __name__ == "__main__":
    main()
