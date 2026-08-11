# Unique Number of Occurrences
# Pattern: Hash Map + Hash Set
# Time: O(n)

from typing import List

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        """
        1. Map each num -> occurrence
        2. Check to see if any number has the same amount of occurrences
        3. The number of different occurrences SHOULD be = to the # of
           different numbers seen
        """
        occ_map = {}

        for n in arr:
            if n in occ_map:
                occ_map[n] += 1
            else:
                occ_map[n] = 1

        occ_seen = set()

        for val in occ_map.values():
            occ_seen.add(val)

        if len(occ_map) == len(occ_seen):
            return True
        else:
            return False


def test():
    sol = Solution()

    print(sol.uniqueOccurrences([1, 2, 2, 1, 1, 3]))
    print(sol.uniqueOccurrences([1, 2]))
    print(sol.uniqueOccurrences([-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]))


if __name__ == "__main__":
    test()
