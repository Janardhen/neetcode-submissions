class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # Sort array to enable two pointers and identify duplicates.
        nums.sort()
        result = []

        # Fix each element as the first number of triplet.
        for i, a in enumerate(nums):

            # Stop because three positive numbers cannot sum to zero.
            if a > 0:
                break

            # Skip duplicate starting values to avoid repeating identical triplets.
            if i > 0 and a == nums[i-1]:
                continue

            # Initialize left after fixed element and right at end.
            l, r = i+1, len(nums)-1

            # Search remaining elements while both pointers have distinct indices.
            while l < r:
                threesum = a + nums[l] + nums[r]

                # Sum too large, decrease it by moving right pointer.
                if threesum > 0:
                    r -= 1

                # Sum too small, increase it by moving left pointer.
                elif threesum < 0:
                    l += 1

                # Found valid triplet, store it and move both pointers.
                else:
                    result.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1

                    # Skip duplicate left values to prevent repeating same triplets.
                    while l < r and nums[l] == nums[l-1]:
                        l += 1

        return result