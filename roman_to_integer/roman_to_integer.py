class Solution:
    def romanToInt(self, s: str) -> int:
        if 1 <= len(s) <= 15:
            values = {
                'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1
            }

            total = 0
            prev_value = 0

            for char in reversed(s):
                if char in values:
                    value = values[char]
                else: return ValueError

                if value < prev_value:
                    total -= value
                else:
                    total += value
                prev_value = value

            return total

def main():
    solution = Solution()
    print(solution.romanToInt('MCMXCVIII'))

if __name__ == '__main__':
    main()
