class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l=[]
        o=[]
        for i in nums:
            if i==0:
                l.append(i)
            else:
                o.append(i)
        o.extend(l)
        nums[:]=o
        # return nums