from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = float("inf")

        for i in prices:
            if i < min_price:
                min_price = i
            profit = i - min_price
            if profit > max_profit:
                max_profit = profit
        return max_profit

def test():
    sol = Solution()
    print(sol.maxProfit([7, 1, 5, 3, 6]))

if __name__ == "__main__":
    test()
