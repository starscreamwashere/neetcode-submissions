class Solution {
public:
    bool isValid(string s) {
        stack<char> st;
        
        for (char c : s) {
            // 1. If it's an opening bracket, push it onto the stack
            if (c == '(' || c == '{' || c == '[') {
                st.push(c);
            } 
            // 2. If it's a closing bracket
            else {
                // If the stack is empty, there is no matching opening bracket
                if (st.empty()) return false;
                
                // Check if the top of the stack matches the current closing bracket
                if ((c == ')' && st.top() == '(') ||
                    (c == '}' && st.top() == '{') ||
                    (c == ']' && st.top() == '[')) {
                    st.pop(); // Matches! Pop it.
                } else {
                    return false; // Mismatch found
                }
            }
        }
        
        // 3. If the stack is empty, all brackets were matched correctly
        return st.empty();
    }
};