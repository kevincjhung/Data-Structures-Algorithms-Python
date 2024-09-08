import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from _07_avlTree.avlTree import AVLTree

class TestAVLTreeInsertion:
    def setup_method(self):
        self.tree = AVLTree()

    def test_insert_single_node(self):
        self.tree.insert(1)
        assert self.tree.root is not None
        assert self.tree.root.content == 1
        assert self.tree.root.left is None
        assert self.tree.root.right is None

    def test_multiple_insertions(self):
        for key in [1, 2, 3, 4, 5, 6]:
            self.tree.insert(key)
        result = self.tree.get_in_order_traversal()
        assert result == [1, 2, 3, 4, 5, 6]

    def test_maintain_balance_after_insertion(self):
        keys = [10, 20, 30, 40, 50, 25]
        for key in keys:
            self.tree.insert(key)
        assert self.tree.is_balanced_tree()

    def test_no_duplicate_keys(self):
        self.tree.insert(1)
        self.tree.insert(1)
        result = self.tree.get_in_order_traversal()
        assert result == [1]


class TestAVLTreeTraversal:
    def setup_method(self):
        self.tree = AVLTree()
    
    def test_in_order_tree_traversal(self):
        keys = [10, 20, 5, 6, 15, 30]
        for key in keys:
                self.tree.insert(key)

        result = self.tree.get_in_order_traversal()
        assert result == sorted(keys)

class TestAVLTreeRotation:
    def setup_method(self):
        self.tree = AVLTree()
    
    def test_left_rotation(self):
        # Insert keys in a way that makes it right heavy
        keys = [10, 20, 30]

        for key in keys:
            self.tree.insert(key)
        
        assert self.tree.root.content == 20
        assert self.tree.root.left.content == 10
        assert self.tree.root.right.content == 30


    def test_right_rotation(self):
        # Insert keys in a way that makes it left heavy
        keys = [30, 20, 10]  # This will cause an imbalance at the root, requiring a right rotation

        for key in keys:
            self.tree.insert(key)

        # After insertion, the tree should be balanced and the new root should be 20
        assert self.tree.root.content == 20
        assert self.tree.root.left.content == 10
        assert self.tree.root.right.content == 30

        # Check if the tree is balanced
        assert self.tree.is_balanced_tree()

    def test_left_right_rotation(self):
        # Insert keys in a way that requires a left-right rotation
        keys = [30, 10, 20]  # This will cause an imbalance at the root's left child, requiring a left-right rotation

        for key in keys:
            self.tree.insert(key)

        # After insertion, the tree should be balanced and the new root should be 20
        assert self.tree.root.content == 20
        assert self.tree.root.left.content == 10
        assert self.tree.root.right.content == 30

        # Check if the tree is balanced
        assert self.tree.is_balanced_tree()

    def test_right_left_rotation(self):
        # Insert keys in a way that requires a right-left rotation
        keys = [10, 30, 20]  # This will cause an imbalance at the root's right child, requiring a right-left rotation

        for key in keys:
            self.tree.insert(key)

        # After insertion, the tree should be balanced and the new root should be 20
        assert self.tree.root.content == 20
        assert self.tree.root.left.content == 10
        assert self.tree.root.right.content == 30

        # Check if the tree is balanced
        assert self.tree.is_balanced_tree()


class TestAVLTreeDeletion:
    def setup_method(self):
        self.tree = AVLTree()
    
    def test_delete_node_with_single_child(self):
        # Insert keys to 
        keys = [10, 5, 15, 3, 7, 12, 18, 6]
        
        for key in keys:
            self.tree.insert(key)
            
        # Delete node with single child
        self.tree.delete(7)
        
        # Check in-order traversal after deletion
        expected = [3, 5, 6, 10, 12, 15, 18]
        assert self.tree.get_in_order_traversal() == expected
        
        # Check balance of the tree
        assert self.tree.is_balanced_tree()

    def test_delete_node_with_two_children(self):
        keys = [10, 5, 15, 3, 7, 12, 18, 6, 8]

        for key in keys:
            self.tree.insert(key)
        
        # Delete node with two children
        self.tree.delete(5)
        
        
class TestAVLTreeSearch:
    def setup_tree(self):
        self.tree = AVLTree()
        # Insert some nodes into the tree
        for key in [10, 5, 15, 3, 7, 13, 17]:
            self.tree.insert(key)

    def test_search_node_present(self):
        pass

    def test_search_node_not_present(self):
        pass
        
if __name__ == '__main__':
    unittest.main()