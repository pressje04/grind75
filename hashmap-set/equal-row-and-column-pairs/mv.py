# Equal Row and Column Pairs
# Pattern: Matrix Traversal
# Time: O(n^3)

from typing import List

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        """
        1. Traverse through the columns
        2. Check if column is in grid
        3. Return output
        """
        col_arr = []
        output = 0

        for i in range(len(grid)):
            curr = []

            for j in range(len(grid)):
                curr.append(grid[j][i])

            col_arr.append(curr)

        for col in col_arr:
            for row in grid:
                if col == row:
                    output += 1

        return output


def test():
    sol = Solution()

    print(sol.equalPairs([
        [3, 2, 1],
        [1, 7, 6],
        [2, 7, 7]
    ]))

    print(sol.equalPairs([
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]
    ]))


if __name__ == "__main__":
    test()
