// 1. Standalone ListNode class defined first
class ListNode {
public:
    int val;
    ListNode* next;
    
    // Constructor for easy initialization
    ListNode(int val) {
        this->val = val;
        this->next = nullptr;
    }
};

// 2. The main MyLinkedList class
class MyLinkedList {
private:
    ListNode* dummy;
    int size;

public:
    MyLinkedList() {
        dummy = new ListNode(-1); // Dummy node to simplify edge cases
        size = 0;
    }
    
    int get(int index) {
        if (index < 0 || index >= size) {
            return -1;
        }
        ListNode* curr = dummy->next;
        for (int i = 0; i < index; i++) {
            curr = curr->next;
        }
        return curr->val;
    }
    
    void addAtHead(int val) {
        addAtIndex(0, val);
    }
    
    void addAtTail(int val) {
        addAtIndex(size, val);
    }
    
    void addAtIndex(int index, int val) {
        if (index < 0 || index > size) {
            return;
        }
        
        ListNode* curr = dummy;
        // Move to the node right BEFORE the insertion index
        for (int i = 0; i < index; i++) {
            curr = curr->next;
        }
        
        ListNode* newNode = new ListNode(val);
        newNode->next = curr->next;
        curr->next = newNode;
        size++;
    }
    
    void deleteAtIndex(int index) {
        if (index < 0 || index >= size) {
            return;
        }
        
        ListNode* curr = dummy;
        // Move to the node right BEFORE the deletion index
        for (int i = 0; i < index; i++) {
            curr = curr->next;
        }
        
        ListNode* toDelete = curr->next;
        curr->next = curr->next->next;
        delete toDelete;
        size--;
    }
    
    // Destructor to prevent memory leaks
    ~MyLinkedList() {
        ListNode* curr = dummy;
        while (curr != nullptr) {
            ListNode* nextNode = curr->next;
            delete curr;
            curr = nextNode;
        }
    }
};