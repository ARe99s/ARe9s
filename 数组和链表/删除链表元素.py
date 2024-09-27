class ListNode:
   def __init__(self, val=0, next=None):
       self.val = val
       self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int)->ListNode:
        # 1 初始化哨兵节点newnode.next 为 2 遍历链表从newnode开始 3只要cur.next不为空就继续
        new_head = ListNode(None, head)
        cur = new_head
        while cur.next is not None:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return new_head.next