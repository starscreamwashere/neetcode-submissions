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
        long low = 1;
        long high = n;
        
        while (low <= high) {
            // Prevent potential integer overflow
            long mid = low + (high - low) / 2;
            int res = guess(mid);
            
            if (res == 0) {
                return mid; // Found the number
            } else if (res == -1) {
                high = mid - 1; // The picked number is lower
            } else {
                low = mid + 1; // The picked number is higher
            }
        }
        
        return -1;
    }

    
};
