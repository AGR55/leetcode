class Solution():
    def minBitFlips(self, start: int, goal: int) -> int:
        if 0 <= start <= 10 ** 9 and 0 <= start <= 10 ** 9:
            xor_num: int = start ^ goal
            return bin(xor_num).count('1')

        else: return ValueError

def main():
    solution = Solution()
    print(solution.minBitFlips(5, 10))
    print(solution.minBitFlips(10, 7))
    print(solution.minBitFlips(3, 4))

if __name__ == '__main__':
    main()
