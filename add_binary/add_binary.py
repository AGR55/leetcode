class Solution:
    def addBinary(self, a: str, b: str) -> str:
        sum: str = ''
        carry: int = 0
        i: int = len(a) - 1
        j: int = len(b) - 1

        while i >= 0 or j >= 0 or carry:
            if i >= 0:
                carry += int(a[i])
                i-= 1
            if j >= 0:
                carry += int(b[j])
                j -=1

            sum = str(carry % 2) + sum
            carry //= 2

        return sum


def main():
    s = Solution()
    print(s.addBinary("1010", "1011"))

if __name__ == '__main__':
    main()
