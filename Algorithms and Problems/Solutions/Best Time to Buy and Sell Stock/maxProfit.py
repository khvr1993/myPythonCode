from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

        You are given an array prices where prices[i] is the price of a given stock on the ith day.

        You want to maximize your profit by choosing a single day to buy one stock and choosing a
        different day in the future to sell that stock.

        Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

        Solution :
        Using Kadanes algorithm maintain the minimum purchase price and maximum profit
        maximum profit = minimum price buy - sell at max price
        """
        minimum_buying_price = 2147483648
        maximum_profit = 0
        for val in prices:
            maximum_profit = max(val - minimum_buying_price,maximum_profit)
            minimum_buying_price = min(minimum_buying_price,val)
            # print(f"minimum_buying_price {minimum_buying_price}")
            # print(f"maximum_profit {maximum_profit}")

        return maximum_profit


pbm = Solution()
# prices = [7,1,5,3,6,4]
prices = [5,4,3,2,1]
op = pbm.maxProfit(prices)
print(op)
