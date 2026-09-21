class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        countMap={}
        for num in nums:
            if num not in countMap:
                countMap[num]=1
            else:
                countMap[num]+=1
            if countMap[num]>len(nums)//2:
                return num
        