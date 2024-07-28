from .node import Node


class AVLTree:
    def __init__(self):
        self.root = None

    def get_height(self, node: Node) -> int:
        """Return the height of the node."""
        return node.height if node else 0

    def get_balance_factor(self, node: Node) -> int:
        """Return the balance factor of the node."""
        return self.get_height(node.left) - self.get_height(node.right) if node else 0

    def right_rotate(self, y: Node) -> Node:
        """Perform a right rotation on the given node."""
        x = y.left
        t2 = x.right

        # Perform rotation
        x.right = y
        y.left = t2

        # Update heights
        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1
        x.height = max(self.get_height(x.left), self.get_height(x.right)) + 1

        # Return the new root
        return x

    def left_rotate(self, x: Node) -> Node:
        """Perform a left rotation on the given node."""
        y = x.right
        t2 = y.left

        # Perform rotation
        y.left = x
        x.right = t2

        # Update heights
        x.height = max(self.get_height(x.left), self.get_height(x.right)) + 1
        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1

        # Return the new root
        return y

    def insert(self, key: int) -> None:
        """Insert a key into the AVL tree."""
        self.root = self._insert(self.root, key)

    def _insert(self, node: Node, key: int) -> Node:
        """Helper method to insert a key into the subtree rooted with node."""
        if not node:
            return Node(key)

        if key < node.content:
            node.left = self._insert(node.left, key)
        elif key > node.content:
            node.right = self._insert(node.right, key)
        else:
            # Duplicate keys are not allowed
            return node

        # Update height of the current node
        node.height = max(self.get_height(node.left), self.get_height(node.right)) + 1

        # Check balance factor and balance the tree if needed
        balance = self.get_balance_factor(node)

        # Left Left Case
        if balance > 1 and key < node.left.content:
            return self.right_rotate(node)

        # Right Right Case
        if balance < -1 and key > node.right.content:
            return self.left_rotate(node)

        # Left Right Case
        if balance > 1 and key > node.left.content:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

        # Right Left Case
        if balance < -1 and key < node.right.content:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node

    def get_min_value_node(self, node: Node) -> Node:
        """Return the node with the smallest key value found in that tree."""
        if node is None or node.left is None:
            return node
        return self.get_min_value_node(node.left)

    def delete(self, key: int) -> None:
        """Delete a key from the AVL tree."""
        self.root = self._delete(self.root, key)

    def _delete(self, node: Node, key: int) -> Node:
        """Helper method to delete a key from the subtree rooted with node."""
        if not node:
            return node

        if key < node.content:
            node.left = self._delete(node.left, key)
        elif key > node.content:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None or node.right is None:
                node = node.left if node.left else node.right
            else:
                temp = self.get_min_value_node(node.right)
                node.content = temp.content
                node.right = self._delete(node.right, temp.content)

        if not node:
            return node

        node.height = max(self.get_height(node.left), self.get_height(node.right)) + 1
        balance = self.get_balance_factor(node)

        # Left Left Case
        if balance > 1 and self.get_balance_factor(node.left) >= 0:
            return self.right_rotate(node)

        # Left Right Case
        if balance > 1 and self.get_balance_factor(node.left) < 0:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

        # Right Right Case
        if balance < -1 and self.get_balance_factor(node.right) <= 0:
            return self.left_rotate(node)

        # Right Left Case
        if balance < -1 and self.get_balance_factor(node.right) > 0:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node

    def in_order_traversal(self, node: Node, result: list = None) -> list:
        """Helper method to perform in-order traversal of the tree."""
        if result is None:
            result = []
        if node:
            self.in_order_traversal(node.left, result)
            result.append(node.content)
            self.in_order_traversal(node.right, result)
        return result

    def get_in_order_traversal(self) -> list:
        """Return in-order traversal of the AVL tree."""
        return self.in_order_traversal(self.root)

    def is_balanced_tree(self, node: Node = None) -> bool:
        """
        Check if the tree is balanced starting from the given node.

        Args:
            node (Node): The starting node to check balance. If None, start from the root.

        Returns:
            bool: True if the tree is balanced, False otherwise.
        """
        if node is None:
            node = self.root
        return self._is_balanced_tree(node)

    def _is_balanced_tree(self, node: Node) -> bool:
        """
        Helper method to check if the tree is balanced starting from the given node.

        Args:
            node (Node): The node to check balance.

        Returns:
            bool: True if the subtree rooted at the node is balanced, False otherwise.
        """
        if not node:
            return True

        left_height = self.get_height(node.left)
        right_height = self.get_height(node.right)
        balance_factor = abs(left_height - right_height)

        if balance_factor > 1:
            return False

        return self._is_balanced_tree(node.left) and self._is_balanced_tree(node.right)

    def search(self, key: int) -> Node:
        """Search for a node with the given key in the AVL tree."""
        return self._search(self.root, key)

    def _search(self, node: Node, key: int) -> Node:
        """Helper method to search for a key in the subtree rooted with node."""
        if not node or node.content == key:
            return node

        if key < node.content:
            return self._search(node.left, key)

        return self._search(node.right, key)
