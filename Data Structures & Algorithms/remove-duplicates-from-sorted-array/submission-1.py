class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        hashmap={}
        unique=0
        index=0
        counter=0
        for num in nums:
            if num not in hashmap:
                hashmap[num]=1
                unique+=1
            else:
                hashmap[num]+=1

        while index < len(nums):
            if hashmap[nums[index]]>1:
                for counter in range(hashmap[nums[index]]-1):
                    nums.pop(index+1)
            counter=0
            index+=1

        return unique

        