class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        jump = 0
        furthest = 0
        current = 0

        for i in range(len(nums) - 1):
            furthest = max(furthest, i + nums[i])

            if i == current:
                jump += 1
                current = furthest

        return jump

    






