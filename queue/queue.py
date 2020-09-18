"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""


class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        # what attributes do we need?
        self.head = None
        self.tail = None

    def add_to_head(self, value):
        # ? create new node
        new_node = Node(value)

        if self.head is None:  # * Condition for new list
            # ? Update head and tail attributes
            self.head = new_node
            self.tail = new_node

        else:  # * Condition for list containing an item
            # ? Set next_node of new node to head
            new_node.set_next_node(self.head)
            # ? Update head attribute
            self.head = new_node

    def add_to_tail(self, value):
        # * Create new node
        new_node = Node(value)

        # * Empty list condition
        if self.head is None:
            # * Update head and tail attributes
            self.head = new_node
            self.tail = new_node

        # * Non empty list condition
        else:
            # * Update next_node of current tail to new node
            self.tail.set_next_node(new_node)
            # * Update tail
            self.tail = new_node

    def remove_head(self):

        # * Empty head condition
        if self.head is None:
            return None

        else:
            prev_head = self.head.get_value()

            # * List with 1 elem condition
            if self.head == self.tail:
                self.head = None
                self.tail = None

            # * List with 2+ elem condition
            else:
                self.head = self.head.get_next_node()

            return prev_head

    def remove_tail(self):

        # * Empty Tail condition
        if self.tail is None:
            return None

        else:
            prev_tail = self.tail.get_value()

            # * List with 1 elem condition
            if self.head == self.tail:
                self.head = None
                self.tail = None

            # * List with 2+ elem condition
            else:
                self.tail = self.head

        return prev_tail

    def contains(self, value):
        current_node = self.head

        # * Loop through LL untill pointer is None
        while current_node.get_next_node() is not None:
            # * If value found
            if current_node.get_value() == value:
                return True

        return False

    def get_max(self):
        # TODO time permitting
        pass

    def get_Count(self):
        temp = self.head  # Initialise temp
        count = 0  # Initialise count

        # Loop while end of linked list is not reached
        while (temp):
            count += 1
            temp = temp.next_node
        return count


class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.storage.get_Count()

    def enqueue(self, value):
        self.storage.add_to_tail(value)
        self.size = self.storage.get_Count()
        print(f"Size in Push: {self.size}")
        print(f"Len in Push: {self.storage.get_Count()}")

    def dequeue(self):
        if self.size == 0:
            return None
        else:
            self.size = self.size - 1
            return self.storage.remove_head()
