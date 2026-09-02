from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        og_color = image[sr][sc]
        self.dfs(image, sr, sc, color, og_color)
        return image
    
    def dfs(self, image, sr, sc, color, og_color):
        #We have a number of conditions that must be true in order to change a color
        if sr is None or sr > len(image) - 1 or sr < 0 or sc is None or sc < 0 or sc > len(image) - 1 or image[sr][sc] == color or image[sr][sc] is not og_color:
            return
        #change color
        image[sr][sc] = color

        #check other quadrants
        self.dfs(image, sr+1, sc, color, og_color)
        self.dfs(image, sr, sc+1, color, og_color)
        self.dfs(image, sr-1, sc, color, og_color)
        self.dfs(image, sr, sc-1, color, og_color)

def test():
    sol = Solution()
    print(sol.floodFill([[1, 1, 1], [1, 1, 1], [1, 1, 1]], 1, 1, 2))

if __name__ == "__main__":
    test()