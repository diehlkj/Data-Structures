class Node:
    def __init__(self, value=None, next_node=None)
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
        previous_head = self.head.get_value()  # ! Return value of previous head

        # * Empty head condition
        if self.head = None:
            return previous_head

        # * List with 1 elem condition
        elif self.head == self.tail:
            self.head = None
            self.tail = None

        # * List with 2+ elem condition
        else:
            self.head = self.head.get_next_node()
        
        return previous_head

    def remove_tail(self):
        previous_tail = self.tail.get_value()  # ! NOT COMPLETE, GET IT DONE

        # * Empty head condition
        if self.tail = None:
            return previous_head

        # * List with 1 elem condition
        elif self.head == self.tail:
            self.head = None
            self.tail = None

        # * List with 2+ elem condition
        else:
            self.head = self.head.get_next_node()
        
        return previous_head

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
