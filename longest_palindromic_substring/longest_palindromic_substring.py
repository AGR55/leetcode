import time

# pepe = 'pesomoslos'
# popo = 'solsomosep'

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if 1 <= len(s) <= 1000:
            i: int = 0
            j: int = len(s) - 1
            word_return: str = ''
            max: int = 0
            size: int

            while i <= j:
                # Si j llega a ser i, i se mueve de posicion
                if j == i and j < len(s) - 1:
                    i += 1
                    j = len(s) - 1

                word: str = s[i:(j+1)]
                size = len(word)
                if word == word[::-1] and size > max:
                    max = size
                    word_return = word

                j -= 1

            return word_return



class Solution2:
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) > 1000:
            return ""

        def expand_around_center(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        longest_palindrome = ""

        for i in range(len(s)):
            # Odd length palindromes
            odd_palindrome = expand_around_center(i, i)
            if len(odd_palindrome) > len(longest_palindrome):
                longest_palindrome = odd_palindrome

            # Even length palindromes
            even_palindrome = expand_around_center(i, i + 1)
            if len(even_palindrome) > len(longest_palindrome):
                longest_palindrome = even_palindrome

        return longest_palindrome


if __name__ == "__main__":
    start_time = time.time()
    pepe = Solution()
    print(pepe.longestPalindrome("waejsfgusiuebfgvuiboaesnfenbugbviuwbnpajdjjeq0ni0wevijmopsajciwej9fuw9ungu9noidnvcodsniv0nrweu9gb9wofowjosgnpmneropoksomosreconocerpfkwhgipnrnhg"))
    end_time = time.time()

    execution_time = end_time - start_time
    print(f"A-GORE Execution time: {execution_time} seconds")



    start_time2 = time.time()
    pepe2 = Solution2()
    print(pepe2.longestPalindrome("waejsfgusiuebfgvuiboaesnfenbugbviuwbnpajdjjeq0ni0wevijmopsajciwej9fuw9ungu9noidnvcodsniv0nrweu9gb9wofowjosgnpmneropoksomosreconocerpfkwhgipnrnhg"))
    end_time2 = time.time()

    execution_time2 = end_time2 - start_time2
    print(f"COPILOT Execution time: {execution_time2} seconds")
