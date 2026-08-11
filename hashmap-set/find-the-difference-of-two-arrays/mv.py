# Find the Difference of Two Arrays
# Pattern: Hash Set / Membership Checking
# Time: O(n^2)

from typing import List

class Solution:
    # Logic: You just loop through each array and see if curr is not in the other
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        answer = [[] for _ in range(2)] # this cryptic looking line just makes [[], []] (ai helped here)

        for n in nums1:
            if n not in nums2:
                if n not in answer[0]:
                    answer[0].append(n)

        for n in nums2:
            if n not in nums1:
                if n not in answer[1]:
                    answer[1].append(n)

        return answer


def test():
    sol = Solution()

    print(sol.findDifference([1, 2, 3], [2, 4, 6]))
    print(sol.findDifference([1, 2, 3, 3], [1, 1, 2, 2]))


if __name__ == "__main__":
    test()
