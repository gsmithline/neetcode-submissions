# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = []
        current = head

        while current:
            if (current.next, current.val) in visited:
                return True
            else:
                visited.append((current.next, current.val))
                current = current.next
        return False 
