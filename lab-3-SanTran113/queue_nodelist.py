from __future__ import annotations
# NodeList version of ADT Queue

from typing import Optional, List, Any

# Node class for use with Queue implemented with linked list
# NodeList is one of
# None or
# Node(value, rest), where rest is the rest of the list
class Node:
    def __init__(self, value: Any, rest: Optional[Node]):
        self.value = value      # value
        self.rest = rest        # NodeList

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Node):
            return self.value == other.value and self.rest == other.rest
        else:
            return False

    def __repr__(self) -> str:
        return ("Node({!r}, {!r})".format(self.value, self.rest))

class Queue:
    def __init__(self, rear: Optional[Node] = None, front: Optional[Node] = None, num_items: int = 0):
        self.rear = rear    # rear NodeList
        self.front = front   # front NodeList
        self.num_items = num_items  # number of items in Queue

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Queue):
            return self.get_items() == other.get_items()
        else:
            return False

    def __repr__(self) -> str:
        return ("Queue({!r}, {!r})".format(self.rear, self.front))

    # get_items returns array (Python list) of items in Queue
    # first item in the list will be front of queue, last item is rear of queue
    def get_items(self) -> List:
        items: List = []
        front = self.front
        while front is not None:
            items.append(front.value)
            front = front.rest
        if self.rear is not None:
            rear_items = []
            rear: Optional[Node] = self.rear
            while rear is not None:
                # self.num_items += 1
                # print(self.num_items)
                rear_items.append(rear.value)
                rear = rear.rest
            rear_items.reverse()
            items.extend(rear_items)
        return items

    def is_empty(self) -> bool:
        """Returns true if the queue is empty and false otherwise
        Must be O(1)"""
        # temp = self.rear
        # print(temp)
        # count = 0
        # while temp is not None:
        #     count += 1
        #     temp = self.rear.rest
        # # self.rear = self.rear.rest
        # print(self.rear.rest)
        # print(count)
        # self.num_items = count
        if self.size() == 0:
            return True
        else:
            return False


    def enqueue(self, item: Any) -> None:
        """enqueues item, adding it to the rear NodeList
        Must be O(1)"""
        # print(self.rear)
        # self.num_items += 1
        if self.rear is None or self.num_items == 0:
            # print(f"item: {item}")
            # self.rear = self.front
            self.rear = Node(item, self.rear)
            self.num_items += 1
            # self.num_items += 1
            # print(f"rear: {self.rear}")
            # self.rear = item
            # self.rear = self.front
        else:
            # print(self.num_items)
            # print(self.rear)
            # print(self.front)
            self.newNode = Node(item, self.rear)
            self.rear = self.newNode
            # print(f"after: {self.rear}")
            # self.rear = self.rear.rest
            self.num_items += 1
            # newNode = Node(item, self.rear.rest)
            # self.front.rest = self.front
            # self.front = newNode
            # self.front = newNode

        # rear = 3 vs 3->2->1
        # front = Node(rear,front)  3->2->1
        # rear = rear.rest


    def dequeue(self) -> Any:
        """dequeues item, removing first item from front NodeList
        If front NodeList is empty, remove items from rear NodeList
        and add to front NodeList until rear NodeList is empty
        (This will still satisfy O(1) requirement for the operation,
        as the transfer is amortized across all dequeues)
        If front NodeList and rear NodeList are both empty, raise IndexError
        Must be O(1) - general case"""
        if self.rear is None and self.front is None:
            raise IndexError
        elif self.front is None:
            while self.rear is not None:
                self.front = Node(self.rear.value, self.front)
                self.rear = self.rear.rest
                print(f"front: {self.front}")
                print(f"rear: {self.rear}")
                print(f"front value: {self.front.value}")
            # if self.rear is None:
            #     # print(f"rear rest value: {self.rear.rest}")
            #     # print(f"front value: {self.front.value}")
            #     # print(self.rear)
            #     value = self.front.value
            #     self.rear = self.front.rest
            #     print(f"front: {self.front}")
            #     self.front = self.rear
            #     print(f"rear: {self.rear}")
            #     # self.rest = None
            #     self.num_items -= 1
            #     return value
        print(f"BREAK: ({self.front}), ({self.rear}), ({self.num_items})")
        value = self.front.value
        if self.front.rest is None:
            self.front = Node(None, None)
        else:
            self.front = self.front.rest
        print(f"front rest: {self.front.rest}")
        # self.front = self.rear
        print(self.rear)
        self.num_items -= 1
        print(f"BREAK_END: ({self.front}), ({self.rear}), ({self.num_items})")
        # self.rear = None
        return value

            # Trying to flip it
            # self.newNode = Node(self.front, None)
            # self.front = self.newNode
            # self.rear = self.rear.value
            # self.front = self.rear
            # print(f"front: {self.front}")


            # Using While Loop
            # x = self.rear.rest
        # if self.rear.rest is None:
        #     target = self.rear
        #     self.front = Node(target, None)
        #     del (target)
        #     self.num_items -= 1
        #     return target



    def size(self) -> int:
        """Returns the number of items in the queue
        Must be O(1)"""
        # print(self.index(self.rear))
        # print(self.rear)
        # print(self.num_items)
        # index = self.get_items(self.rear)
        # print(self.num_items)
        # print(index)
        # else:
        if self.num_items != 0:
            return self.num_items
        else:
            cur = self.rear
            print(self.rear)
            count = 0
            while cur is not None:
                count += 1
                getNext = cur.rest
                cur = getNext
            return count
        # return self.num_items