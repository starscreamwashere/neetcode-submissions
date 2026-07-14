class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        int low = 1;
        int high = 0;
        
        // Find the maximum element in the array for our upper bound
        for (int pile : piles) {
            high = max(high, pile);
        }
        
        int ans = high;
        
        // Binary search for the minimum working speed
        while (low <= high) {
            int mid = low + (high - low) / 2;
            
            // Calculate total hours needed at speed 'mid'
            long long totalHours = 0;
            for (int pile : piles) {
                // Equivalent to ceil(pile / mid) without floating point math
                totalHours += (pile + mid - 1) / mid;
            }
            
            // If Koko can finish within h hours, try a slower speed
            if (totalHours <= h) {
                ans = mid;        // Record this valid speed
                high = mid - 1;   // Check the left half
            } else {
                low = mid + 1;    // Speed is too slow, check the right half
            }
        }
        
        return ans;
    }
};