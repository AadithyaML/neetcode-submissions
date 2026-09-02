class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pr = 1
        prz=1
        cz = 0
        for i in nums:
            pr*=i
            if i == 0:
                cz+=1
        if cz == 1:
            for i in nums:
                if i!=0:
                    prz*=i   
        if cz == 0:
            for i in range(len(nums)):
                nums[i]=int(pr/nums[i])
        elif cz == 1:
            for i in range(len(nums)):
                if nums[i]==0:
                    nums[i]=prz
                else:
                    nums[i]=0
        else:
            for i in range(len(nums)):
                nums[i]=0

        return nums