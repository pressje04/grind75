# Removing Stars From a String
# Pattern: Stack
# Time: O(n)

class Solution:
    def removeStars(self, s: str) -> str:
        """
        Logic: Append every character. If you see '*', pop twice
        to remove the '*' and the non-star to its left, then
        return a string from that list/stack.
        """
        stack = []

        for c in s:
            stack.append(c)

            if c == '*':
                stack.pop()
                stack.pop()

        return "".join(stack)


def test():
    sol = Solution()

    print(sol.removeStars("leet**cod*e"))
    print(sol.removeStars("erase*****"))


if __name__ == "__main__":
    test()
