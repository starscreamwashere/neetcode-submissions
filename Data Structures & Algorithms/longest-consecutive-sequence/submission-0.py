class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:                    # handle empty input
            return 0

        vals = sorted(set(nums))        # distinct values, ascending
        max_size = 1                    # at least one number exists
        current_size = 1                # current run starts at length 1

        for i in range(1, len(vals)):   # compare each element to the previous
            if vals[i] - vals[i-1] == 1:
                current_size += 1        # extends the run
            else:
                current_size = 1         # gap → start a new run of length 1
            max_size = max(max_size, current_size)   # update EVERY step

        return max_size