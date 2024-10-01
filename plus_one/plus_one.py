class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        acum: int = 0
        change: bool = False

        if len(digits) == 1 and digits[0] == 9:
            digits[0] = 1
            digits.append(0)
            change = True

        if digits[-1] == 9:
            acum: bool = True
            index: int = len(digits) - 1
            change = True
            while acum:
                if index >= 0:
                    if digits[index] != 9:
                        digits[index] += 1
                        return digits

                    elif digits[index] == 9 and index != 0:
                        digits[index] = 0

                if index == 0 and digits[index] == 9:
                    digits[index] = 0
                    digits.insert(0, 1)
                    acum = False

                index -= 1

        if digits[-1] != 9 and not change:
            digits[-1] += 1

        return digits


s = Solution()
print(s.plusOne([8, 9, 9, 9]))
