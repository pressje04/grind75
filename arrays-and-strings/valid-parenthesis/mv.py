class Solution:
    def isValid(self, s: str) -> bool:
        """
        1. The logic is append each open bracket to the stack
        2. If you find a closing bracket, stack.peek() should be it's respective open
        3. By the end, the stack should be empty since everything will be popped
        """
        stack = []

        for c in s:
            if c == ')':
                if not stack:
                    return False
                
                if stack[-1] == '(':
                    stack.pop()
                else:
                    return False

            elif c == '}':
                if not stack:
                    return False

                if stack[-1] == '{':
                    stack.pop()
                else:
                    return False

            elif c == ']':
                if not stack:
                    return False

                if stack[-1] == '[':
                    stack.pop()
                else:
                    return False

            else:
                stack.append(c)
        
        if stack:
            return False
        
        return True

def test():
    sol = Solution()
    print(sol.isValid("()"))

if __name__ == "__main__":
    test()
