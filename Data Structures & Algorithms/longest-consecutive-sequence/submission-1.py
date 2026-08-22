class Solution:
    def longestConsecutive(self, nums):
        num_set = set(nums)
        longest = 0
        for n in num_set:
          if n - 1 not in num_set:         # only start from a sequence's beginning
            length = 1
            while n + length in num_set:  # walk forward via O(1) lookups
                length += 1
            longest = max(longest, length)
        return longest
        