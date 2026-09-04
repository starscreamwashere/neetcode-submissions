class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        while head.next and head.next != head:   # while there's still work
            # find the tail AND the node before it (second-last)
            prev = None
            curr = head
            while curr.next:
                prev = curr          # prev trails one behind
                curr = curr.next
            tail = curr              # last node
            # prev is the second-last node

            if tail == head.next:    # only one node between—or tail IS head.next: done
                break

            # detach the tail from the second-last node
            prev.next = None         # ← THE FIX: second-last now points to None

            # splice tail in right after head
            second = head.next       # save head's current next
            head.next = tail         # head → tail
            tail.next = second       # tail → old second node

            # advance head to the node after the tail we just placed
            head = second