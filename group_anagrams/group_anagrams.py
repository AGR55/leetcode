class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        if strs and len(strs) <= 10000:
            anagrams: dict = {}

            for word in strs:
                sorted_word: str = "".join(sorted(word))
                if sorted_word not in anagrams:
                    anagrams[sorted_word] = [word]
                else:
                    anagrams[sorted_word].append(word)

            return list(anagrams.values())

        else: return ValueError

def main():
    solution = Solution()
    print(solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))

if __name__ == '__main__':
    main()
