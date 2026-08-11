# Is Subsequence
# Pattern: Two Pointers
# Time: O(n)

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        1. Iterate through both s and t
        2. Every char in s should be in t
        3. Therefore we should be able to go through all of s
        """
        s_ptr, t_ptr = 0, 0

        while s_ptr < len(s) and t_ptr < len(t):
            if s[s_ptr] == t[t_ptr]:
                s_ptr += 1
                t_ptr += 1
            else:
                t_ptr += 1

        return s_ptr >= len(s)


def test():
    sol = Solution()

    print(sol.isSubsequence("abc", "ahbgdc"))
    print(sol.isSubsequence("axc", "ahbgdc"))
    print(sol.isSubsequence("", "ahbgdc"))


if __name__ == "__main__":
    test()
