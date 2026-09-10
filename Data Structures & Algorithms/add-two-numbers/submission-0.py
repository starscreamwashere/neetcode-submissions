# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1,curr2=l1,l2
        digits1,digits2=0,0
        num1,num2,ans=0,0,0
        while curr1:
            digits1+=1
            num1+=curr1.val*(10 ** (digits1 - 1))
            curr1=curr1.next
        while curr2:
            digits2+=1
            num2+=curr2.val*(10 ** (digits2 - 1))
            curr2=curr2.next
        ans=num1+num2
        digit3=0
        dummy = ListNode(0)
        curr = dummy
        if ans == 0:
            return ListNode(0)
        while ans>0:
            digit3=int(ans%10)
            curr.next=ListNode(digit3)
            curr=curr.next
            ans=ans//10
        return dummy.next
        
        
        