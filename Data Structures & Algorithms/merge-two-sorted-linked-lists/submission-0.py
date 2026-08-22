# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        output = ListNode(None, None)

        result = list()

        if list1 == None and list2 != None:
            return list2

        elif list1 != None and list2 == None:
            return list1

        elif list1 == None and list2 == None:
            return None

        ptr1 = list1
        ptr2 = list2

        # Compare while both lists still have nodes
        while ptr1 != None and ptr2 != None:

            if ptr1.val <= ptr2.val:
                result.append(ptr1.val)
                ptr1 = ptr1.next

            else:
                result.append(ptr2.val)
                ptr2 = ptr2.next

        # Add remaining nodes of list1
        while ptr1 != None:
            result.append(ptr1.val)
            ptr1 = ptr1.next

        # Add remaining nodes of list2
        while ptr2 != None:
            result.append(ptr2.val)
            ptr2 = ptr2.next

        # Create linked list from result
        head = ListNode(result[0], None)
        current = head

        new_ptr = 1

        while new_ptr < len(result):
            current.next = ListNode(result[new_ptr], None)
            current = current.next
            new_ptr += 1

        return head
        