from typing import Any, List

class MinHeap:

    def __init__(self, capacity: int = 50):
        """Constructor creating an empty heap with default capacity = 50 but allows heaps of other capacities to be created."""
        self.heap: List = [0]*(capacity+1)     # index 0 not used for heap
        self.num_items = 0

    def enqueue(self, item: Any) -> None:
        """inserts "item" into the heap
        Raises IndexError if there is no room in the heap"""
        if self.is_full() == True:
            raise IndexError
        else:
            # print(self.size())
            self.num_items += 1
            self.heap[self.num_items] = item
            print(self.num_items)
            # self.heap.append(item)
            self.perc_up(self.num_items)

    def peek(self) -> Any:
        """returns root of heap (highest priority) without changing the heap
        Raises IndexError if the heap is empty"""
        if self.is_empty() == True:
            raise IndexError
        else:
            # self.perc_up(self.heap[self.size()])
            print(f"size: {self.size()}")
            print(f"what i perc: {self.heap[self.size()]}")
            print(f"perc: {self.heap}")
            # return self.heap[self.size()]
            return self.heap[1]
        # so i cant do perc down or perc up?

    def dequeue(self) -> Any:
        """returns item at root (highest priority) - removes it from the heap and restores the heap property
           Raises IndexError if the heap is empty"""
        if self.is_empty() == True:
            raise IndexError
        else:
            last = self.heap[self.size()]  # Swap last item with first item
            size = self.size()
            # print(f"last: {self.heap[self.size()]}")
            first = self.heap[1]
            self.heap[1] = last
            # self.heap.pop(last)
            # print(f"size l: {self.size()}")
            # print(self.heap)
            self.num_items -= 1  # Reduce heap size
            self.perc_down(1)  # drift down
            # print(f"last after: {self.heap[self.size()]}")
            # print(self.heap)
            return first

    def contents(self) -> List:
        """returns a list of contents of the heap in the order it is stored internal to the heap.
        (This may be useful for in testing your implementation.)
        If heap is empty, returns empty list []"""
        if self.is_empty() == True:
            return []
        else:
            return self.heap[1:self.size() + 1]

    def build_heap(self, alist: List) -> None:
        """Discards the items in the current heap and builds a heap from
        the items in alist using the bottom up method.
        If the capacity of the current heap is less than the number of
        items in alist, the capacity of the heap will be increased to accommodate the items in alist"""
        # print(f"heap before: {self.heap}")
        if self.capacity() < len(alist):
            # print(self.capacity())
            self.heap = [0] * (len(alist) + 1)
        i = len(alist) // 2
        self.num_items = len(alist)
        self.heap[1:len(alist) + 1] = alist
        # print(f"heap{self.heap}")
        while (i > 0):
            self.perc_down(i)
            i = i - 1
        # print(f"heap after: {self.heap}")

    def is_empty(self) -> bool:
        """returns True if the heap is empty, false otherwise"""
        if self.size() == 0:
            return True
        else:
            return False

    def is_full(self) -> bool:
        """returns True if the heap is full, false otherwise"""
        if self.capacity() == self.size():
            return True
        else:
            return False

    def capacity(self) -> int:
        """This is the maximum number of a entries the heap can hold, which is
        1 less than the number of entries that the array allocated to hold the heap can hold"""
        # print(self.heap.index(self.heap[-1]))
        return len(self.heap) - 1
        # return 50

    def size(self) -> int:
        """the actual number of elements in the heap, not the capacity"""
        return self.num_items

    def perc_down(self,i: int) -> None:
        """where the parameter i is an index in the heap and perc_down moves the element stored
        at that location to its proper place in the heap rearranging elements as it goes."""
        done = False
        while not done and 2 * i <= self.size():  # at least one child
            c1 = 2 * i  # Child 1
            c2 = c1 + 1  # Child 2
            if c2 <= self.size() and self.heap[c1] > self.heap[c2]:  # Two children and c2 is smaller
                if self.heap[i] > self.heap[c2]:
                    self.heap[i], self.heap[c2] = self.heap[c2], self.heap[i]
                    i = c2
                else:
                    done = True
            else:  # One child, or c1 is smaller
                if self.heap[i] > self.heap[c1]:
                    self.heap[i], self.heap[c1] = self.heap[c1], self.heap[i]
                    i = c1
                else:
                    done = True


    def perc_up(self,i: int) -> None:
        """where the parameter i is an index in the heap and perc_up moves the element stored
        at that location to its proper place in the heap rearranging elements as it goes."""
        parent = i // 2
        while parent > 0 and self.heap[i] < self.heap[parent]:
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            i = parent
            parent = i // 2


    def heap_sort_ascending(self, alist: List) -> None:
        """perform heap sort on input alist in ascending order
        This method will discard the current contents of the heap, build a new heap using
        the items in alist, and mutate (change contents of) alist to put the items in ascending order"""
        self.build_heap(alist)
        #Every parent has to be less than children
        size = len(alist) - 1
        print(f"heap before : {self.heap[:self.num_items + 1] }")
        print(self.num_items)
        count = 0
        while count <= size:
            alist[count] = self.dequeue()
            count += 1
