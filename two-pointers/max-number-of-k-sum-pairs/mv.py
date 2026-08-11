# Max Number of K-Sum Pairs
# Pattern: Two Pointers
# Time: O(n log n)

from typing import List

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        """
        Logic: If you sort the array and work your way towards
        the middle with l and r pointers, you will find
        every sum that = k, so no need to remove anything.

        If the sum is < k, that must mean the l pointer
        is too small since we sorted the array. Same idea
        for the right pointer if the sum is > k.
        """
        nums.sort()
        l, r = 0, len(nums) - 1
        output = 0

        while l < r:
            if nums[l] + nums[r] == k:
                output += 1
                l += 1
                r -= 1

            elif nums[l] + nums[r] < k:
                l += 1

            elif nums[l] + nums[r] > k:
                r -= 1

        return output


def test():
    sol = Solution()

    print(sol.maxOperations([1, 2, 3, 4], 5))
    print(sol.maxOperations([3, 1, 3, 4, 3], 6))
    print(sol.maxOperations([1, 1, 1, 1], 2))


if __name__ == "__main__":
    test()
