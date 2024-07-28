class Node:
    def __init__(self, key: int):
        """
        Initialize a node with a given key.

        Args:
            key (int): The key for the node.
        """
        self.content = key
        self.left = None
        self.right = None
        self.height = 1

    def set_left(self, left_node: 'Node') -> None:
        """
        Set the left child of the node.

        Args:
            left_node (Node): The left child node.
        """
        self.left = left_node

    def set_right(self, right_node: 'Node') -> None:
        """
        Set the right child of the node.

        Args:
            right_node (Node): The right child node.
        """
        self.right = right_node

    def __str__(self) -> str:
        """
        Return a string representation of the node.

        Returns:
            str: String representation of the node.
        """
        return f'Node({self.content})'

    def __repr__(self) -> str:
        """
        Return a detailed string representation of the node.

        Returns:
            str: Detailed string representation of the node.
        """
        return f'Node(content={self.content}, left={self.left}, right={self.right}, height={self.height})'
