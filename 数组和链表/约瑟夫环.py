
class Solution:
    # 建链表节点
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next

    def joseph(self, n: int, m: int) -> list:

        # 建一个循环单链表
        res = [0] * n
        head = self.ListNode(val=1)
        tail = head
        for i in range(2, n+1):
            tail.next = self.ListNode(i)
            tail = tail.next
        tail.next = head

        #问题解决步骤
        i = 0  #结果集的下标
        count = 1 # m的计数
        prev = tail #prev节点
        p = head #当前节点
        while prev != p:
            if count == m:
                res[i] = p.val #保存值
                prev.next = p.next # 删除对应节点
                p = p.next  # 移动当前指针
                i += 1 # 结果集到下一位
                count = 1  #重置计数
            else:
                prev = p #移动prev 到当前
                p = p.next # 移动当前到下一个
                count += 1 # 计数加一
        res[i] = p.val  #最后一个节点
        return res





