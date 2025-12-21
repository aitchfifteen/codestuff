class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        out = nums[:]
        i = 0
        for j in range(len(nums)):
            if j < 2:
                nums[i] = out[j]
                i += 1
            elif out[j] != out[j-2] and j > 1:
                nums[i] = out[j]
                i += 1
        return i

