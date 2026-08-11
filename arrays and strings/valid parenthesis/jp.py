class Solution:
    def valid_parenthesis(self, input: str) -> bool:
        stack = []
        paren = {")": "(", "]": "[", "}": "{"}

        for char in input:
            #closing brace
            if char in paren:
                popped = stack.pop()

                if paren[char] != popped:
                    return False
            #opening brace
            else:
                stack.append(char)
        return not stack
        

def test():
    sol = Solution()
    print(sol.valid_parenthesis("()"))

if __name__ == "__main__":
    test()
