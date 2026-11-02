class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        ts=sum(nums)
        ls=0
        for i in range(len(nums)):
            if ts-ls-nums[i]==ls:
                return i
            ls+=nums[i]
        return -1       