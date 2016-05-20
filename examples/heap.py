class Heap:
    def __init__(self, items=[]):
        self.heap = items
        self.heap_size = len(self.heap)
        self.build_heap()

    def parent(self, i):
        return ((i + 1) // 2) - 1

    def left(self, i):
        return ((i + 1) << 1) - 1

    def right(self, i):
        return (i + 1) << 1 

    def heapify(self, i):
        l = self.left(i)
        r = self.right(i)
        if l < self.heap_size and self.heap[l] > self.heap[i]:
            largest = l
        else:
            largest = i
        if r < self.heap_size and self.heap[r] > self.heap[largest]:
            largest = r
        if largest != i:
            copy = self.heap[i]
            self.heap[i] = self.heap[largest]
            self.heap[largest] = copy
            return self.heapify(largest)

    def build_heap(self):
        for i in range(self.heap_size // 2 - 1, -1, -1):
            self.heapify(i)
