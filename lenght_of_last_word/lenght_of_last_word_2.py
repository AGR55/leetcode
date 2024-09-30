class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words: list = s.strip().split()

        if not words:
            return 0

        return len(words[-1])


def main():
    text = 'La vaca lola, la vaca lola'
    s = Solution()
    print(s.lengthOfLastWord(text))

if __name__ == '__main__':
    main()
