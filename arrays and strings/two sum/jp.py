# Two Sum
# Pattern: Using a Hashtable and checking for membership
# Time: O(log n)

from typing import List

class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        num_dict = {}

        for i, num in enumerate(nums):
            comp = target - num
            if comp in num_dict:
                return [i, num_dict[comp]]
            #if not:
            num_dict[num] = i

def test():
    sol = Solution()
    print(sorted(sol.two_sum([1, 2, 3, 5], 4)))

    #Can return either [0, 2] or [2, 0]
    #I sort so mine should return the first index followed by the second (i.e. [0, 2])

if __name__ == "__main__":
    test()
