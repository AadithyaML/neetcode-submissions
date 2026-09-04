class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        out=[]
        nums.sort()
        lp=[]
        '''if len(nums)<3:
            return out
        elif len(nums)==3:
            if nums[0]+nums[1]+nums[2]==0:
                return [nums]
            return out
        else:
            if nums[0]==0 and nums[0]==nums[-1]:
                return [[0,0,0]]
            else:
                pe1 = nums[-1]'''
        pe1=float('-inf')
                
        for i in range(len(nums)-1):
            r=len(nums)-1
            l=i+1
            e1=nums[i]
            if e1 == pe1:
                continue
            while r>l:
                e2=nums[l]
                e3=nums[r]
                ln=[e1,e2,e3]
                if e1+e2+e3 == 0 :
                    if ln!=lp:
                        out.append([e1,e2,e3])
                        lp=ln
                    l+=1
                    r-=1
                elif e1 >= -(e2+e3) :
                    r-=1
                else:
                    l+=1
            pe1=e1

        return out

                