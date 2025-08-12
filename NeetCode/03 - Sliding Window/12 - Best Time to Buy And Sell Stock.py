class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        greatest = 0

        l, r = 0, 1
        while r < len(prices):
            profit = prices[r] - prices[l]
            greatest = max(greatest, profit)

            if prices[r] < prices[l]:
                l = r
            r += 1

        return greatest


# or


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        greatest = 0

        for i, price in enumerate(prices):
            sell = max(prices[i:]) - price
            greatest = max(greatest, sell)

        return greatest
