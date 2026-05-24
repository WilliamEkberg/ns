# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        

        def addnumbers(curr, l):

            smallest = 999999999
            indexes = []
            
            n = len(l)
            empty_count = 0

            for i in range(n):
                if not l[i]:
                    empty_count += 1

                    continue


                if l[i].val < smallest:
                    indexes = [i]
                    smallest = l[i].val
                elif l[i].val == smallest:
                    indexes.append(i)


            # add to list
            for j in indexes:
                curr = add_smallest(l, j, curr)

            # Remove empty items

            return curr, empty_count, n

        def add_smallest(l, j, curr):
            tmp = curr.next
            tmp2 = l[j].next

            curr.next = l[j]
            curr.next.next = tmp

            l[j] = tmp2
            
            return curr.next

        head = ListNode()
        curr = head
        
        n=10
        e=0
        while e<n:
            curr, e, n = addnumbers(curr, lists)
        return head.next

        
        





            



        
        


        