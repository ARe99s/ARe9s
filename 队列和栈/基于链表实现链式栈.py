class ListNode:
   def __init__(self, val=0, next=None):
       self.val = val
       self.next = next
class LinkedStack:
    def __init__(self):
        self.head = None

    def push(self, value: int)->ListNode:
        new_node = ListNode(value)
        new_node.next = self.head
        self.head = new_node


    def pop(self)->int:
        if self.head is None:
            return -1
        res = self.head.val
        self.head = self.head.next
        return res


    def peek(self)->int:
        if self.head is None:
            return -1
        return self.head.val

    def isEmpty(self)->bool:
        return self.head is None
