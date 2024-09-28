class Solution:
    def myPow(self, x: float, n: int) -> float:
        def pow(a: float, n: int) -> float:
            ans: int = 1.0
            while n > 0:
                if n & 1:
                    ans *= a
                a *= a
                n >>= 1
            return ans

        return pow(x, n) if n >= 0 else 1 / pow(x, -n)



def main():
    solution = Solution()
    print(solution.myPow(2.00000, -2))

if __name__ == '__main__':
    main()
