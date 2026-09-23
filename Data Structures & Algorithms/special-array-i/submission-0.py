class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        i=0
        if len(nums)==1:
            return True
        while i<=len(nums)-2:
            if(abs(nums[i]-(nums[i+1]))%2==0):
                return False
            i+=1
        return True

        