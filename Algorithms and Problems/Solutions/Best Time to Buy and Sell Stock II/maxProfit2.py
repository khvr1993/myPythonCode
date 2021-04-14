from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/solution/

        You are given an array prices where prices[i] is the price of a given stock on the ith day.

        Find the maximum profit you can achieve.
        You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

        Note: You may not engage in multiple transactions simultaneously
        (i.e., you must sell the stock before you buy again).

        Solution :
        From leetcode Solution 2
        We should always consecutive peak and valley

        """
        max_profit = 0
        length_of_string = len(prices) - 1
        i = 0
        while i < length_of_string:
            # Find the first Valley to buy the stock
            while i < length_of_string and prices[i+1] <= prices[i]:
                i += 1
            valley = prices[i]
            print(f"valley {valley}")
            # Find the highest peak from the valley
            while i < length_of_string and prices[i+1] >= prices[i]:
                i += 1
            peak = prices[i]
            max_profit += peak - valley
            print(f"max_profit {max_profit}")

        return max_profit


pbm = Solution()
# prices = [7, 1, 5, 3, 6, 4]
prices = [5,4,3,2,1]
op = pbm.maxProfit(prices)
print(op)
