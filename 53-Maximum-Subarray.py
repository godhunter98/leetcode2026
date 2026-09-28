class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        # kadanes algorithm
        if len(nums) == 1:
            best_sum = nums[0]
            return best_sum
        # -inf to accomodate only -ve arrays as 0 would be best there.
        best_sum = float("-inf")
        current_sum = 0
        for x in nums:
            # only keep the current sum and x if adding X increases it, else keep only X
            current_sum = max(x, current_sum + x)
            best_sum = max(best_sum, current_sum)
        return best_sum