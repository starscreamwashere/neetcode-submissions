# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        curr = head
        
        while curr:
            # If the current node object is already in our set, a cycle exists
            if curr in visited:
                return True
            
            # Add the current node reference to the set
            visited.add(curr)
            
            # Move to the next node
            curr = curr.next
            
        # If curr becomes None/null, we reached the end, so there is no cycle
        return False