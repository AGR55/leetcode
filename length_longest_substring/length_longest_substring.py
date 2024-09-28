class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0 or len(s) >= 50000:
            return 0

        char_set: set = set()
        left: int = 0
        max_length: int = 0

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            max_length = max(max_length, right - left + 1)

        return max_length


pepe = Solution()
print(pepe.lengthOfLongestSubstring("abcabcbb"))  # Output: 3
print(pepe.lengthOfLongestSubstring("pepe lambo"))  # Output: 8
print(pepe.lengthOfLongestSubstring("pwwkew"))  # Output: 3
