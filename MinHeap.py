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
        if self.root == None: # ie heap is empty
            return None
        else:
            output = self.root.value

            # TODO: remove root value, replace with last value, and bubble down

            return output

    def peek(self):
        """
        Returns but does not remove the minimum value of the heap.
        If the heap is empty, returns None.
        """
        if self.root == None: # empty heap
            return None

        else:
            return self.root.value

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
        if self.root == None:
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
        self.bubble_up_last()

        return None

    def clear(self):
        """ Removes all elements from the heap."""
        self.root = None
        self.last = None
        return None

    def bubble_up_last(self):
        """
        Called after insertion operation.
        Bubbles up the value in self.last until it's larger than its parent node.
        """

        node_pointer = self.last

        # repeat until we hit root
        while node_pointer.parent is not None:

            # swap values if we're smaller, then move up one level
            if node_pointer < node_pointer.parent:
                node_pointer.value, node_pointer.parent.value = node_pointer.parent.value, node_pointer.value
                node_pointer = node_pointer.parent

            else: # if the parent is smaller, we're done
                break

        return None