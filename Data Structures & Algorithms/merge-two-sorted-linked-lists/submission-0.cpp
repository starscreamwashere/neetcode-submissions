/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        // 1. Create a dummy node to act as the anchor
        ListNode dummy(0); 
        
        // 2. 'tail' will track the end of our new list
        ListNode* tail = &dummy; 
        
        // 3. Loop while both lists have elements left
        while (list1 != nullptr && list2 != nullptr) {
            if (list1->val <= list2->val) {
                tail->next = list1;  // Link the smaller node
                list1 = list1->next; // Move list1 pointer forward
            } else {
                tail->next = list2;  // Link the smaller node
                list2 = list2->next; // Move list2 pointer forward
            }
            tail = tail->next;       // Move the tail pointer forward
        }
        
        // 4. If one list runs out, append the remaining elements of the other list
        if (list1 != nullptr) {
            tail->next = list1;
        } else {
            tail->next = list2;
        }
        
        // 5. The actual merged list starts right after the dummy node
        return dummy.next;
    }
};