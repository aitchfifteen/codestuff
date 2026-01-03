class Solution:
    def reverseWords(self, s: str) -> str:
        arr = s.split()
        stack = []
        reverse = []

        for i in arr:
            stack.append(i)

        while stack:
            reverse.append(stack.pop())
        
        return " ".join(reverse)


        

        