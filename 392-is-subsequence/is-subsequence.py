class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l = 0
        r = 0
        lst = []
        if s == "":
            return True
        while r < len(t):
            if l == len(s):
                break
            if s[l] == t[r]:
                lst.append(t[r])
                l += 1
                r += 1
            else:
                r += 1

        if "".join(lst) == s:
            return True
        else:
            return False
