class Solution:
    def intToRoman(self, num: int) -> str:
        if 1 <= num <= 3999:
            symbols = [
                'M', 'CM', 'D', 'CD',
                'C', 'XC', 'L', 'XL',
                'X', 'IX', 'V', 'IV',
                'I'
            ]
            values = [
                1000, 900, 500, 400,
                100, 90, 50, 40,
                10, 9, 5, 4,
                1
            ]

            result = ''
            i = 0

            while num > 0:
                while num >= values[i]:
                    result += symbols[i]
                    num -= values[i]
                i += 1

            return result

        else: return ValueError


def main():
    solution = Solution()
    print(solution.intToRoman(1998))

if __name__ == '__main__':
    main()
