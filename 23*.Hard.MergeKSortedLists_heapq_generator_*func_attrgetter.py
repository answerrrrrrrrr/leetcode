# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
    # https://leetcode.com/discuss/28722/python-133ms-solution
    # LinkedList => List => LinkedList
    # attrgetter('val')
    # 100ms, 99.12%
        from operator import attrgetter
        lst = []
        for head in lists:
            cur = head
            while cur:
                lst.append(cur)
                cur = cur.next
        lst = sorted(lst, key=attrgetter('val'))
        for i in xrange(len(lst)-1):
            lst[i].next = lst[i+1]
        if lst:
            return lst
        else:
            return



    # https://leetcode.com/discuss/78783/8-lines-python-with-generators-and-heapq-merge
    # generators & heapq & *func()
    # Building the new list with just the values from the old ones, leaving the old lists intact.
    # 196ms, 25.16%
        def vals(node):
            while node:
                yield node.val
                node = node.next
        dummy = p = ListNode(None)
        for val in heapq.merge(*map(vals, lists)):
            p.next = p = ListNode(val)
        return dummy.next

    # Building the new list with the nodes from the old ones.
    # 196ms, 25.16%
        def gen(node):
            while node:
                yield node.val, node
                node = node.next
        dummy = p = ListNode(None)
        for _, p.next in heapq.merge(*map(gen, lists)):
            p = p.next
        return dummy.next
