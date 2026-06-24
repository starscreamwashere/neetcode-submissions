#include <stack>
#include <algorithm>

class MinStack {
private:
    std::stack<int> st;
    std::stack<int> minSt;

public:
    MinStack() {}
    
    void push(int val) {
        st.push(val);
        // The new minimum is the smaller of the current value and the previous minimum
        if (minSt.empty()) {
            minSt.push(val);
        } else {
            minSt.push(std::min(val, minSt.top()));
        }
    }
    
    void pop() {
        st.pop();
        minSt.pop();
    }
    
    int top() {
        return st.top();
    }
    
    int getMin() {
        return minSt.top();
    }
};