class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        result = []
        for i,num in enumerate(nums):
            for j,dg in enumerate(nums[i+1:]):
                if num + dg == target:
                    result.append(i)
                    result.append(i+j+1)
        return result