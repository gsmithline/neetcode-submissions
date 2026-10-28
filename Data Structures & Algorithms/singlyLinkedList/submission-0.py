from typing import List, Optional


class Node:
    def __init__(self, val: int):
        self.val = val
        self.next: Optional[Node] = None


class LinkedList:
    def __init__(self):
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None
        self.length = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.length:
            return -1

        current = self.head

        for _ in range(index):
            current = current.next

        return current.val

    def insertHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

        # If the list was empty, the new node is also the tail.
        if self.tail is None:
            self.tail = new_node

        self.length += 1

    def insertTail(self, val: int) -> None:
        new_node = Node(val)

        if self.tail is None:
            # Empty list
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1

    def remove(self, index: int) -> bool:
        if index < 0 or index >= self.length:
            return False

        if index == 0:
            self.head = self.head.next
            self.length -= 1

            # The list became empty.
            if self.length == 0:
                self.tail = None

            return True

        # Find the node immediately before the one being removed.
        previous = self.head

        for _ in range(index - 1):
            previous = previous.next

        removed = previous.next
        previous.next = removed.next

        # If we removed the last node, update tail.
        if removed == self.tail:
            self.tail = previous

        self.length -= 1
        return True

    def getValues(self) -> List[int]:
        values = []
        current = self.head

        while current is not None:
            values.append(current.val)
            current = current.next

        return values
        
