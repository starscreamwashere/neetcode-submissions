/** 
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0
 * int guess(int num);
 */

class Solution {
public:
    int guessNumber(int n) {
        // Call the binary search helper function with the initial range [1, n]
        return binarySearch(1, n);
    }

    int binarySearch(long low, long high) {
        while (low <= high) {
            // Prevent potential overflow by using long or calculating mid this way
            long mid = low + (high - low) / 2;
            int res = guess(mid);
            
            if (res == 0) {
                return mid; // Found the picked number
            } else if (res == -1) {
                high = mid - 1; // The picked number is lower, reduce upper bound
            } else {
                low = mid + 1; // The picked number is higher, reduce lower bound
            }
        }
        return -1;
    }
};
