class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count = {}

        for i, num in enumerate(nums):
            count[num] = i

        for i, num in enumerate(nums):
            difference = target - num
            if difference in count and (i != count[difference]) :
                return [i, count[difference]] 

