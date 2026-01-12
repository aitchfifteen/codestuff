class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sum_ = 0          
        left = 0
        subCount = float("inf")  

        for i in range(len(nums)):         
            sum_ += nums[i]

          
            while sum_ >= target:
                count = i - left + 1      
                if count < subCount:
                    subCount = count

                sum_ -= nums[left]          
                left += 1                  

        return 0 if subCount == float("inf") else subCount



                    


        


            
