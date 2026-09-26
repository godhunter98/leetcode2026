class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s)-1
        while left < right:
            if len(s) < 1:
                break
            s[left], s[right] = s[right], s[left]
            left +=1
            right-=1
