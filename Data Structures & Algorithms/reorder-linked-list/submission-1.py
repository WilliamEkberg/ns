# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # Find middle
        fast, slow = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # reverse secound half
        curr = slow.next
        slow.next = None



        prev = None
        while curr:
            n = curr.next 
            curr.next = prev

            prev = curr
            curr = n

        end = prev
        # Merge
        start = head
        while end:
            temp = start.next
            temp2 = end.next

            start.next = end
            end.next = temp

            start = temp
            end = temp2