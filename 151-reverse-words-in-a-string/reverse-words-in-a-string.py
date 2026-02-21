class Solution:
    def reverseWords(self, s: str) -> str:
        reversed_word = " ".join(s.split()[::-1])
        return reversed_word