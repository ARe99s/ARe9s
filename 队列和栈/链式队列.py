# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class LinkedQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, value: int):
        new_node =  ListNode(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self)->int:
        if self.head is None:
            return -1
        res = self.head.val
        self.head = self.head.next
        return res


    def isEmpty(self)->bool:
        return self.head is None
