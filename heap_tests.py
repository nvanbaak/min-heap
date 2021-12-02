import unittest
from MinHeap import MinHeap

class MyHeapTests(unittest.TestCase):
    """
    Suite of tests for MinHeap
    """
    def test_constructor(self):
        mh = MinHeap()

        if not mh: self.assertFalse(True, "MinHeap failed instantiation")
        self.assertEqual(mh.root, None)
        self.assertEqual(mh.last, None)

    def test_insert_bad_type(self):
        mh = MinHeap()

        lists_are_not_supported = []
        self.assertRaises(TypeError, mh.insert, lists_are_not_supported)

    def test_insert_empty_heap(self):
        mh = MinHeap()

        mh.insert(4)
        self.assertEqual(mh.root.value, 4)
        self.assertEqual(mh.root.parent, None)
        self.assertEqual(mh.root.left, None)
        self.assertEqual(mh.root.right, None)
        self.assertEqual(mh.root.is_left, None)
        self.assertEqual(mh.last.value, 4)

    def test_insert_multiple(self):
        mh = MinHeap()

        mh.insert(8)
        mh.insert(3)
        mh.insert(5)
        mh.insert(9)
        mh.insert(1)
        mh.insert(2)

        # if the bubbling works properly, we should get:
        #     1 
        #  3     2
        # 9 8   5

        self.assertEqual(mh.last.value, 5, "self.last not properly set")
        self.assertEqual(mh.root.left.left.value, 9, "Did not find proper value")
        self.assertEqual(mh.root.right.value, 2, "Did not find proper value")
        self.assertTrue(mh.root.left.is_left, "left/right bool not set properly")
        self.assertFalse(mh.root.left.right.is_left, "left/right bool not set properly")
        self.assertEqual(mh.last.parent.value, 2, "self.last parent not set properly")

    def test_peek_empty_heap(self):
        mh = MinHeap()

        self.assertEqual(mh.peek(), None)

    def test_peek_heap_with_items(self):
        mh = MinHeap()
        mh.insert("tactical")

        self.assertEqual(mh.peek(), "tactical")

    def test_clear(self):
        mh = MinHeap()

        mh.insert(8)
        mh.insert(3)
        mh.insert(5)
        mh.insert(9)
        mh.insert(1)
        mh.insert(2)

        mh.clear()

        self.assertEquals(mh.root, None)

    def test_pop_empty_heap(self):
        mh = MinHeap()

        self.assertEquals(mh.pop(), None)
        self.assertEquals(mh.root, None)

    def test_pop_once(self):
        mh = MinHeap()

        mh.insert(8)
        mh.insert(4)
        mh.insert(7)
        mh.insert(6)
        mh.insert(5)
        mh.insert(1)

        # we should end up with this:
        #     1
        #   5   4
        #  8 6 7

        self.assertEquals(mh.pop(), 1)

        # after pop, we should have this:
        #    4
        #  5   7
        # 8 6

        self.assertEquals(mh.root.right.value, 7)
        self.assertEquals(mh.root.left.value, 5)
        self.assertEquals(mh.last.value, 6)

    def test_pop_multiple(self):
        mh = MinHeap()

        mh.insert(8)
        mh.insert(4)
        mh.insert(7)
        mh.insert(6)
        mh.insert(5)
        mh.insert(1)

        # Tree should look like this:
        #     1
        #   5   4
        #  8 6 7

        self.assertEquals(mh.pop(), 1)
        #     4
        #   5   7
        #  8 6
        self.assertEquals(mh.pop(), 4)
        #     5
        #   6   7
        #  8
        self.assertEquals(mh.pop(), 5)
        #    6
        #  8   7

        self.assertEquals(mh.peek(), 6)
        self.assertEquals(mh.last.value, 7)
        self.assertEquals(mh.root.left.value, 8)


if __name__ == "__main__":
    unittest.main()