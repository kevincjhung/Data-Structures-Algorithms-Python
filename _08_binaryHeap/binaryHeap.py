class BinaryHeap:
    def __init__(self, heap_type='min'):
        """
        Initialize a new BinaryHeap.

        :param heap_type: Type of heap ('min' for min-heap or 'max' for max-heap).
        """
        self.heap = []
        self.heap_type = heap_type  # 'min' for min-heap, 'max' for max-heap

    def _parent(self, index):
        """
        Return the index of the parent of the given index.

        :param index: The index of the child.
        :return: The index of the parent.
        """
        return (index - 1) // 2

    def _left_child(self, index):
        """
        Return the index of the left child of the given index.

        :param index: The index of the parent.
        :return: The index of the left child.
        """
        return 2 * index + 1

    def _right_child(self, index):
        """
        Return the index of the right child of the given index.

        :param index: The index of the parent.
        :return: The index of the right child.
        """
        return 2 * index + 2

    def _compare(self, child_value, parent_value):
        """
        Compare child and parent values based on heap type.

        :param child_value: The value of the child node.
        :param parent_value: The value of the parent node.
        :return: True if the child and parent values should be swapped.
        """
        if self.heap_type == 'min':
            return child_value < parent_value
        elif self.heap_type == 'max':
            return child_value > parent_value
        else:
            raise ValueError("heap_type must be 'min' or 'max'")

    def _heapify_up(self, index):
        """
        Move the element at the given index up the heap to maintain the heap property.

        :param index: The index of the element to move.
        """
        parent_index = self._parent(index)
        
        while index > 0 and self._compare(self.heap[index], self.heap[parent_index]):
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            index = parent_index
            parent_index = self._parent(index)

    def _heapify_down(self, index):
        """
        Move the element at the given index down the heap to maintain the heap property.

        :param index: The index of the element to move.
        """
        size = len(self.heap)
        
        while True:
            left_index = self._left_child(index)
            right_index = self._right_child(index)
            smallest_or_largest = index
            
            if left_index < size and self._compare(self.heap[left_index], self.heap[smallest_or_largest]):
                smallest_or_largest = left_index
            if right_index < size and self._compare(self.heap[right_index], self.heap[smallest_or_largest]):
                smallest_or_largest = right_index
            
            if smallest_or_largest != index:
                self.heap[index], self.heap[smallest_or_largest] = self.heap[smallest_or_largest], self.heap[index]
                index = smallest_or_largest
            else:
                break

    def insert(self, value):
        """
        Insert a new value into the heap.

        :param value: The value to insert.
        """
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def extract_root(self):
        """
        Remove and return the root value from the heap.

        :return: The root value of the heap.
        :raises IndexError: If the heap is empty.
        """
        if not self.heap:
            raise IndexError("extract_root from an empty heap")

        root_value = self.heap[0]
        last_value = self.heap.pop()
        if self.heap:
            self.heap[0] = last_value
            self._heapify_down(0)
        
        return root_value

    def peek(self):
        """
        Return the root value without removing it.

        :return: The root value of the heap.
        :raises IndexError: If the heap is empty.
        """
        if not self.heap:
            raise IndexError("peek from an empty heap")
        return self.heap[0]

    def __len__(self):
        """
        Return the number of elements in the heap.

        :return: The number of elements in the heap.
        """
        return len(self.heap)

    def __str__(self):
        """
        Return a string representation of the heap.

        :return: String representation of the heap.
        """
        return str(self.heap)

