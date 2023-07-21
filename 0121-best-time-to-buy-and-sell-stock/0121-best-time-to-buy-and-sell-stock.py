class Solution(object):
    def maxProfit(self, prices):
        # profit = 0

        # for buy in range(len(prices)):
        #     for sell in range(buy+1,len(prices)):
        #         profit = max(profit,(prices[sell]-prices[buy]))
        # return profit
        profit = 0
        i = 0
        for j in range(1,len(prices)):
            diff = prices[j] - prices[i]
            if diff>0:
                profit = max(profit, diff)
            else:
                i = j
        return profit



