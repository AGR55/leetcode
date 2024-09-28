class Solution:
    def kthDistinct(self, arr: list[str], k: int) -> str:
        if 1 <= k <= len(arr) <= 1000:
            count: int = 0

            for i in arr:
                if not i or len(i) > 1000:
                    return

                if arr.count(i) == 1:
                    count += 1
                    if count == k:
                        return i

            return ""


pepe = Solution()
print(pepe.kthDistinct(["a","b","a"], 3))
