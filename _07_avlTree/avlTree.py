from .node import Node

class AVLTree:
    """
    Represents a binary tree.

    Attributes:
        root (Node): The root node of the binary tree.
    """

    def __init__(self):
        """Initializes an AVL instance."""
        self.root = None

    def create_node(self, content):
        """
        Creates a new node with the given content.

        Args:
            content (any): The content to be stored in the node.

        Returns:
            Node: The newly created node.
        """
        return Node(content)
    