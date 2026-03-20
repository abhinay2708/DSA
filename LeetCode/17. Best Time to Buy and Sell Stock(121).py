class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_prrice=prices[0]
        profit=0

        for i in range(1, len(prices)):
            current_profit= prices[i] - min_prrice

            if current_profit>profit:
                profit=current_profit

            if min_prrice>prices[i]:
                min_prrice=prices[i]

        return profit
