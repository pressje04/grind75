# Kids With the Greatest Number of Candies
# Pattern: Finding the Maximum
# Time: O(n)

from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
	"""
	1. get the max number in candies
	2. iterate through candies and add extraCandies to each iteration
	3. if that sum is >= maxCandies, true, false otherwise
	"""
        result = []
        max_candies = max(candies)

        for n in candies:
            curr = n + extraCandies

            if curr >= max_candies:
                result.append(True)
            else:
                result.append(False)

        return result


def test():
    sol = Solution()
    print(sol.kidsWithCandies([2, 3, 5, 1, 3], 3))
    print(sol.kidsWithCandies([4, 2, 1, 1, 2], 1))


if __name__ == "__main__":
    test()
