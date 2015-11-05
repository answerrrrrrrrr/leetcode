# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
    # rcs
    # LTE
        return self.insertSort(head)
    def insertSort(self, head):
        if head==None or head.next==None:
            return head
        self.insertSort(head.next)
        l=head
        r=head.next
        while r and l.val>r.val:
            l.val,r.val=r.val,l.val
            l=r
            r=r.next
        return head



    # itr
    # 353ms
        dummy = p = ListNode(0)
        dummy.next = q = head
        while q and q.next:
            if q.val <= q.next.val:
                q = q.next
                continue
            p = dummy # compare from the first node
            while p.next.val <= q.next.val:
                p = p.next
            p.next, q.next.next, q.next = q.next, p.next, q.next.next
        return dummy.next



# https://leetcode.com/discuss/63052/ac-python-192ms-solution
    # itr, logic optimized
    # 200ms
        dummy = p = ListNode(0)
        dummy.next = q = head
        while q and q.next:
            val = q.next.val # save 50ms+
            if q.val <= val:
                q = q.next
                continue
            if p.next.val > val: # save 100ms+
                p = dummy
            while p.next.val <= val:
                p = p.next
            p.next, q.next.next, q.next = q.next, p.next, q.next.next
        return dummy.next