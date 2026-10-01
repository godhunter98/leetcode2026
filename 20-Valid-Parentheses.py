class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        stack = []
        brackets = {
            ")":"(",
            "}":"{",
            "]":"[",
        }
        for brack in s:
            if brack in brackets:
                if stack and stack[-1] == brackets[brack]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(brack)
        return True if not stack else False