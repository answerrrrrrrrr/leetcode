# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
    # 2 pass
        d = {None:None}
        dummy = p = RandomListNode(0)
        while head:
            p.next = p = RandomListNode(head.label)
            p.next, p.random = head.next, head.random
            d[head] = p
            head = head.next
        q = dummy.next
        while q:
            q.random = d[q.random]
            q = q.next
        return dummy.next


    # 1 pass
        d = {}
        dummy = p = RandomListNode(0)
        while head:
            p.next = p = RandomListNode(head.label)
            d[head] = p
            if head.random:
                if head.random not in d:
                    d[head.random] = RandomListNode(head.random.label)
                p.random = d[head.random]
            if head.next in d:
                p.next = d[head.next]
            head = head.next
        return dummy.next


    # rcs
        d = {}
        if not head:
            return
        self.dfs(head, d)
        return d[head]
    def dfs(self, head, d):
        new = RandomListNode(head.label)
        d[head]= new
        if head.next:
            self.dfs(head.next, d)
            new.next = d[head.next]
        new.random = d.get(head.random, None)
