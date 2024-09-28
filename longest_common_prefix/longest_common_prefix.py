class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if 1 <= len(strs) <= 200:
            for i, char in enumerate(strs[0]):
                for other_str in strs[1:]:
                    if i >= len(other_str) or other_str[i] != char:
                        return strs[0][:i]

            return strs[0]

        else: return ValueError

def main():
    example1 = ["flower", "flow", "flight"]
    example2 = ["carta", "racecar", "car"]

    solution = Solution()
    print(solution.longestCommonPrefix(example1))
    print(solution.longestCommonPrefix(example2))

if __name__ == '__main__':
    main()
