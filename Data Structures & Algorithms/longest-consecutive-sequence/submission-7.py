class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort()
        m=1
        l=1
        if len(nums)==0:
            return 0
        for i in range(len(nums)-1):
            if nums[i+1] == nums[i]+1:
                l+=1
            if l>m:
                m=l
            if nums[i+1] != nums[i]+1:
                l=1
            
        return m
