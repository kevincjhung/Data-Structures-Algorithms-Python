import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from _06_binaryTree.binaryTree import Node, BinaryTree


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


    def test_insert_multiple_values(self):
        values = [10, 5, 15, 3, 7, 12, 18]
        for value in values:
            self.tree.insert(value)

        # Check if the values are correctly inserted and the BST property is maintained
        # We will perform an in-order traversal to get a sorted list of values
        sorted_values = list(self.tree.in_order_traversal())

        self.assertEqual(sorted_values, sorted(values))

        # Additional checks to verify tree structure
        # This is more complex, so it could be expanded based on specific needs
        self.assertEqual(self.tree.root.content, 10)
        self.assertEqual(self.tree.root.left.content, 5)
        self.assertEqual(self.tree.root.right.content, 15)
        self.assertEqual(self.tree.root.left.left.content, 3)
        self.assertEqual(self.tree.root.left.right.content, 7)
        self.assertEqual(self.tree.root.right.left.content, 12)
        self.assertEqual(self.tree.root.right.right.content, 18)

    def test_search_existing_values(self):
        values = [10, 5, 15, 3, 7, 12, 18]
        for value in values:
            self.tree.insert(value)

        # Search for each value and verify that it exists
        for value in values:
            result = self.tree.search(value)
            self.assertIsNotNone(result)
            self.assertEqual(result.content, value)

    def test_search_non_existing_values(self):
        values = [10, 5, 15, 3, 7, 12, 18]

        for value in values:
            self.tree.insert(value)

        # Search for values that are not in the tree
        non_existing_values = [1, 2, 4, 6, 8, 20, 25]

        for value in non_existing_values:
            result = self.tree.search(value)
            self.assertIsNone(result)

    # Test deleting a leaf node (a node with no children)
    def test_delete_leaf_node(self):
        values = [10, 5, 15, 3, 7]
        for value in values:
            self.tree.insert(value)

        self.tree.delete(7)  # Deleting a leaf node

        # Verify that the node with value 7 is deleted
        result = self.tree.search(7)
        self.assertIsNone(result)

        # Verify that the parent node is updated correctly
        self.assertIsNone(self.tree.root.left.right)

    # Test deleting a node with one child
    def test_delete_node_with_one_child(self):
        values = [10, 5, 15, 3, 7, 6]
        for value in values:
            self.tree.insert(value)

        self.tree.delete(7)  # Node 7 has one child (node 6)

        # Verify that the node with value 7 is deleted
        result = self.tree.search(7)
        self.assertIsNone(result)

        # Verify that node 6 has replaced node 7
        self.assertEqual(self.tree.root.left.right.content, 6)


    # Test deleting a node with two children
    def test_delete_node_with_two_children(self):
        values = [10, 5, 15, 3, 7, 12, 18]
        for value in values:
            self.tree.insert(value)

        self.tree.delete(5)  # Node 5 has two children (nodes 3 and 7)

        # Verify that the node with value 5 is deleted
        result = self.tree.search(5)
        self.assertIsNone(result)

        # Verify that the node with value 7 has replaced node 5, and the tree structure is updated correctly
        self.assertEqual(self.tree.root.left.content, 7)
        self.assertEqual(self.tree.root.left.left.content, 3)
        # The right child of the node with value 7 should remain None since there was no node 6 in the initial values
        self.assertIsNone(self.tree.root.left.right)

    # Test deleting the root node
    def test_delete_root_node(self):
        values = [10, 5, 15, 3, 7, 12, 18]
        for value in values:
            self.tree.insert(value)

        self.tree.delete(10)  # Deleting the root node

        # Verify that the root node is deleted
        result = self.tree.search(10)
        self.assertIsNone(result)

        # Verify that the new root is correct
        new_root = self.tree.root
        self.assertEqual(new_root.content, 12)  # In this case, 12 should become the new root

        # Verify the new left and right subtrees
        self.assertEqual(new_root.left.content, 5)
        self.assertEqual(new_root.left.left.content, 3)
        self.assertEqual(new_root.left.right.content, 7)

        self.assertEqual(new_root.right.content, 15)
        self.assertIsNone(new_root.right.left)  # The left child of node 15 should be None since 12 was moved
        self.assertEqual(new_root.right.right.content, 18)

    # Test deleting a node that doesn't exist
    def test_delete_node_that_does_not_exist(self):
        values = [10, 5, 15, 3, 7]
        for value in values:
            self.tree.insert(value)

        self.tree.delete(20)  # Attempting to delete a node that doesn't exist

        # Verify that the tree structure is unchanged
        self.assertEqual(self.tree.root.content, 10)
        self.assertEqual(self.tree.root.left.content, 5)
        self.assertEqual(self.tree.root.right.content, 15)
        self.assertEqual(self.tree.root.left.left.content, 3)
        self.assertEqual(self.tree.root.left.right.content, 7)

    # Test in-order traversal on an empty tree.
    def test_in_order_traversal_empty(self):
        return_array = list(self.tree.in_order_traversal())
        self.assertEqual(return_array, [])
            
        
    # Test in-order traversal on a tree with multiple nodes.
    def test_in_order_traversal(self):
        values = [10, 5, 15, 3, 7]
        
        for value in values: 
            self.tree.insert(value)
        
        expected_order = [3, 5, 7, 10, 15]
        return_array = list(self.tree.in_order_traversal())

        self.assertEqual(return_array, expected_order)


    # Test the behavior when inserting None.
    def test_insert_none(self):
        with self.assertRaises(TypeError):
            self.tree.insert(None)


# Test deleting from an empty tree.


if __name__ == "__main__":
    unittest.main()
