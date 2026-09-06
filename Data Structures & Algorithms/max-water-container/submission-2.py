class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0
        r=len(heights)-1
        m=r*min(heights[0],heights[-1])
        while l<r:
            lh=heights[l]
            rh=heights[r]
            h=min(lh,rh)
            v=(r-l)*h
            if v>m:
                m=v
            while l<r and heights[r]<=h:
                r-=1
            while l<r and heights[l]<=h:
                l+=1
        return m
                

    
        