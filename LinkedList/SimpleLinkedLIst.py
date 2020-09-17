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
            self.start = temp
            return
        p = self.start
        while p.link is not None:
            if p.link.info == k:
                break
            p = p.link
        if p.link is None:
            print(k, "is not present in the list")
        else:
            temp = Node(data)
            temp.link = p.link
            p.link = temp

    def insert_at_position(self, data, k):
        if k == 1:
            temp = Node(data)
            temp.link = self.start
            self.start = temp
            return
        p = self.start
        i = 1
        while i < k-1 and p is not None:
            p = p.link
            i += 1
        if p is None:
            print("you can insert upto position ", i)
        else:
            temp = Node(data)
            temp.link = p.link
            p.link = temp

    def delete_node(self, data):
        if self.start is None:
            print("List is empty")
            return
        p = self.start
        while p.link is not None:
            if p.link.info == data:
                break
            p = p.link
        if p.link is None:
            print("element ", data, " not found in list")
        else:
            p.link = p.link.link

    def delete_first(self):
        if self.start:
            return
        self.start = self.start.link

    def delete_last(self):
        if self.start is None:
            return
        if self.start.link is None:
            self.start = None
            return
        p = self.start
        while p.link is not None:
            p = p.link
        p = None

    def reverse_list(self):
        prev = None
        p = self.start
        while p is not None:
            next = p.link
            p.link = prev
            prev = p
            p = next
        self.start = prev

    def bubble_sort_exdata(self):
        end = None
        while end != self.start.link:
            p = self.start
            while p.link != end:
                q = p.link
                if(p.info > q.info):
                    p.info, q.info = q.info, p.info
                p = p.link
            end = p

    def bubble_sort_exlinks(self):
        end = None
        while end != self.start.link:
            r = p = self.start
            while p.link != end:
                q = p.link
                if(p.info > q.info):
                    p.link = q.link
                    q.link = p
                    if p != self.start:
                        r.link = q
                    else:
                        self.start = q
                    p, q = q, p
                r = p
                p = p.link
            end = p

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
list.insert_after(122, data)
list.insert_before(152, data)
list.count_nodes()
list.insert_at_position(443, 3)
list.reverse_list()
list.delete_first()
list.delete_last()
list.delete_node(data)
# list.bubble_sort_exdata()/
# list.bubble_sort_exlinks()
list.display_list()
list.search(data)
