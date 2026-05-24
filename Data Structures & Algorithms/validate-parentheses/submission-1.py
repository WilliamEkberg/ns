class Solution:
    def isValid(self, s: str) -> bool:
        # (){()}

        # Check if right side or left side.
        # pop and check if it is the equivalent:

        opening = ['[','{', '(']
        stack = []
        d = {'[':']','{': '}', '(': ')'}

        for i in s:
            if i in opening:
                stack.append(i)
            elif not stack:
                return False
            else:
                v = stack.pop()
                if i != d[v]:
                    return False

        return not stack

