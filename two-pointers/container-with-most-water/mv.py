# Container With Most Water
# Pattern: Two Pointers
# Time: O(n)

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        1. Set l and r pointers
        2. Calculate area (smaller pointer * [r - l])
        3. Set maxArea
        4. Move the smaller pointer
        5. Continue until l >= r
        """
        l, r = 0, len(height) - 1
        max_area = -1

        # [1, 8, 6, 2, 5, 4, 8, 3, 7]
        #  0  1  2  3  4  5  6  7  8
        #     l           r
        # ma = 49

        while l < r:
            if height[l] < height[r]:
                area = height[l] * (r - l)
                l += 1
            else:
                area = height[r] * (r - l)
                r -= 1

            max_area = max(max_area, area)

        return max_area


def test():
    sol = Solution()

    print(sol.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
    print(sol.maxArea([1, 1]))


if __name__ == "__main__":
    test()
