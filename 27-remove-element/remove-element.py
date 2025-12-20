class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for k in range(len(nums)):
            if val in nums:
                nums.remove(val)