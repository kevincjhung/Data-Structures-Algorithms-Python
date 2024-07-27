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
        if value is None:
            raise TypeError("Cannot insert None into the binary tree.")
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

    def _find_min(self, node: Node) -> Node:
        """
        Finds the node with the minimum value in a subtree.
        Args:
            node (Node): The root of the subtree.
        Returns:
            Node: The node with the minimum value.
        """

        while node.left:
            node = node.left
        return node
    

    def search(self, value):
        """
        Searches for a value in the binary search tree.

        Args:
            value (any): The value to search for.

        Returns:
            Node: The node containing the value, or None if not found.
        """
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        """
        Helper function for recursive search of a value in the binary tree.

        Args:
            node (Node): The current node.
            value (any): The value to search for.

        Returns:
            Node: The node containing the value, or None if not found.
        """
        if node is None or node.content == value:
            return node
        if value < node.content:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value)

    def delete(self, value):
        """
        Deletes a value from the binary search tree.

        Args:
            value (any): The value to delete.
        """
        node_to_delete = self.search(value)
        if node_to_delete:
            self._delete_node(node_to_delete)

    def _delete_node(self, node):
        """
        Helper function to delete a node from the binary tree.

        Args:
            node (Node): The node to delete.
        """
        # Node has no children
        if not node.left and not node.right:
            if node == self.root:
                self.root = None
            elif node == node.parent.left:
                node.parent.left = None
            else:
                node.parent.right = None

        # Node has one child
        elif not node.left:
            if node == self.root:
                self.root = node.right
            elif node == node.parent.left:
                node.parent.left = node.right
            else:
                node.parent.right = node.right
            node.right.parent = node.parent
        elif not node.right:
            if node == self.root:
                self.root = node.left
            elif node == node.parent.left:
                node.parent.left = node.left
            else:
                node.parent.right = node.left
            node.left.parent = node.parent

        # Node has two children
        else:
            successor = self._find_min(node.right)
            node.content = successor.content
            self._delete_node(successor)

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
