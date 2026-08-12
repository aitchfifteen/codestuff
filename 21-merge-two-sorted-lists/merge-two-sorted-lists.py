# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head1 = list1
        head2 = list2

        head3 = None
        current = None

        if head1 == None:
            return head2
        elif head2 == None:
            return head1

        
        if head1.val > head2.val:
            head3 = head2
            head2 = head2.next
        elif head1.val <= head2.val:
            head3 = head1
            head1 = head1.next

        current = head3


        while head1 and head2:
            if head1.val > head2.val:
                current.next = head2
                current = head2
                head2 = head2.next
    
            else:     
                current.next = head1
                current = head1
                head1 = head1.next

        if head1 == None:
            while head2:
                current.next = head2
                current = head2
                head2 = head2.next

        elif head2 == None:
            while head1:
                current.next = head1
                current = head1
                head1 = head1.next
            
        
        return head3





        