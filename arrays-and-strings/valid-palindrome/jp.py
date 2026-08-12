"""
1) one pointer at start, one at end 

2) if l > r, end of word

3) skip chars that aren't alphanum like commas

4) when comparing, check lowercase version of char
"""

class Solution:
    def isPalindrome(self, word: str) -> bool:
        n = len(word)
        l = 0
        r = n - 1

        while l < r:
            if not word[l].isalnum():
                #skip non alphanum chars
                l += 1
                continue
            if not word[r].isalnum():
                r -= 1
                continue
            #word.lower vs word = word.lower is a memory optimization
            if word[l].lower() != word[r].lower():
                return False
            l += 1
            r -= 1
        return True

def test():
    sol = Solution()
    print(sol.isPalindrome("A man, a plan, a canal: Panama"))

if __name__ == "__main__":
    test()


"""
Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
"""