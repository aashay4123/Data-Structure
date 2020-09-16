class Node:
    def __init__(self, value):
        self.info = value
        self.link = None


class SingleLinkedList:
    def __init__(self):
        self.start = None

    def display_list(self):
        if self.start is None:
            print("List is empty!!")
            return
        else:
            print("List is: ")
            p = self.start
            while p is not None:
                print(p.info, " ")
                p = p.link
            print()

    def count_nodes(self):
        p = self.start
        n = 0
        while p is not None:
            n += 1
            p = p.link
        print("Number of nodes:", n)

    def search(self, data):
        position = 1
        p = self.start
        while p is not None:
            if p.info == data:
                print(data, " is at position ", position)
                return True
            position += 1
            p = p.link
        else:
            print(data + " is Not found in List")
            return False

    def insert_start(self, data):
        temp = Node(data)
        temp.link = self.start
        self.start = temp

    def insert_end(self, data):
        temp = Node(data)
        if self.start is None:
            self.start = temp
            return
        p = self.start
        while p.link is not None:
            p = p.link
        p.link = temp

    def create_list(self):
        n = int(input("Enter number of nodes to create:"))
        if n == 0:
            return
        for _ in range(n):
            data = input("Enter the element to insert")
            self.insert_end(data)

    def insert_after(self, data, x):
        p = self.start
        while p is not None:
            if p.info == x:
                break
            p = p.link
        if p is None:
            print(x, " Not found in list")
        else:
            temp = Node(data)
            temp.link = p.link
            p.link = temp

    def insert_before(self, data, k):
        if self.start is None:
            print("List is empty")
            return
        if k == self.start.info:
            temp = Node(data)
            temp.link = self.start

    def insert_at_position(self, data, k):
        pass

    def delete_node(self, data):
        pass

    def delete_first(self):
        pass

    def delete_last(self):
        pass

    def reverse_list(self):
        pass

    def bubble_sort_exdata(self):
        pass

    def bubble_sort_exlinks(self):
        pass

    def find_cycle(self):
        pass

    def has_cycle(self):
        pass

    def insert_cycle(self, data):
        pass

    def remove_cycle(self):
        pass

    def merge2(self, list2):
        pass

    def _merge2(self, p1, p2):
        pass

    def merge_sort_rec(self, lineStart):
        pass

    def _divide_list(self, p):
        pass


list = SingleLinkedList()
data = int(input("Enter the element:"))
list.create_list()
list.insert_start(data)
list.insert_end(data)
list.count_nodes()
list.display_list()
list.search(data)
