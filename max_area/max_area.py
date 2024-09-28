class Solution:
    def maxArea(self, height: list[int]) -> int:
        left: int = 0
        right: int = len(height) - 1
        max_area: int = 0

        while left < right:
            if height[left] < 0 or height[left] > 10000 or height[right] < 0 or height[right] > 10000:
                return 0

            min_height: int = min(height[left], height[right])
            width: int = right - left
            max_area: int = max(max_area, min_height * width)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area


pepe = Solution()
print(pepe.maxArea([3, 7, 5, 4, 5, 6, 3]))
