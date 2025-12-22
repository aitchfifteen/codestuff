class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n
        if n == 1 or k == 0:
            return

        out = nums[:]          
        doubled = out + out    

        start = n - k          
        nums[:] = doubled[start : start + n]













        