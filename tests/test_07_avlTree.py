import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from _07_avlTree.avlTree import AVLTree

class TestAVLTree(unittest.TestCase):
    def test_create_node(self):
        pass

if __name__ == '__main__':
    unittest.main()