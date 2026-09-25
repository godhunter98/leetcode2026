from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag_count = Counter(magazine)
        for c in ransomNote:
            if c not in mag_count:
                return False
            if mag_count[c] == 1:
                del mag_count[c]
            else:
                mag_count[c]-=1 
        return True