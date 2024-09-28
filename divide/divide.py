class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if divisor == 0:
            raise ValueError("No se puede dividir por cero")
        if dividend == 0:
            return 0

        sign = 1
        if (dividend < 0) ^ (divisor < 0):
            sign = -1

        dividend, divisor = abs(dividend), abs(divisor)

        quotient, result = 0, 0

        # Realizamos la división a nivel de bits
        for i in range(31, -1, -1):
            if (result + (divisor << i)) <= dividend:
                result += divisor << i
                quotient |= 1 << i

        quotient *= sign

        # Aseguramos que el resultado esté dentro del rango de 32 bits
        return max(min(quotient, 2**31 - 1), -2**31)



def main():
    solution = Solution()
    print(solution.divide(264, 8))

if __name__ == '__main__':
    main()
