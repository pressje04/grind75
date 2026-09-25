from collections import deque

"""
Use BFS, NOT DFS since the question is asking for a minimum. 

Minimum steps/path ==> BFS
Explore all steps/paths ==> DFS
"""
class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        rows = len(mat)
        cols = len(mat[0])
        res = [[0] * cols for _ in range(rows)]
        queue = deque()
        visited = set()

        #1. Populate queue
        for row in range(rows):
            for col in range(cols):
                if mat[row][col] == 0:
                    queue.append((row, col))
                    visited.add((row, col))
        
        #2. Main DFS Loop
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        dist = 0

        while queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()
                if mat[row][col] == 1:
                    res[row][col] = dist

                for d in directions:
                    new_row = row + d[0]
                    new_col = col + d[1]

                    if 0 <= new_row < rows and 0 <= new_col < cols and (new_row, new_col) not in visited:
                        queue.append((new_row, new_col))
                        visited.add((new_row, new_col))
            dist += 1
        return res

def test():
    sol = Solution()
    print(sol.updateMatrix([[0, 0, 0], [0, 1, 0], [1, 1, 1]]))

if __name__ == "__main__":
    test()
        