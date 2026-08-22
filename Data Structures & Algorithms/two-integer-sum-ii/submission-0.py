class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        indexList=[]
        for i in range(len(numbers)):
            j=i+1
            if(numbers[i]+numbers[j]==target):
                indexList.append(i+1)
                indexList.append(j+1)
                return indexList
            else:
                j+=1

        