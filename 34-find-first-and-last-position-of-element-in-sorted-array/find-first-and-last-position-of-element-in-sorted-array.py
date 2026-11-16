class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        # def starting():
        #     index=len(nums)
        #     start=0
        #     end=len(nums)-1
        #     while start<end:
        #         mid=(start+end)//2
        #         if nums[mid]==target:
        #             index=mid
        #             end=mid-1
        #         elif nums[mid]<target:
        #             start=mid+1
        #         else:
        #             end=mid-1
        #     return index
        # def starting():
        #     index = -1
        #     start = 0
        #     end = len(nums) - 1
        #     while start <= end:
        #         mid = (start + end) // 2
        #         if nums[mid] == target:
        #             index = mid
        #             end = mid - 1
        #         elif nums[mid] < target:
        #             start = mid + 1
        #         else:
        #             end = mid - 1
        #     return index
        # starting()
        def starting():
            index = -1
            start = 0
            end = len(nums) - 1

            while start <= end:
                mid = (start + end) // 2

                if nums[mid] == target:
                    index = mid
                    end = mid - 1

                elif nums[mid] < target:
                    start = mid + 1

                else:
                    end = mid - 1

            return index

        def ending():
            index = -1
            start = 0
            end = len(nums) - 1

            while start <= end:
                mid = (start + end) // 2

                if nums[mid] == target:
                    index = mid
                    start = mid + 1

                elif nums[mid] < target:
                    start = mid + 1

                else:
                    end = mid - 1

            return index

        return [starting(), ending()]

