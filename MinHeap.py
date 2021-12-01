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
        Raises a ValueError for types other than int, float, and str.
        """
        return None

    def clear(self):
        """ Removes all elements from the heap."""
        self.root = None
        self.last = None
        return None