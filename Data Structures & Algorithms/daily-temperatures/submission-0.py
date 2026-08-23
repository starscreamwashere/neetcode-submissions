#Brute force
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result=[0]*len(temperatures)
        for i in range(len(temperatures)):
            if i==len(temperatures)-1:
                break
            for j in range(i,len(temperatures)):
                if temperatures[j]>temperatures[i]:
                    result[i]=j-i
                    break
        return result
        