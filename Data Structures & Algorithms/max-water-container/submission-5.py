class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area=0
        curr_area=1
        L=0
        R=len(heights)-1
        while L<R:
            W=R-L
            H=min(heights[L],heights[R])
            curr_area=W*H
            max_area=max(max_area,curr_area)
            if(heights[L]<heights[R]):
                L+=1
            else:
                R-=1
        return max_area
        