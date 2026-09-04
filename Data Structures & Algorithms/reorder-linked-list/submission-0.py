class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # Step 1: find middle (slow ends at end of first half)
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: reverse the second half
        second = slow.next
        slow.next = None            # split into two lists
        prev = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # Step 3: merge the two halves
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2