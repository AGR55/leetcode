class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        return min({*range(1, len(nums) + 2)} - {*nums})


def main():
    solution = Solution()
    print(solution.firstMissingPositive([3,4,-1,1]))

if __name__ == '__main__':
    main()
