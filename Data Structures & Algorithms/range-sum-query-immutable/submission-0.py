class NumArray:

    def __init__(self, nums: List[int]):
        self.nums=nums
        self.prefixSum={}
        currSum=0
        for i in range(len(self.nums)):
            self.prefixSum[i]=currSum+self.nums[i]
            currSum=currSum+nums[i]
        

    def sumRange(self, left: int, right: int) -> int:
        if left==0:
            rangeSum=self.prefixSum[right]
        else:
            rangeSum=self.prefixSum[right]-self.prefixSum[left-1]
        
        return rangeSum

        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)