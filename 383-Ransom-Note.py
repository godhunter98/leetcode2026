class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag_count = {}
        for i in magazine:
            if i in mag_count:    
             mag_count[i] +=1
            else:
                mag_count[i] = 1
        for c in ransomNote:
            if c not in mag_count:
                return False
            if mag_count[c] == 1:
                del mag_count[c]
            else:
                mag_count[c]-=1 
        return True