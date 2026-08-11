from typing import Optional

# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
#list1 and list2 are just pointers to the head of a list with a value
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        d = ListNode()
        curr = d

        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        #Append the rest of the remaining list
        curr.next = list1 if list1 else list2 

        return d.next

def test():
    sol = Solution()
    print(sol.mergeTwoLists([], []))

if __name__ == "__main__":
    test()