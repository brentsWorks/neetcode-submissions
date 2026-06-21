class Solution:
    def isValid(self, s: str) -> bool:
        # O(n) time and space col
        mapping = { ')' : '(', ']' : '[', '}' : '{'}
        stack = []

        for c in s:
            if c in mapping: # c is a closing bracket
                if stack and stack[-1] == mapping[c]:
                    # top stack matches what we need, so pop it
                    # maintain empty stack
                    stack.pop()
                else:
                    return False
                    # nothing to match, or wrong match -> invalid
            else: # c is a opening bracket
                stack.append(c)

        return True if not stack else False