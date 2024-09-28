class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        if 1 <= n <= 8:
            def backtrack(s: str, left: int, right: int) -> None:
                if len(s) == 2 * n:
                    result.append(s)
                    return
                if left < n:
                    backtrack(s+'(', left+1, right)
                if right < left:
                    backtrack(s+')', left, right+1)

            result = []
            backtrack('', 0, 0)
            return result
        else: return ValueError


def main():
    solution = Solution()
    print(solution.generateParenthesis(4))

if __name__ == '__main__':
    main()
