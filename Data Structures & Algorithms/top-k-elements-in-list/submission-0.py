class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencyCount={}
        mostFrequentK=[]
        for num in nums:
            if num not in frequencyCount:
                frequencyCount[num]=1
            else:
                frequencyCount[num]+=1
        while k>0:
            #so the hashmap frequencyCount has keys as values of the nums array , and frequency of each number as the value,so we'll go through the values of the hashmap in descending order , and for every value,we'll add its corresponding key to the list named mostFrequentK. Each time we add a key to the list , we decrement k by 1 , and the while loop continues till k>0
            max_freq = -1
            most_frequent_key = None
            
            # Find the key with the highest frequency currently in the map
            for key, count in frequencyCount.items():
                if count > max_freq:
                    max_freq = count
                    most_frequent_key = key
            
            # Add key to result and remove it from map so it isn't picked again
            mostFrequentK.append(most_frequent_key)
            del frequencyCount[most_frequent_key]
            
            k -= 1
            
        return mostFrequentK



        