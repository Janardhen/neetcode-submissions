class Solution:
    def findMin(self, nums: List[int]) -> int:
        #find middle index of array
        left = 0
        right = len(nums)-1
        
        # for this example [3,4,5,6,1,2], middle is now at index 2 aka 5.

        while left < right:
            middle = ( left + right)//2
            if nums[middle] > nums[right]:
                left = middle+1
            #elif nums[middle] <= nums[right]:
            else:
                right = middle
        return nums[left]


                #we know its rotated 

        