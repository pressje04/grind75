from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return Counter(s) == Counter(t)



def test():
    sol = Solution()
    print(sol.isAnagram("cinema", "iceman")) #True
    print(sol.isAnagram("cat", "car"))

if __name__ == "__main__":
    test()