class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        length: int = len(nums)

        if (0 <= length <= 100) and (0 <= val <= 100):
            count: int = 0
            index: int = 0

            while index < length:
                aux: int = nums[index]

                if aux < 0 or aux > 50:
                    return

                if aux == val:
                    count += 1
                    nums.pop(index)
                    length -= 1
                else:
                    index += 1

            return nums

        else:
            return


pepe = Solution()
print(pepe.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))
