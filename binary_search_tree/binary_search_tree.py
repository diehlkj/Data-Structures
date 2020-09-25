"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

! When returning in recursive functions, you shouldn't just call the function again
! you should return it, that way when you exit the loop it doesnt return None
? https://stackoverflow.com/questions/17778372/why-does-my-recursive-function-return-none

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                return self.left.insert(value)

        if value >= self.value:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                return self.right.insert(value)
    
    # ! Recursive Example:
        # ? if value < Root
            # ? if left child is None
                # * insert here
            # ? else
                # * call insert on next tree
        # ? if value >= Root, go right
            # ? if right child is None
                # * insert here
            # ? else
                # * call insert on next tree
                
    # ! Iterative Example:
        # ? While not at end of tree
            # ? if value < Root, go left
                # ? if left child is none
                    # * exit loop
                    # * insert here

            # ? if value >= Root, go right
                # ? if right child is none
                    # * exit loop
                    # * insert here

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # print(f"Target: {target} | Self: {self.value}\n")
        if target == self.value:
            # print(f"{self.value} IS {target} | RETURN TRUE\n")
            return True
        else:
            if target < self.value:
                if self.left is None:
                    # print(f"{self.value} IS NOT {target} | RETURN FALSE\n")
                    return False
                else:
                    # print(f"{self.value} IS NOT {target} | going LEFT\n")
                    return self.left.contains(target)
            if target > self.value:
                if self.right is None:
                    # print(f"{self.value} IS NOT {target} | RETURN FALSE\n")
                    return False
                else:
                    # print(f"{self.value} IS NOT {target} | going RIGHT\n")
                    return self.right.contains(target)
            
        # ? if self.value is target
            # ? if yes 
                # * return True
            # ? if no
                # ? go left
                # ? go right

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right is None:
            return self.value
        else:
            return self.right.get_max()
        
        # ? Go right until right is None
            # * Return the value of final branch of right


    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        if self.left is not None:
            self.left.for_each(fn)
        if self.right is not None:
            self.right.for_each(fn)
        return fn(self.value)
    
        # ? Once side then the other...
            # * Returns fn(self.value)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        if self.left is None and self.right is None:
            return print(self.value)
        else:
            if self.left is not None:
                self.left.in_order_print()
            print(self.value)
            if self.right is not None:
                self.right.in_order_print()

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        q = []
        q.append(self)
        while q:
            if q[0].left is not None:
                q.append(q[0].left)
            
            if q[0].right is not None:
                q.append(q[0].right)
                
            print(q[0].value)
            del q[0]

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        # ? Create stack to keep track of nodes being searched
        # ? PUSH 'self' into stack when we start branch
        stk = []
        stk.insert(0, self)
        
        # ? While something is still in the stack (Not dont processing)            
            # ? Use exisiting for_each() as refrence for taversal Logic
            # ? POP node from stack when we are done processing that nodes sub branches
            # ? and dont forget to call 'print()'
        while stk:
            # ? PUSH node when we start processing
            if stk[0].left is not None:
                stk.insert(0, stk[0].left)
                
                if stk[0].right is not None:
                    stk.insert(0, stk[0].right)
                else:
                    print(stk[0].value)
            else:
                print(stk[0].value)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self):
        pass

"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

bst.bft_print()
# bst.dft_print()

# print("elegant methods")
# print("pre order")
# bst.pre_order_dft()
# print("in order")
# bst.in_order_dft()
# print("post order")
# bst.post_order_dft()  
