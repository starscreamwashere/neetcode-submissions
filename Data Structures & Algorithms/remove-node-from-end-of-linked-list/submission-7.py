# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count=0
        curr=head
        while curr:
            count+=1
            curr=curr.next
        #nth node fron the end = (count-n+1)th node from the start,provided node 1 is index 1,so now I know how many nodes are there in the list,and I already know which node from the end needs to be removed, but since this is singly linked list,what we'll do is stop at the node before and change its next pointer , to the next of the next node
        if (count==1):
            singlenode=head
            head=None
            return head
        dummynode=ListNode(-1)
        dummynode.next=head
        prev_index=count-n
        trav=0
        curr2=dummynode
        while trav<prev_index :
            trav+=1
            curr2=curr2.next
        curr3=curr2.next
        curr2.next=curr2.next.next
        curr3.next=None
        return dummynode.next
        
        