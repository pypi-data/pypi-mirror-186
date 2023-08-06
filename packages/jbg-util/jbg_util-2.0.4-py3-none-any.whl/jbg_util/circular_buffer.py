


from __future__ import annotations
from typing import Generic, TypeVar
from dataclasses import dataclass

T = TypeVar("T")

@dataclass
class CircularBufferNode(Generic[T]):
    data : T
    next : CircularBufferNode = None

    def __repr__(self):
        return repr(self.data)

@dataclass
class CircularBuffer(Generic[T]):
    capacity : int
    curr_size : int = 0
    oldest : CircularBufferNode[T] = None
    latest : CircularBufferNode[T] = None

    def add(self,new_data : T):
        new_node = CircularBufferNode(new_data)
        if self.latest is not None:
            self.latest.next = new_node
        self.latest = new_node
        self.curr_size+=1
        change_in_size=self._update_oldest()
        self.curr_size+=change_in_size

    def _update_oldest(self):
        if self.oldest is None:
            self.oldest=self.latest
        elif self.curr_size>self.capacity:
            self.oldest = self.oldest.next
            return -1
        return 0

    def __iter__(self):
        curr_node = self.oldest
        while curr_node is not None:
            yield curr_node
            curr_node = curr_node.next

    def __str__(self):
        return ', '.join([str(node) for node in self])






