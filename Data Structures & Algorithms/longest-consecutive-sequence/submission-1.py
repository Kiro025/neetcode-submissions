class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)

        maxlength = 1

        if len(numset) == 0:
            return 0

        for i in range(len(nums)):
            if nums[i] - 1 not in numset:
                length = 1
                nextnum = nums[i] + 1
                while nextnum in numset:
                    length += 1
                    nextnum += 1
                    if length > maxlength:
                        maxlength = length
        return maxlength
