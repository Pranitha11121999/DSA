class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_value = 0
        min_value = float("inf")
        for i in range(len(prices)):
            if min_value > prices[i]:
                min_value = prices[i]
            if max_value < prices[i] - min_value:
                max_value = prices[i]-min_value
        return max_value
        