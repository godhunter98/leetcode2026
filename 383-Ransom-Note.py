class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomcount = {}
        mag_count = {}
        for i in ransomNote:
            if i in ransomcount:    
             ransomcount[i] +=1
            else:
                ransomcount[i] = 1
        for i in magazine:
            if i in mag_count:    
             mag_count[i] +=1
            else:
                mag_count[i] = 1
        result = True
        print(ransomcount)
        print(mag_count)
        for char, count in ransomcount.items():
            if mag_count.get(char,0) < count:
                result = False
        return result
                