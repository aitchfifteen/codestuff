# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current = head
        count = head
        previous = current
        length = 0
        count2 = 1

        while count:
            count = count.next
            length += 1

        if length < 2 and length == n:
            return None
        
        
        target = (length + 1) - n
        
        if count2 == target:
            current = current.next
            head = current
            previous = current

        while current:
            if count2 == target:
                previous.next = current.next
            else:
                previous = current
            
            count2 += 1
            current = current.next
        

        return head



        