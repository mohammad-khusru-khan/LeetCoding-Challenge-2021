'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).



Example 1:

Input: prices = [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]
Example 2:

Input: prices = [1]
Output: 0


Constraints:

1 <= prices.length <= 5000
0 <= prices[i] <= 1000
'''


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        INF = float('inf')
        memo = [[-INF] * 2 for _ in range(N)]

        def findMaxProfit(i, hasStock):
            if i >= N:
                return 0
            if hasStock:
                if memo[i][0] != -INF:
                    return memo[i][0]
                memo[i][0] = max(findMaxProfit(i + 2, False) + prices[i], findMaxProfit(i + 1, True))
                return memo[i][0]
            else:
                if memo[i][1] != -INF:
                    return memo[i][1]
                memo[i][1] = max(findMaxProfit(i + 1, True) - prices[i], findMaxProfit(i + 1, False))
                return memo[i][1]

        return findMaxProfit(0, False)
