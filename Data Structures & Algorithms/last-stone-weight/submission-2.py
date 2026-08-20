class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        self.stones=[-stone for stone in stones]
        heapq.heapify(self.stones)
        while (len(self.stones)>=0):
            if(len(self.stones)==0):
                return 0
            else:
                if(len(self.stones)==1):
                    return -self.stones[0]
                first=heapq.heappop(self.stones)
                second=heapq.heappop(self.stones)
                rem_wt=first-second
                if rem_wt!=0:
                    heapq.heappush(self.stones,rem_wt)
                
            
        