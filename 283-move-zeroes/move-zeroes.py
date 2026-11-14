class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lz=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[i],nums[lz]=nums[lz],nums[i]
                lz+=1
                
