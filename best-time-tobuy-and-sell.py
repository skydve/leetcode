# Say you have an array for which the ith element is the price of a given stock on day i. Design an algorithm to find the maximum profit.

def maxProfit(prices):
    z = [b-a for a, b in zip(prices, prices[1:])]
    return sum(x for x in z if x > 0)

def maxProfit2(prices):
    return sum(max(prices[i + 1] - prices[i], 0) for i in range(len(prices) -1))

prices = [-1, 4]
print(maxProfit(prices))