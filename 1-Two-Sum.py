class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        visited = {}
        for indice, val in enumerate(nums):
            num = target - val
            if num in visited:
                return [visited[num], indice]
            visited[val] = indice
