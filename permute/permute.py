class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        if 1 <= len(nums) <= 6:
            def backtrack(start) -> None:
                if start == len(nums):
                    result.append(nums[:])
                    return

                for i in range(start, len(nums)):
                    nums[start], nums[i] = nums[i], nums[start]
                    backtrack(start+1)
                    nums[start], nums[i] = nums[i], nums[start]

            result = []
            backtrack(0)
            return result


def main():
    solution = Solution()
    print(solution.permute([1, 2, 3]))

if __name__ == '__main__':
    main()
