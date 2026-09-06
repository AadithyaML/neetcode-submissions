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
            if lh>rh:
                r-=1
            else:
                l+=1
        return m
                

    
        