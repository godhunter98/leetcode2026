class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if len(strs)==1:
            return strs[0]
        prefix = ""
        shortest_char = min([len(x) for x in strs])
        for i in range(shortest_char):
            chars = strs[0][i]
            for der in strs:
                if der[i] != chars:
                    return prefix
            prefix+=chars
        return prefix
        # the best solution is to start from the shortest string and start iterating over all the chars and if they exist in others
