# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p1 = head
        p2 = head

        count = 0
        while p1:
            count +=1
            p1 = p1.next
            
            if count > n+1:
                p2 = p2.next
        
        prev = p2

        if count == n:
            return head.next
        
        p2.next = p2.next.next

        return head


        


            
            

            


        