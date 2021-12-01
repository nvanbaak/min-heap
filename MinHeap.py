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

    def __init__(self):
        self.root = None
        self.last = None
        self.next_open = None

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
        Raises a ValueError for types other than int, float, and str.
        """
        # type checking
        if not (isinstance(data, int) 
                or isinstance(data, float)
                or isinstance(data, str)):
            raise ValueError("This MinHeap only supports int, float, and str.")

        if self.root == None: # trivial case, empty heap
            # store data in root, set as last inserted
            n = self.HeapNode()
            n.value = data
            self.root = n
            self.last = n

            # create empty node for next_open
            next_node = self.HeapNode()
            n.left = next_node
            next_node.is_left = True
            self.next_open = next_node
            return

        current = self.root
        while current:
            return None

    def clear(self):
        """ Removes all elements from the heap."""
        self.root = None
        self.last = None
        self.next_open = None
        return None