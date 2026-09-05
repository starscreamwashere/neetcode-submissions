class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        currSum = 0
        seen = {0: 1}          # empty prefix: sum 0 seen once
        for num in nums:
            currSum += num
            count += seen.get(currSum - k, 0)   # subarrays ending here
            seen[currSum] = seen.get(currSum, 0) + 1
        return count