# Find Pivot Index
# Pattern: Prefix Sum
# Time: O(n)

from typing import List

class Solution:
    """
    Logic: w/ the help of chatgpt, I found out that there's a formula for prefix sums,
           the whole prefix[r+1] - prefix[l] thing. So I basically used that to find the
	   sums for the left and right for each iteration of the array. Eventually it
	   reaches the answer.
    """
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = [0]

        for i in range(len(nums)):
            prefix.append(prefix[i] + nums[i])

        # print(prefix)
        # sum(left to right) = prefix[right + 1] - prefix[left]

        for i in range(len(nums)):
            left_sum, right_sum = 0, 0

            if i == 0:
                right_sum = prefix[len(nums)] - prefix[i + 1]

                if left_sum == right_sum:
                    return i

            elif i == len(nums) - 1:
                left_sum = prefix[i] - prefix[0]

                if left_sum == right_sum:
                    return i

            else:
                left_sum = prefix[i] - prefix[0]
                right_sum = prefix[len(nums)] - prefix[i + 1]

                if left_sum == right_sum:
                    return i

        return -1


def test():
    sol = Solution()

    print(sol.pivotIndex([1, 7, 3, 6, 5, 6]))
    print(sol.pivotIndex([1, 2, 3]))
    print(sol.pivotIndex([2, 1, -1]))


if __name__ == "__main__":
    test()
