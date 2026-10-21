class Solution:
    def isValid(self, s: str) -> bool:
       stack = []
       mapping = {'{':'}','(':')','[':']'}

       for ch in s:
        if ch in mapping.keys():
            stack.append(ch)
        elif ch in mapping.values():
            if not stack or mapping[stack[-1]] != ch:
                return False
            stack.pop()
       return not stack

