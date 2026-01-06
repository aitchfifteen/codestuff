import string 

class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = s.replace(" ","")
        s = s.translate(str.maketrans("", "", string.punctuation))
        s = s.lower()

        n = len(s)
        arr = []

        for i in range(n - 1, -1, -1):
            arr.append(s[i])

        arr = "".join(arr)    

        for i in range(len(s)):
            if arr[i] != s[i]:
                return False
        return True
