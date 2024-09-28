class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        length: int = len(nums)

        if (nums[0] < -10000 or nums[length - 1] > 10000) or (target < -10000 or target > 10000):
            return

        if 1 <= length <= 10000:
            left: int = 0
            right: int = length - 1
            middle: int

            if target > nums[length - 1]:
                return length
            elif target == nums[length - 1]:
                return length - 1
            elif target <= nums[0]:
                return 0

            while left < right:
                middle = (left + right) // 2

                if nums[middle] >= target > nums[middle - 1]:
                    return middle
                elif nums[middle] < target <= nums[middle + 1]:
                    return middle + 1

                if target < nums[middle]:
                    right = middle - 1
                else:
                    left = middle + 1


pepe = Solution()
print(pepe.searchInsert([1, 3, 5, 6], 0))
