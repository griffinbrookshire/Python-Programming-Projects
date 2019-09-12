import time

def max_stock_profit_bf (stockPrices, index):
    buyingPrice = stockPrices [index]
    maxProfit = 0
    sellAt = index
    
    for i in range (index+1, len(stockPrices)):
        sellingPrice = stockPrices[i]
        profit = sellingPrice - buyingPrice
        if profit > maxProfit:
            maxProfit = profit
            sellAt = i
    return maxProfit, sellAt
    
# check all possible buying times

def stock_strategy_brute_force (stockPrices):
    maxProfit = None
    buy = None
    sell = None
    
    for index, item in enumerate (stockPrices):
        profit, sellAt = max_stock_profit_bf (stockPrices, index)
        if (maxProfit is None) or (profit > maxProfit):
            maxProfit = profit
            buy = index
            sell = sellAt
            
    return maxProfit, buy, sell

prices = [30, 35, 15, 5, 10, 20, 25, 30, 35, 15, 5, 10, 20, 25]
start_time = time.time()
print (stock_strategy_brute_force(prices))    
end_time = time.time()
print(end_time - start_time)
