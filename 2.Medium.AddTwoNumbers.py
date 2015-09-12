# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
    #120ms+
        # p, q = l1, l2
        # c = 0
        # while p and q:
        #     val = p.val + q.val + c
        #     p.val, c = val%10, val/10
        #     if not p.next:
        #         p.next, q.next = q.next, None
        #         if c and not p.next:
        #             p.next = ListNode(c)
        #             c = 0
        #     p, q = p.next, q.next
        # while p:
        #     val = p.val + c
        #     p.val, c = val%10, val/10
        #     if c and not p.next:
        #         p.next = ListNode(c)
        #         break
        #     p = p.next
        # return l1

    # Simplified
        # carry = 0
        # dummy = n = ListNode(0)
        # while l1 or l2 or carry:
        #     v1 = v2 = 0
        #     if l1:
        #         v1 = l1.val
        #         l1 = l1.next
        #     if l2:
        #         v2 = l2.val
        #         l2 = l2.next
        #     carry, val = divmod(v1+v2+carry, 10)
        #     n.next = ListNode(val)
        #     n = n.next
        # return dummy.next

    # Simplified
        carry = 0 
        dummy = n = ListNode(0)
        while l1 or l2 or carry:
            if l1:
                carry += l1.val 
                l1 = l1.next
            if l2:
                carry += l2.val 
                l2 = l2.next
            carry, val = divmod(carry, 10)
            # https://leetcode.com/discuss/25432/clear-python-code-straight-forward?show=28475#a28475
            n.next = n = ListNode(val)
        return dummy.next



# https://leetcode.com/discuss/36908/python-for-the-win
    # addends[]
    # 140ms+
        addends = l1, l2
        dummy = end = ListNode(0)
        carry = 0
        while addends or carry:
            carry += sum(a.val for a in addends)
            addends = [a.next for a in addends if a.next]
            end.next = end = ListNode(carry % 10)
            carry /= 10
        return dummy.next           

    # rcs 
    # 148ms+
        def toInt(node):
            return node.val + 10*toInt(node.next) if node else 0
        def toLinkedList(n):
            node = ListNode(n%10)
            if n/10:
                node.next = toLinkedList(n/10)
            return node
        return toLinkedList(toInt(l1) + toInt(l2))

    # 136ms+
        def toInt(node):
            return node.val + 10*toInt(node.next) if node else 0
        n = toInt(l1) + toInt(l2)
        first = node = ListNode(n%10)
        while n > 9:
            n /= 10
            node.next = node = ListNode(n%10)
        return first




















