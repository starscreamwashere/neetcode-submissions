class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefixSum = [0]*len(nums) 
        suffixSum = [0]*len(nums)
        currleftSum=nums[0]
        currrightSum=nums[len(nums)-1]
        for i in range(len(nums)-1,-1,-1):
            currrightSum=currrightSum+nums[i] if i<len(nums)-1 else nums[len(nums)-1]
            suffixSum[i]=currrightSum-nums[i]
        #right side ka sum done
        for i in range(len(nums)):
            currleftSum=currleftSum+nums[i] if i>0 else nums[0]
            prefixSum[i]=currleftSum-nums[i]
            if prefixSum[i]==suffixSum[i]:
                return i
        #left side ka sum done + comparison also done
        return -1
        




            

        