from typing import Optional

"""
Use tortoise and hare for this problem. Because when the fast pointer reaches the end, 
the slow pointer will point to whatever is in the middle.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #slow and fast both start at head
        slow = fast = head
        
        while fast and fast.next:
            #advance slow to next, and fast to next.next
            slow = slow.next
            fast = fast.next.next
        
        return slow

def test():
    sol = Solution()

    LL = ListNode(1)
    LL.next = ListNode(2)
    LL.next.next = ListNode(3)
    LL.next.next.next = ListNode(4)
    LL.next.next.next.next = ListNode(5)

    print(sol.middleNode(LL).val)

if __name__ == "__main__":
    test()