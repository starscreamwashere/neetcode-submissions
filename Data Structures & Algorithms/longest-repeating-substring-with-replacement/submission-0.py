#windowlength=R-L+1
#no of replacements=windowlength - no.of times the same character appears in the window
#and this no. should be <=k where k is max permitted swaps
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}           # frequency of each char in the current window
        left = 0
        max_count = 0        # count of the most frequent char in the window
        result = 0

        for right in range(len(s)):
            # grow window: add s[right]
            count[s[right]] = count.get(s[right], 0) + 1
            max_count = max(max_count, count[s[right]])

            # if window is invalid (needs > k replacements), shrink from left
            while (right - left + 1) - max_count > k:
                count[s[left]] -= 1     # remove leftmost char from window
                left += 1

            # window is now valid; record its size
            result = max(result, right - left + 1)

        return result
        
        