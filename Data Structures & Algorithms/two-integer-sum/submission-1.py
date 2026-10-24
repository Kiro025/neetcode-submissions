class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}

        for i, num in enumerate(nums):
            

            complement = target - num
            if complement in hm:
                return [min(i,hm[complement]),max(i ,hm[complement])]

            if num not in hm:
                hm[num] = i


