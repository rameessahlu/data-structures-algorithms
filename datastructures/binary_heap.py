
#BinaryHeap
class MaxHeap:
    def __init__(self):
        self.heap = []

    def parent(self, pos):
        return ((pos-1)//2)

    def left_child(self, pos):
        return ((2*pos) + 1)

    def right_child(self, pos):
        return ((2*pos) + 2)

    def heap_size(self):
        return len(self.heap)

    def _get(self, pos):
        return self.heap[pos]

    def _get_max(self):
        if self.heap_size() == 0:
            return None
        else:
            return self.heap[0]

    def swap(self, x, y):
        self.heap[x], self.heap[y] = self.heap[y], self.heap[x]

    def insert(self, value):
        pos = self.heap_size()
        self.heap.append(value)

        while(pos != 0):
            parent_pos = self.parent(pos)

            if self.heap[parent_pos] < self.heap[pos]:
                self.swap(pos, parent_pos)

            pos = parent_pos

    def delete_max(self):
        if self.heap_size() == 0:
            return None
        largest = self._get_max()
        self.heap[0] = self.heap[-1]
        del self.heap[-1]
        self.max_heapify(0)
        return largest

    def max_heapify(self, i):
        l = self.left_child(i)
        r = self.right_child(i)
        if (l <= self.heap_size() - 1 and self._get(l) > self._get(i)):
            largest = l
        else:
            largest = i
        if (r <= self.heap_size() - 1 and self._get(r) > self._get(largest)):
            largest = r
        if (largest != i):
            self.swap(largest, i)
            self.max_heapify(largest)

class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, pos):
        return ((pos-1)//2)

    def left_child(self, pos):
        return ((2*pos) + 1)

    def right_child(self, pos):
        return ((2*pos) + 2)

    def heap_size(self):
        return len(self.heap)

    def _get(self, pos):
        return self.heap[pos]

    def _get_min(self):
        if self.heap_size() == 0:
            return None
        else:
            return self.heap[0]

    def swap(self, x, y):
        self.heap[x], self.heap[y] = self.heap[y], self.heap[x]

    def insert(self, value):
        pos = self.heap_size()
        self.heap.append(value)

        while(pos != 0):
            parent_pos = self.parent(pos)

            if self.heap[parent_pos] > self.heap[pos]:
                self.swap(pos, parent_pos)

            pos = parent_pos

    def delete_min(self):
        if self.heap_size() == 0:
            return None
        smallest = self._get_min()
        self.heap[0] = self.heap[-1]
        del self.heap[-1]
        self.min_heapify(0)
        return smallest

    def min_heapify(self, i):
        l = self.left_child(i)
        r = self.right_child(i)
        if (l <= self.heap_size() - 1 and self._get(l) < self._get(i)):
            smallest = l
        else:
            smallest = i
        if (r <= self.heap_size() - 1 and self._get(r) < self._get(smallest)):
            smallest = r
        if (smallest != i):
            self.swap(smallest, i)
            self.max_heapify(smallest)

max_heap = MaxHeap()
max_heap.insert(50)
max_heap.insert(30)
max_heap.insert(20)
max_heap.insert(15)
max_heap.insert(10)
max_heap.insert(8)
max_heap.insert(16)

print(max_heap.heap)

max_heap.insert(60)

print(max_heap.heap)

max_heap.delete_max()

print(max_heap.heap)
