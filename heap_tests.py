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

        booleans_not_supported = True
        self.assertRaises(TypeError, mh.insert, booleans_not_supported)

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

        self.assertEquals(mh.last.value, 5, "self.last not properly set")
        self.assertEquals(mh.root.left.left.value, 9, "Did not find proper value")
        self.assertEquals(mh.root.right.value, 2, "Did not find proper value")
        self.assertTrue(mh.root.left.is_left, "left/right bool not set properly")
        self.assertFalse(mh.root.left.right.is_left, "left/right bool not set properly")
        self.assertEquals(mh.last.parent.value, 2, "self.last parent not set properly")


if __name__ == "__main__":
    unittest.main()