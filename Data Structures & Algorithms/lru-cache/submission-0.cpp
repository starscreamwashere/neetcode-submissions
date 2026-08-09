class LRUCache {
private:
    struct Node {
        int key, value;
        Node* prev;
        Node* next;
        Node(int k, int v) : key(k), value(v), prev(nullptr), next(nullptr) {}
    };

    int capacity;
    unordered_map<int, Node*> cache;   // key -> pointer to its node
    Node* head;   // sentinel: most-recent side is head->next
    Node* tail;   // sentinel: least-recent side is tail->prev

    // unhook a node from the list (O(1))
    void remove(Node* node) {
        node->prev->next = node->next;
        node->next->prev = node->prev;
    }

    // insert node right after head (the most-recent end)
    void insertFront(Node* node) {
        node->next = head->next;
        node->prev = head;
        head->next->prev = node;
        head->next = node;
    }

public:
    LRUCache(int capacity) {
        this->capacity = capacity;
        head = new Node(0, 0);
        tail = new Node(0, 0);
        head->next = tail;
        tail->prev = head;
    }

    int get(int key) {
        if (cache.find(key) == cache.end())
            return -1;
        Node* node = cache[key];
        remove(node);        // pull it out of its current spot
        insertFront(node);   // move it to most-recent end
        return node->value;
    }

    void put(int key, int value) {
        if (cache.find(key) != cache.end()) {   // key exists
            Node* node = cache[key];
            node->value = value;   // update value
            remove(node);
            insertFront(node);     // bump to most-recent
            return;
        }

        // new key
        if (cache.size() == capacity) {          // full -> evict LRU
            Node* lru = tail->prev;              // stalest real node
            remove(lru);
            cache.erase(lru->key);               // keep map in sync
            delete lru;                          // free memory
        }

        Node* node = new Node(key, value);
        cache[key] = node;
        insertFront(node);
    }
};