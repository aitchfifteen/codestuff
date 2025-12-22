class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n
        if n == 1 or k == 0:
            return

        out = nums[:]          # copy
        doubled = out + out    # "double" it

        start = n - k          # where the rotated version begins in doubled
        nums[:] = doubled[start : start + n]













        