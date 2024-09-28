class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if len(digits) > 4:
            return ValueError

        letters = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        def backtrack(combination, next_digits):

            if not next_digits:
                result.append(combination)
            else:
                for letter in letters[next_digits[0]]:
                    backtrack(combination + letter, next_digits[1:])

        result = []
        if digits:
            backtrack('', digits)
        return result


def main():
    solution = Solution()
    print(solution.letterCombinations('23'))
    print(solution.letterCombinations(''))
    print(solution.letterCombinations('2'))

if __name__ == '__main__':
    main()
