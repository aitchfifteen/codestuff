class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        maxLeft = [0] * n
        maxRight = [0] * n
        water = 0
        count = 0

        for i in range(len(height)):
            if i == 0:
                maxLeft[i] = 0
            else:
                maxLeft[i] = max(maxLeft[i - 1], height[i - 1])
        
        for i in range(n-2, -1, -1):
                maxRight[i] = max(maxRight[i+1], height[i+1])

        for i in range(len(height)):
            water = min(maxLeft[i], maxRight[i]) - height[i]
            if water > 0:
                count += water
        return count

