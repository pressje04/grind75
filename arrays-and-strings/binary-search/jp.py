from typing import List, Optional

class Solution:
    def binarySearch(self, nums: List[int], target: int) -> int:
        n = len(nums)
        start = 0
        end = n - 1

        while start <= end:
            mid = (start + end) // 2

            if nums[mid] < target:
                start = mid + 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                return mid
        return -1

def test():
    sol = Solution()
    print(sol.binarySearch([1, 2, 3, 4, 5, 6, 7, 8], 2)) #1

if __name__ == "__main__":
    test()