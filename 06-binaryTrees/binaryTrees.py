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


class BinaryTree:
    """
    Represents a binary tree.

    Attributes:
        root (Node): The root node of the binary tree.
    """

    def __init__(self):
        """Initializes a BinaryTree instance."""
        self.root = None

    def insert(self, value):
        """
        Inserts a new value into the binary search tree.

        Args:
            value (any): The value to insert.
        """
        if not self.root:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        """
        Helper function for recursive insertion of value into the binary tree.

        Args:
            node (Node): The current node.
            value (any): The value to insert.
        """
        if value < node.content:
            if not node.left:
                node.set_left(Node(value))
            else:
                self._insert_recursive(node.left, value)
        else:
            if not node.right:
                node.set_right(Node(value))
            else:
                self._insert_recursive(node.right, value)

    def in_order_traversal(self):
        """
        Performs an in-order traversal of the binary tree.

        Yields:
            any: The content of each node in the tree, in in-order sequence.
        """
        yield from self._in_order_recursive(self.root)

    def _in_order_recursive(self, node):
        """
        Helper function for recursive in-order traversal of the binary tree.

        Args:
            node (Node): The current node.

        Yields:
            any: The content of each node in in-order sequence.
        """
        if node:
            yield from self._in_order_recursive(node.left)
            yield node.content
            yield from self._in_order_recursive(node.right)


# Example usage
if __name__ == "__main__":
    tree = BinaryTree()
    tree.insert(5)
    tree.insert(3)
    tree.insert(7)

    print("In-order Traversal: ", list(tree.in_order_traversal()))  # Output: [3, 5, 7]
