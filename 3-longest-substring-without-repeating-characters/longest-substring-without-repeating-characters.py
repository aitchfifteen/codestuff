from collections import deque

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        q = deque()
        longest = 0
        
        for ch in s:
            while ch in q:
                q.popleft()
            
            q.append(ch)
            longest = max(longest, len(q))
        
        return longest
        







        