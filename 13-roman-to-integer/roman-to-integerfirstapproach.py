class Solution:
    def romanToInt(self, s: str) -> int:
        arr = list(s)
        number = 0

        for i in range(len(arr)):
            if arr[i] == 'I':
                arr[i] = 1
            elif arr[i] == 'V':
                arr[i] = 5
            elif arr[i] == 'X':
                arr[i] = 10
            elif arr[i] == 'L':
                arr[i] = 50
            elif arr[i] == 'C':
                arr[i] = 100
            elif arr[i] == 'D':
                arr[i] = 500
            elif arr[i] == 'M':
                arr[i] = 1000
        
        for i in range(1, len(arr)):
            if arr[i] > arr[i-1]:
                arr[i] = arr[i] - arr[i-1]
                arr[i - 1] = 0
        
        return sum(arr)


          
