class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        try:
            return haystack.lower.index(needle.lower) if len(haystack) <= 10000 or len(haystack) >= 1 else -1
        except ValueError:
            return -1
