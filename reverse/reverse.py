class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x *= sign
        reverse_string = str(x)[::-1]
        number = int(reverse_string) * sign

        if number < -2147483648 or number > 2147483647:
            return 0

        return number
