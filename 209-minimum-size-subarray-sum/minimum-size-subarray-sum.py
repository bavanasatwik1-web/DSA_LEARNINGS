class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        ml=float("inf")
        le=r=sum=0
        while r<len(nums):
            sum+=nums[r]
            while sum>=target:
                ml=min(ml,r-le+1)
                sum=sum-nums[le]
                le+=1
            r+=1
        if ml==float("inf"):
            return 0    
        return ml        

                











        # for i in range(len(nums)):
        #     for j in range(i,len(nums)):
        #         sub=nums[i:j+1]
        #         sum1=sum(sub)
        #         if sum1>=target:
        #             if len(sub)<ml:
        #                 ml=len(sub)
        # if ml == float("inf"):
        #     return 0                
        # return ml                