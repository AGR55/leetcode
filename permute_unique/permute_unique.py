class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        if 1 <= len(nums) <= 8:
            def backtrack(start: int) -> None:
                if start == len(nums):
                    result.append(nums[:])
                    return
                used = set()
                for i in range(start, len(nums)):
                    if nums[i] not in used:
                        nums[start], nums[i] = nums[i], nums[start]
                        backtrack(start+1)
                        nums[start], nums[i] = nums[i], nums[start]
                        used.add(nums[i])

            result = []
            backtrack(0)
            return result



def main():
    solution = Solution()
    print(solution.permuteUnique([1,1,2]))

if __name__ == '__main__':
    main()
