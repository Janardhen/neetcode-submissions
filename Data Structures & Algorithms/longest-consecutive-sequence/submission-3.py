class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        maxLen = 0

        for n in numSet:
            if n - 1 not in numSet:   # start of sequence
                curr = n
                length = 1

                while curr + 1 in numSet:
                    curr += 1
                    length += 1

                maxLen = max(maxLen, length)

        return maxLen