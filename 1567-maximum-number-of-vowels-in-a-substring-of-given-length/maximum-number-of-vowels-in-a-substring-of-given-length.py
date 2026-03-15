class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        count = 0
        l = 0
        max_count = 0

        for r in range(len(s)):
            if s[r] in vowels:
                count += 1

            if r-l+1 > k:
                if s[l] in vowels:
                    count -= 1
                l += 1
            max_count = max(max_count, count)

        return max_count