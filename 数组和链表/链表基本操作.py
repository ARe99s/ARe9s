class ListNode:
   def __init__(self, val=0, next=None):
       self.val = val
       self.next = next
class Solution:

    def insertAtHead(self, head: ListNode, value: int) -> ListNode:
        new_head = ListNode(value, head)
        return new_head

    def insertAtTail(self, head: ListNode, value: int) -> ListNode:
        if head is None:
            return ListNode(value, None)
        tail = head
        while tail.next is not None:
            tail = tail.next
        tail.next = ListNode(value, None)
        return head

    def size(self, head: ListNode) -> int:
        len = 0
        tail = head
        while tail is not None:
            tail = tail.next
            len += 1
        return len


    def prev(self, head: ListNode, enode: ListNode) -> ListNode:
        if head is None or enode is None:
            return None
        if head == enode:
            return None
        prev = head
        while prev.next is not None and prev.next != enode:
            prev = prev.next
        if prev.next is None:
            return None
        else:
            return prev

    def delete(self, head: ListNode, enode: ListNode) -> ListNode:
        if head is None or enode is None:
            return None
        if head == enode:
            return head.next
        prev = head
        p = head.next
        while p is not None and p != enode:
            prev = p
            p = p.next
        if p is None:
            return head
        prev.next = p.next
        return head