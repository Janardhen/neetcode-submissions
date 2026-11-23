class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsub = nums[0]
        cursum = 0 
        for n in nums:
            if cursum <0:
                cursum =0
            cursum+=n
            maxsub = max(cursum, maxsub)

        return maxsub
        
        #start at 2, check next. if negative take max and move pointer to 4. 
# when n itself is bigger than curmax, then we end the sequel. 

