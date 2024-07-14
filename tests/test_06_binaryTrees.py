import os
import sys
import unittest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from _06_binaryTree.binaryTree import (
    Node, BinaryTree
)



# TODO: initialization tests
  # create a node with children
  
class TestNode(unittest.TestCase):
    def setUp(self):
        self.parent = Node(10)
        self.left_child = Node(5)
        self.right_child = Node(15)
        self.parent.set_left(self.left_child)
        self.parent.set_right(self.right_child)
    
    def tearDown(self):
        self.parent = None
        self.left_child = None
        self.right_child = None

    def test_node_initialization_with_children(self):
        self.assertEqual(self.parent.content, 10)
        self.assertEqual(self.parent.left.content, 5)
        self.assertEqual(self.parent.right.content, 15)
        self.assertEqual(self.left_child.parent, self.parent)
        self.assertEqual(self.right_child.parent, self.parent)
    
    def test_node_initialization_without_children(self):
        node = Node(10)
        self.assertEqual(node.content, 10)
        self.assertIsNone(node.parent)
        self.assertIsNone(node.left)
        self.assertIsNone(node.right)


class TestBinaryTree(unittest.TestCase):
    def setUp(self):
        self.tree = BinaryTree()

    def tearDown(self):
        self.tree = None

    def test_insert_single_value(self):
        self.tree.insert(10)
        self.assertIsNotNone(self.tree.root)
        self.assertEqual(self.tree.root.content, 10)
        self.assertIsNone(self.tree.root.left)
        self.assertIsNone(self.tree.root.right)
        
        
  # insert a single value into the tree

  # insert multiple values and make sure the BST property is maintained

# TODO: search tests
  # search for values in the tree

  # search for values NOT in the tree

# TODO: delete tests
  # Test deleting a leaf node (a node with no children)

  # Test deleting a node with one child
   
  # Test deleting a node with two children`
   
  # Test deleting the root node
   
  # Test deleting a node that doesn't exist

# TODO: traversal tests
  # Test in-order traversal on an empty tree.

  # Test in-order traversal on a tree with multiple nodes.

  # Ensure the traversal output is in sorted order.

# TODO: edge cases
  # Test the behavior when inserting None.

  # Test operations on an initially empty tree.

  # Test deleting from an empty tree.



if __name__ == '__main__':
    unittest.main()
