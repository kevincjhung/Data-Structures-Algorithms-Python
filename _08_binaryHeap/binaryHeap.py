class BinaryHeap:
    def __init__(self, heap_type='min'):
        """
        Initialize a new BinaryHeap.

        :param heap_type: Type of heap ('min' for min-heap or 'max' for max-heap).
        """
        self.heap = []
        self.heap_type = heap_type  # 'min' for min-heap, 'max' for max-heap

  