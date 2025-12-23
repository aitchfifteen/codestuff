class Solution:
    def canJump(self, nums: List[int]) -> bool:
        count = 0
        endOfLine = len(nums) - 1
        for x in range(len(nums)):
            if count == 0 and nums[x] == 0 and x != endOfLine:
                return False
            if nums[x] > count:
                count = nums[x]
            if x + count >= endOfLine:
                return True
            count -= 1
        return True


