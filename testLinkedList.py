import traceback

class ListNode:
    def __init__(self, x):
        (filename,line_number,function_name,text)=traceback.extract_stack()[-2]
        self.name = text[:text.find('=')].strip()
        self.val = x
        self.next = None

    def show(self):
        print self.name, self.val, self.next

class Solution:
    def isPalindrome(self, head):
        rev = None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow, slow.next, rev = slow.next, rev, slow # Wrong
            # rev, slow.next, slow = slow, rev, slow.next
            print slow.next
        if fast:
            slow = slow.next
        while slow:
            if slow.val != rev.val:
                return False
            slow, rev = slow.next, rev.next
        return True

def testCases():
    sol = Solution()
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(2)
    d = ListNode(1)
    a.next, b.next, c.next = b, c, d

    # def testa():
    #     a = b
    #     a.show()
    # testa()
    # a.show()

    sol.isPalindrome(a)


def main():
    testCases()
    

if __name__ == "__main__":
    main()