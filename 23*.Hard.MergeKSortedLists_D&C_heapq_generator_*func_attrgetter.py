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
    # https://leetcode.com/discuss/72007/three-ways-solve-problem-python-build-merge-priority-queue
    # Divide & Conquer
    # 160ms, 39.82%
        def merge(l, r):
            dummy = p = ListNode(-1)
            while l and r:
                if l.val < r.val:
                    p.next, l = l, l.next
                else:
                    p.next, r = r, r.next
                p = p.next
            p.next = l or r
            return dummy.next

        if not lists:
            return
        if len(lists) == 1:
            return lists[0]
        m = len(lists) / 2
        l = self.mergeKLists(lists[:m])
        r = self.mergeKLists(lists[m:])
        return merge(l, r)



    # https://leetcode.com/discuss/55662/108ms-python-solution-with-heapq-and-avoid-changing-heap-size
    # heapq
    # 108ms, 94.53%
        from heapq import heappush, heappop, heapify

        h = [(n.val, n) for n in lists if n]
        heapify(h)
        # h = []
        # for node in lists:
        #     if node:
        #         heappush(h, (node.val, node))

        dummy = p = ListNode(-1)
        while h:
            val, node = heappop(h)
            if node.next:
                heappush(h, (node.next.val, node.next))
            p.next = node
            p = p.next
        return dummy.next



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
