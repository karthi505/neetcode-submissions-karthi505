# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #seen_ptr = set()
        current = head
        slow = current
        fast = slow
        if head == None:
            return False
        

        while(fast.next != None):
            
            slow = slow.next
            
            fast = fast.next.next
            if(fast == None):
                return False
            if(slow == fast):
                return True

        return False