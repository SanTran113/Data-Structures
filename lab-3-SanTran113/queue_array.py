# Queue ADT - circular array implementation
from typing import Optional, List, Any

class Queue:
    """Implements an efficient first-in first-out Abstract Data Type using a Python List"""

    def __init__(self, capacity: int, init_items: Optional[List] = None):
        """Creates a queue with a capacity and initializes with init_items"""
        self.capacity = capacity         # capacity of queue
        self.items = [None]*capacity    # array for queue
        self.num_items = 0              # number of items in queue
        self.front = 0                  # front index of queue (items removed from front)
        self.rear = 0                   # rear index of queue (items enter at rear)
        if init_items is not None:      # if init_items is not None, initialize queue
            if len(init_items) > capacity:
                raise IndexError
            elif capacity > 0:
                self.num_items = len(init_items)
                self.items[:self.num_items] = init_items
                self.rear = self.num_items % self.capacity # % capacity addresses length=capacity

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Queue):
            return (self.capacity == other.capacity and self.get_items() == other.get_items())
        else:
            return False

    def __repr__(self) -> str:
        return ("Queue({!r}, {!r})".format(self.capacity, self.get_items()))

    # get_items returns array (Python list) of items in Queue
    # first item in the list will be front of queue, last item is rear of queue
    def get_items(self) -> List:
        if self.num_items == 0:
            print('execute')
            return []
        if self.front < self.rear:
            return self.items[self.front:self.rear]
        else:
            return self.items[self.front:] + self.items[:self.rear]

    def is_empty(self) -> bool:
        """Returns true if the queue is empty and false otherwise
        Must be O(1)"""
        if self.num_items == 0 or self.capacity == 0:
            return True
        else:
            return False

    def is_full(self) -> bool:
        """Returns true if the queue is full and false otherwise
        Must be O(1)"""
        if self.num_items == self.capacity:
            return True
        else:
            return False

    def enqueue(self, item: Any) -> None:
        """enqueues item, raises IndexError if Queue is full
        Must be O(1)"""
        if self.num_items == self.capacity:
            raise IndexError
        # self.rear += 1
        # if self.rear == self.capacity:
        #     self.rear = 0
        elif self.num_items != self.capacity:
            self.items[self.rear] = item
            self.rear = (self.rear + 1) % self.capacity
            self.num_items += 1

        #     print(f"front: {self.front}")
            # print(f"front value: {self.items[self.front]}")

    def dequeue(self) -> Any:
        """dequeues item, raises IndexError is Queue is empty
        Must be O(1)"""
        if self.num_items == 0 or self.capacity == 0:
            print(self.num_items)
            raise IndexError
        if self.num_items != 0:
            self.rear = 0
            # self.front = (self.front + 1) % self.capacity
            x = self.items[self.rear]
            # print(self.items[self.rear])

            del(self.items[self.rear])
            # self.rear = self.items[self.rear]
            # self.num_items -= 1
            print(self.items)
            print(f"rear: {self.rear}")
            # if self.rear == self.capacity:
            #     count = 0
            #     self.front = self.items[count]
            #     count += 1
            # count = 0
            # self.rear = self.items[count]
            # count += 1
            self.num_items -= 1
            return x

    def size(self) -> int:
        """Returns the number of items in the queue
        Must be O(1)"""
        print(f"num_items: {self.num_items}")
        return self.num_items
