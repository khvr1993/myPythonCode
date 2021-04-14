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
        From leetcode Solution 3
        We can keep on adding the profitss till we reach a peak. Once we reach the peak we need
        to check for next peak again. Thiss will help us in adding all the profits

        This stems from the logic that
        Say we have profits of 2,4,7 The maximum profit by adding will always be greater than the profit if we dont include
        all points

        eg: 1,3,5,6,7,11
            profits = 2{3-1}+2{5-3}+1+1+4 >= 11-1
        eg2:1,3,5,6,7,20,1,11
            profits = 2+2+1+1+13+10
            1,3,5,2,11
            2+2 + 9

        """
        max_profit = 0
        for i in range(1,len(prices)):
            # We can sell a stock only when the current day price is less than the previous day price
            if (prices[i] >= prices[i-1]):
                max_profit += prices[i] - prices[i-1]
            # print(max_profit)
        return max_profit

pbm = Solution()
prices = [7,1,5,3,6,4]
op = pbm.maxProfit(prices)
print(op)