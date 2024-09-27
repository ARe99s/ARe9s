class ListNode:
   def __init__(self, val=0, next=None):
       self.val = val
       self.next = next
class Solution:
    def insert(self, head: ListNode, value: int)->ListNode:
        # 和每个节点对比，大于等于就往后，小于就往后走
        if head is None:
            return ListNode(value, None)
        if value < head.val:
            return ListNode(value, head)
        p = head
        while p.next is not None and p.val < value and p.next.val < value:
            # 检查p.next val 插入
            # 1 1 2 2 4 5  insert 3
            p = p.next
        tmp = p.next
        p.next = ListNode(value, tmp)
        return head
