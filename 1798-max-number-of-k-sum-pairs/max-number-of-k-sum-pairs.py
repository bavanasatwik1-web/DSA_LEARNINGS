class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        # l=[]
        # c=0
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]+nums[j]==k:
        #             c+=1
        #             nums[i]=0
        #             nums[j]=0
        # return c        
        nums.sort()

        l = 0
        r = len(nums) - 1
        c = 0

        while l < r:
            total = nums[l] + nums[r]

            if total == k:
                c += 1
                l += 1
                r -= 1

            elif total < k:
                l += 1

            else:
                r -= 1

        return c