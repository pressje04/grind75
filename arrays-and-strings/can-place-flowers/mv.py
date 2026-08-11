# Can Place Flowers
# Pattern: A very hardcoded approach lol
# Time: O(n)

from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowers_placed = 0

        """
        All 5 valid cases for a flower to be placed
        1. [0, 0, ...]
        2. [..., 0, 0, 0, ...]
        3. [..., 1, 0, 0, ...]
        4. [..., 0, 0, 1, ...]
        5. [..., 0, 0]

        [1, 0, 1, 0, 0, 1]
        """

        length = len(flowerbed)
        cache = 0

        if length == 1 and flowerbed[0] == 0:
            return n <= 1

        if length == 2 and flowerbed[0] == flowerbed[1] == 0:
            return n == 1

        if length == 3 and flowerbed[0] == flowerbed[1] == flowerbed[2] == 0:
            return n == 2 or n == 1

        for i in range(1, length - 1):
            prv, cur, nxt = flowerbed[i - 1], flowerbed[i], flowerbed[i + 1]

            # case 1
            if i == 1 and prv == cur == 0:
                flowerbed[i - 1] = 1
                cache = i - 1
                flowers_placed += 1

            # case 5
            elif i == length - 1 and cur == nxt == 0:
                flowerbed[i + 1] = 1
                cache = i + 1
                flowers_placed += 1

            # case 2
            elif prv == cur == nxt == 0:
                flowerbed[i] = 1
                cache = i
                flowers_placed += 1

            # case 3
            elif prv == 1 and cur == nxt == 0:
                flowerbed[i + 1] = 1
                cache = i + 1
                flowers_placed += 1

            # case 4
            elif prv == cur == 0 and nxt == 1:
                flowerbed[i - 1] = 1
                cache = i - 1
                flowers_placed += 1

            if prv == cur == 1 or cur == nxt == 1:
                flowers_placed -= 1
                flowerbed[cache] = 0

        return flowers_placed >= n


def test():
    sol = Solution()

    print(sol.canPlaceFlowers([1, 0, 0, 0, 1], 1))
    print(sol.canPlaceFlowers([1, 0, 0, 0, 1], 2))
    print(sol.canPlaceFlowers([0, 0, 1, 0, 0], 1))
    print(sol.canPlaceFlowers([0, 0, 0, 0, 0], 2))


if __name__ == "__main__":
    test()
