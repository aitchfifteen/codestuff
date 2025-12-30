class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        trimmed = s.rstrip()
        arr = list(trimmed)
        n = len(arr)
        count = 0
        

        for i in range(n-1,-1,-1):
            if arr[i] != " ":
                count += 1
            else:
                break
        return count
        