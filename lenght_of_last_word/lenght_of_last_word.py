class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        index_start: int = -1
        index_end: int = 0
        letra: str = ''
        flag: bool = False

        if not s: return 0

        while letra != ' ' or not flag:
            letra = s[index_start]
            if letra != ' ' and not flag:
                index_end = index_start
                flag = True
            if letra == ' ' and flag:
                return -1 * (index_start - index_end)
            if index_start == -1 * len(s):
                return -1 * (index_start - 1 - index_end)
            index_start -= 1

        return ValueError


def main():
    s = Solution()
    print(s.lengthOfLastWord('a'))

if __name__ == '__main__':
    main()
