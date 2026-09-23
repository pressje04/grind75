from typing import List

"""
This problem is really easy cuz u don't have to return list indices so u just track the max sum you've found

The clever part is if a current_sum < 0 after an interation, you set current_sum back to 0. 

Say you have [-3, 1, -4, 10]. After -3, you set current sum back to 0 then max sum is 1 next iteration. Then -3 after 3rd iteration so we set it back 
to 0. Then last iteration is 10 which is correct since current_sum is 0 at that point 
"""
class Solution:
    def maxSubarray(self, nums: List[int]) -> int:
        current_sum = 0
        max_sum = float("-inf")

        for num in nums:
            current_sum += num
            if current_sum > max_sum:
                max_sum = current_sum
            current_sum = max(0, current_sum)
        return max_sum

def test():
    sol = Solution()
    print(sol.maxSubarray([-3, 1, -4, 10]))

if __name__ == "__main__":
    test()