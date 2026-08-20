class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n

        # Pass 1: fill output[i] with the product of everything to the LEFT of i
        prefix = 1
        for i in range(n):
            output[i] = prefix          # product of nums[0..i-1] (left side)
            prefix *= nums[i]           # extend prefix to include nums[i] for next round

        # Pass 2: multiply in the product of everything to the RIGHT of i
        suffix = 1
        for i in range(n - 1, -1, -1):  # iterate right to left
            output[i] *= suffix         # output[i] already has left; now × right
            suffix *= nums[i]           # extend suffix to include nums[i] for next round

        return output