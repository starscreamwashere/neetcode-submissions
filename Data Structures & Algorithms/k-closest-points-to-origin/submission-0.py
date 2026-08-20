class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        self.points=points
        self.k=k
        distance_heap=[]
        for x,y in self.points:
            distance=x*x + y*y
            heapq.heappush(distance_heap,(distance,[x,y]))
        k_closest=[]
        counter=0
        for counter in range(0,k):
            k_closest.append(heapq.heappop(distance_heap))
        k_closest_without_distance=[]
        for distance,[a,b] in k_closest:
            k_closest_without_distance.append([a,b])
        return k_closest_without_distance


        

        