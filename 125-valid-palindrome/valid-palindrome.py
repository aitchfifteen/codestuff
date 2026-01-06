import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ","")
        s = s.lower()
        s = s.translate(str.maketrans("", "", string.punctuation))

        l, r = 0, len(s) - 1

        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        
        return True
