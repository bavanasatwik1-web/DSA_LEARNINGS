class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        max=r=le=sum1=0
        d={}
        while r<len(nums):
            sum1+=nums[r]
            d[nums[r]]=d.get(nums[r],0)+1
            if r-le+1==k:
                if len(d)==k: #duplicates checking
                    if sum1>max:
                        max=sum1
                sum1=sum1-nums[le]
                d[nums[le]]=d.get(nums[le])-1
                if d[nums[le]]==0:
                    d.pop(nums[le])
                le+=1
            r+=1
        return max            




        # for i in range(len(nums)-k+1):
        #     sub=nums[i:i+k]
        #     s=set(sub)
        #     if len(s)==k:
        #         sum1=sum(sub)
        #         if sum1>max:
        #             max=sum1
        # return max            