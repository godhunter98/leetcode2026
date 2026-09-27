class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        chars = {}
        for char in s:
            if char in chars:
                chars[char] +=1
            else:
                chars[char] = 1
        for char in t:
            if char in chars:
                chars[char] -=1
            else:
                return False
        return all(value == 0 for value in chars.values())