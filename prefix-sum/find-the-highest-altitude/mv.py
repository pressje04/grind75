# Find the Highest Altitude
# Pattern: Prefix Sum
# Time: O(n)

from typing import List

class Solution:
    # Logic: altitudes acts as our prefix sum, we get the new
    #	     new altitude every iteration by adding the curr
    #	     sum to the current index; return the max.
    def largestAltitude(self, gain: List[int]) -> int:
        altitudes = [0]

        for i in range(len(gain)):
            altitudes.append(altitudes[i] + gain[i])

        return max(altitudes)


def test():
    sol = Solution()

    print(sol.largestAltitude([-5, 1, 5, 0, -7]))
    print(sol.largestAltitude([-4, -3, -2, -1, 4, 3, 2]))


if __name__ == "__main__":
    test()
