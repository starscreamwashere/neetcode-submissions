#so I guess , the number of subarrays here can be found from 3 areas: (1)where no.itself is equal to k , (2)whose prefix sum =k (3)whose suffix sum=k . 
#but there can also be a possibility where subarray is like in the middle , and not beginning from either end,how will u count those cases?
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count=0
        prefixSum=[0]*len(nums)
        currSum=0
        currSuffixSum=0
        suffixSum=[0]*len(nums)
        for i in range(len(nums)):
            currSum=currSum+nums[i]
            prefixSum[i]=currSum
        for i in range(len(nums)-1,-1,-1):
            currSuffixSum=currSuffixSum+nums[i]
            suffixSum[i]=currSuffixSum
            if nums[i]==k:
                count+=1
            if prefixSum[i]==k and prefixSum[i]!= nums[i]:
                count+=1
            if suffixSum[i]==k and suffixSum[i]!=nums[i]:
                count+=1
        return count
        