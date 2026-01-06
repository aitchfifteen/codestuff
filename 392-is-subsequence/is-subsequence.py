class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        next = 0

        for i in range(len(t)):
            if next == len(s):
                break
            if t[i] != s[next]:
                continue
            next += 1
        
        if next == len(s):
            return True
        else:
            return False

