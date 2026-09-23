from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

def test():
    sol = Solution()
    print(sol.containsDuplicate([1, 2, 3, 4, 5, 1])) #True
    print(sol.containsDuplicate([1, 2, 3, 4, 5, 6])) #False

if __name__ == "__main__":
    test()
         