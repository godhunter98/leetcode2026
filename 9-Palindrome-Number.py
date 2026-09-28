class Solution:
    def isPalindrome(self, x: int) -> bool:
        # convert to str solution
        x = str(x)
        return x == x[::-1]