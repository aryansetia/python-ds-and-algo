class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node 
        self.length = 1

    def print_list(self):
        temp = self.head 
        while temp is not None:
            print(temp.value, end=' ')
            temp = temp.next

    #insert at end
    def append(self, value):
        new_node = Node(value)
        if self.head == None: #list is empty
            self.head = new_node
            self.tail = new_node 
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

my_linked_list = LinkedList(5)
my_linked_list.append(7)
my_linked_list.print_list()
print('\n')
print(my_linked_list.length)
