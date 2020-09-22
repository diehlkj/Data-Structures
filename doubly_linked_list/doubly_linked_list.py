"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
    
    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next

    def get_prev_node(self):
        return self.prev

    def set_next_node(self, new_next):
        self.next = new_next

    def set_prev_node(self, new_prev):
        self.prev = new_prev
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 0 if node is None else 1

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        
        new_head = ListNode(value)                  # ? Make a new List Node
        
        if self.head is None:
            self.head = new_head
            self.tail = new_head
        else:
            old_head = self.head                    # ? Get the current head
            old_head.set_prev_node(new_head)        # ? Point the current head backwards to the new head
            new_head.set_next_node(self.head)       # ? Point the new head forward to the current head
            self.head = new_head                    # ? Replace the current head with the new head
        self.length += 1
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        if self.head is None:
            return None
        else:
            old_head = self.head                    # ? Get the current head
            if self.head.get_next_node() is None:
                self.head = None
                self.tail = None
            else:
                new_head = self.head.get_next_node()# ? Get the first node after head
                new_head.set_prev_node(None)        # ? Point the new head backwards to None
                self.head = new_head                # ? Replace the current head with the new head
            self.length -= 1
            return old_head.get_value()              # ? Return the value of the old head
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        
        new_tail = ListNode(value)                  # ? Make a new List Node
        
        if self.head is None:
            self.head = new_tail
            self.tail = new_tail
        else:
            old_tail = self.tail                    # ? Get the current tail
            old_tail.set_next_node(new_tail)        # ? Point the current tail forward to the new tail
            new_tail.set_prev_node(old_tail)       # ? Point the new tail backwards to the current tail
            self.tail = new_tail                    # ? Replace the current tail with the new tail
        self.length += 1
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        if self.tail is None:
            return None
        else:
            old_tail = self.tail                    # ? Get the current tail
            if self.tail.get_prev_node() is None:
                self.head = None
                self.tail = None
            else:
                new_tail = self.tail.get_prev_node()# ? Get the first node after tail
                new_tail.set_next_node(None)        # ? Point the new tail backwards to None
                self.tail = new_tail                # ? Replace the current tail with the new tail
            self.length -= 1
            return old_tail.get_value()              # ? Return the value of the old tail
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        if self.head is not node:                       # ? If given node is not head
                                                        # ? Get next of given node if not None
            next_of_node = node.get_next_node() if node.get_next_node is not None else None
            
            prev_of_node = node.get_prev_node()         # ? Get prev of given node
            old_head = self.head                        # ? Get current head

            if next_of_node is not None:                # ? Point former and latter of given node to each other if given is not tail
                next_of_node.set_prev_node(prev_of_node)
                prev_of_node.set_next_node(next_of_node)
            else:                                       # ? Point former of given node forwards to None
                prev_of_node.set_next_node(None)        # ? Point former of given node forwards to None
                self.tail = prev_of_node                # ? Set tail to former of given node
                
            node.set_next_node(old_head)                # ? Point given node forward to current head
            node.set_prev_node(None)                    # ? Set prev of given node to None
            old_head.set_prev_node(node)                # ? Point current head backwards to new head
            self.head = node                            # ? Set head to given node
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if self.tail is not node:                       # ? If given node is not tail
            next_of_node = node.get_next_node()         # ? Get next of given node
                                                        # ? Get prev of given node if not None
            prev_of_node = node.get_prev_node() if node.get_prev_node is not None else None
            
            old_tail = self.tail                        # ? Get current tail

            if prev_of_node is not None:                # ? Point former and latter of given node to each other if given is not head
                next_of_node.set_prev_node(prev_of_node)
                prev_of_node.set_next_node(next_of_node)
            else:                                       
                next_of_node.set_prev_node(None)        # ? Point former of given node forwards to None
                self.head = next_of_node                # ? Set head to latter of given node
                
            node.set_prev_node(old_tail)                # ? Point given node backwards to current tail
            node.set_next_node(None)                    # ? Set next of given node to None
            old_tail.set_next_node(node)                # ? Point current tail forwards to new tail
            self.tail = node                            # ? Set tail to given node

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        if self.head is node and self.tail is node:
            self.head = None
            self.tail = None
            self.length -= 1
        elif self.head is node:
            self.remove_from_head()
        elif self.tail is node:
            self.remove_from_tail()
        else:
            next_of_node = node.get_next_node()         # ? Get next of given node
            prev_of_node = node.get_prev_node()         # ? Get prev of given node
            next_of_node.set_prev_node(prev_of_node)    # ? Point latter of given node to former
            prev_of_node.set_next_node(next_of_node)    # ? Point former of given node to latter
            self.length -= 1

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        if self.head is None:
            return None
        
        cur_node = self.head  # * Initialise temp
        maxVal = self.head.value  # * Initialise count

        # * Loop while end of linked list is not reached
        while (cur_node):
            if cur_node.value > maxVal:
                maxVal = cur_node.value
            cur_node = cur_node.next
        return maxVal
    
    def get_count(self):
        temp = self.head  # * Initialise temp
        count = 0  # * Initialise count

        # * Loop while end of linked list is not reached
        while (temp):
            count += 1
            temp = temp.next
        return count