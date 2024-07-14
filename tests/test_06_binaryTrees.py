import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from _06_binaryTree.binaryTree import (
    Node, BinaryTree
)



# TODO: initialization tests
  # create a node with children

  # create a node without children

# TODO: insertion tests
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