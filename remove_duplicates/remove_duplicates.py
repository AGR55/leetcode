class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if 1 <= len(nums) <= 30000:
            i: int = 1

            while i < len(nums):
                if -100 <= nums[i] <= 100:
                    if nums[i] == nums[i-1]:
                        nums.pop(i-1)
                    else:
                        i += 1
                else:
                    return

            return len(nums)


pepe = Solution()
print(pepe.removeDuplicates([1,1,2]))
