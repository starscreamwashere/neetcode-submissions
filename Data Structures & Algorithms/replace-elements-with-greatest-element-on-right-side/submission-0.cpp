class Solution {
public:
    vector<int> replaceElements(vector<int>& arr) {
        // Your outer loop: processes everything up to the second-to-last element
        for (int index = 0; index < arr.size() - 1; index++) {
            int max_val = arr[index + 1];
            
            // Your inner loop: scans everything to the right to find the true max
            for (int j = index + 2; j < arr.size(); j++) {
                if (arr[j] > max_val) {
                    max_val = arr[j];
                }
            }
            
            // Replace current element with the max found
            arr[index] = max_val;
        }
        
        // Edge Case 2: Handled cleanly at the very end outside the loop
        if (!arr.empty()) {
            arr[arr.size() - 1] = -1;
        }
        
        return arr;
    }
};