class Solution:
    def trap(self, height: List[int]) -> int:
        lp=0
        rp=lp+2
        count=0
        if len(height)<3:
            return 0
        while rp<len(height):
            while lp<len(height)-1 and height[lp]<=height[lp+1]:
                lp+=1
            if lp>=len(height)-1:
                break
            l=height[lp]
            rp=lp+1
            r=height[rp]
            for i in range(rp,len(height)):
                tr=height[i]
                if tr>=l:
                    rp=i
                    r=l
                    break
                if tr>r:
                    rp=i
                    r=tr
            if r>l:
                level=l
            else :
                level = r
            for i in range (lp+1,rp):
                count+=level-height[i]
            lp=rp
        return count

            