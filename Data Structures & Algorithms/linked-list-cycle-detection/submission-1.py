# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        slow = head
        if head.next:
            fast = head.next
        else:
            return False

        # Two pointer:
        while slow != fast:
            if not fast:
                return False
            elif not fast.next:
                return False
            
            fast = fast.next.next
            slow = slow.next
        return True



        