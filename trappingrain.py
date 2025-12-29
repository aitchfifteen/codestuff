class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        maxHeight = max(height)
        count = 0

        for i in range(maxHeight):
            inside = False
            pending = 0

            for h in height:
                if h > i:
                    inside = True
                    count += pending
                    pending = 0
                elif inside:
                    pending += 1

        return count
