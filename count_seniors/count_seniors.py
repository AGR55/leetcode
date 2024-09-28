from re import match


class Solution:
    def countSeniors(self, details: list[str]) -> int:
        if 1 <= len(details) <= 100:
            count: int = 0
            age: int
            for i in details:
                if len(i) == 15 and i[10] in "FMO" and match(r'^\d{10}[FMO]\d{4}$', i):
                    age = int(i[11:13])
                    if age > 60:
                        count += 1

            return count


pepe = Solution()
print(pepe.countSeniors(["7868190130M7522", "5303914400F9211", "9273338290F4010"]))
