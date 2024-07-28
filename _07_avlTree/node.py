class Node:
    """
    Represents a node in the binary tree.

    Attributes:
        content (any): The content stored in the node.
        parent (Node, optional): The parent node.
        left (Node, optional): The left child node.
        right (Node, optional): The right child node.
    """

    def __init__(self, content, parent=None, left=None, right=None):
        """
        Initializes a Node instance.

        Args:
            content (any): The content to be stored in the node.
            parent (Node, optional): The parent node.
            left (Node, optional): The left child node.
            right (Node, optional): The right child node.
        """
        self.content = content
        self.parent = parent
        self.left = left
        self.right = right

    def set_left(self, node):
        """
        Sets the left child of the node.

        Args:
            node (Node): The node to be set as the left child.
        """
        self.left = node
        if node:
            node.parent = self

    def set_right(self, node):
        """
        Sets the right child of the node.

        Args:
            node (Node): The node to be set as the right child.
        """
        self.right = node
        if node:
            node.parent = self