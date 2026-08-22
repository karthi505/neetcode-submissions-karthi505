# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen_ptr = set()
        current = head
        while(current != None):
            seen_ptr.add(current)
            current = current.next

            if(current in seen_ptr):
                return True

        return False