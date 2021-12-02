# Nik Van Baak / 501 / 1 Dec 2021

class MinHeap():
    """
    A node-based implementation of a MinHeap.
    """
    class HeapNode():
        """
        Nodes store one datum and links to other nodes in the heap.
        """
        def __init__(self):
            self.parent = None
            self.left = None
            self.right = None
            self.value = None
            self.is_left = None

        def is_smaller_than_kids(self):
            """
            Returns False if the node has at least one child node with a smaller value.
            Otherwise, returns True.
            """
            if self.left is not None:
                if not self.value < self.left.value:
                    return False
            if self.right is not None:
                if not self.value < self.right.value:
                    return False
            return True

        def append_right(self, node):
            """
            Appends a given node to the right with appropriate linking.
            """
            self.right = node
            node.parent = self
            node.is_left = False
            return

        def append_left(self, node):
            """
            Appends a given node to the left with appropriate linking.
            """
            self.left = node
            node.parent = self
            node.is_left = True
            return

        def swap_values_with_left_child(self):
            """
            Exchanges the value of this node with its left child.
            Raises TypeError if no left child.
            """
            if self.left is None:
                raise TypeError()
            self.value, self.left.value = self.left.value, self.value
            return

        def swap_values_with_right_child(self):
            """
            Exchanges the value of this node with its right child.
            Raises TypeError if no right child.
            """
            if self.right is None:
                raise TypeError()
            self.value, self.right.value = self.right.value, self.value
            return

        def __eq__(self, other_node):
            """
            Equality operator
            """
            return self.value == other_node.value

        def __lt__(self, other_node):
            """
            Less-than operator
            """
            return self.value < other_node.value


    def __init__(self):
        self.root = None
        self.last = None

    def pop(self):
        """
        Returns and removes the minimum value from the heap.
        If the heap is empty, returns None.
        """
        if self.root is None: return None # empty heap case

        # first, grab value from root
        output = self.root.value

        # trivial case: heap has size of 1
        if self.root.left == None and self.root.right == None:
            self.clear()
            return output

        # begin by replacing root value with last insertion
        self.root.value = self.last.value

        # next, figure out where the new last is going to be once we delete the old one
        if self.last.is_left: 
            node_pointer = self.last.parent
            node_pointer.left = None

            while node_pointer.parent.is_left: # go up until we find a right child
                if node_pointer.parent is not None:
                    node_pointer = node_pointer.parent
                else: # we hit root, nowhere else to climb
                    break

            # if it's not root, hop over to the left sibling
            if node_pointer.parent is not None:
                node_pointer = node_pointer.parent.left

            # Traverse down the right until we hit an open slot
            while node_pointer.right is not None:
                node_pointer = node_pointer.right

            # we're done, it's our new last
            self.last = node_pointer

        else: # if last is a right child, new last will be its right sibling
            node_pointer = self.last.parent
            node_pointer.right = None
            self.last = node_pointer.left

        # bubble down the root value
        node_pointer = self.root
        while node_pointer.is_smaller_than_kids():

            # check for edge cases, return if encountered
            if node_pointer.left is None: return output # case: no children
            elif node_pointer.right is None: # case: one child
                if node_pointer.left.value < node_pointer.value:
                    node_pointer.swap_values_with_left_child()
                # one child means we've hit the bottom row, so return
                return output

            # move to smaller node
            if node_pointer.left <= node_pointer.right:
                node_pointer = node_pointer.left
            else: node_pointer = node_pointer.right

        # if we reached here, both children are larger, so we're done
        return output

    def peek(self):
        """
        Returns but does not remove the minimum value of the heap.
        If the heap is empty, returns None.
        """
        if self.root is None: return None # empty heap
        else: return self.root.value

    def insert(self, data):
        """
        Inserts the provided value onto the heap.
        Raises a TypeError for types other than int, float, and str.
        """
        # type checking
        if not (isinstance(data, int) 
                or isinstance(data, float)
                or isinstance(data, str)):
            raise TypeError("This MinHeap only supports int, float, and str.")

        # easy case: empty heap
        if self.root is None:
            n = self.HeapNode()
            n.value = data
            self.root = n
            self.last = n
            return

        #######
        # Using the last inserted node, we find the next open position for insertion
        #######

        # First, make a new node with the data
        n = self.HeapNode()
        n.value = data

        # if the recent-most child is on the left, the right child is open
        if self.last.is_left:
            self.last.parent.append_right(n)
            self.last = n

        else: # if the recent-most child is right, we traverse to find the next slot
            node_pointer = self.last

            # keep going up until we find root or a node that's the left child
            while not node_pointer.is_left:
                if node_pointer.parent is not None:
                    node_pointer = node_pointer.parent
                else: # pointer's at root, nowhere to go
                    break

            # if we hit a left child before root, move pointer to its right sibling
            if node_pointer.parent is not None:
                node_pointer = node_pointer.parent.right

            # The next open position should now be a straight shot down the left children
            # from our current position.
            while node_pointer.left is not None:
                node_pointer = node_pointer.left

            # Insert new node as left child
            node_pointer.append_left(n)
            self.last = n

        # now that the new node is in self.last, bubble up its value
        node_pointer = self.last

        # repeat until we hit root
        while node_pointer.parent is not None:

            # swap values if we're smaller, then move up one level
            if node_pointer < node_pointer.parent:
                node_pointer.value, node_pointer.parent.value = node_pointer.parent.value, node_pointer.value
                node_pointer = node_pointer.parent
            else: break # if the parent is smaller, we're done

        return None

    def clear(self):
        """ Removes all elements from the heap."""
        self.root = None
        self.last = None
        return None