class Solution:
    def romanToInt(self, s: str) -> int:
        symbol_dict = {
         "I":1,
         "V":5,
         "X":10,
         "L":50,
         "C":100,
         "D":500,
         "M":1000
        }
        if s in symbol_dict:
            return symbol_dict[s]
        total = 0
        prev_val = 0
        s = s[::-1]
        for char in s:
            curr_val = symbol_dict[char]
            if curr_val < prev_val:
                total -= curr_val
            else:
                total += curr_val
            prev_val = curr_val
        return total
