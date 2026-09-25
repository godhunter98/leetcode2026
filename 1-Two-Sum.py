class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        rev = nums[::-1]
        for i,val in enumerate(nums):
            for j,dec in enumerate(rev):
                if val + dec == target and i != len(nums)-j-1:
                    return [i,len(nums)-j-1]        