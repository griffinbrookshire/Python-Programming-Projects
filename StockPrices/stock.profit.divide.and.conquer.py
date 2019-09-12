import time

def max_stock_profit_dc (stockPrices, start, stop):
    n = stop - start
    
    # edge case 1: start==stop: buy and sell immidiately = no profit at all
    if n == 0:
        return 0, start, stop
        
    if n == 1:
        return stockPrices[stop] - stockPrices[start], start, stop
        
    mid = start + n/2

    # the "divide" part in Divide and Conquer: try both halfs of the array
    maxProfit1, buy1, sell1 = max_stock_profit_dc (stockPrices, start, mid-1)
    maxProfit2, buy2, sell2 = max_stock_profit_dc (stockPrices, mid, stop)

    maxProfitBuyIndex = start
    maxProfitBuyValue = stockPrices[start]
    for k in range (start+1, mid):
        if stockPrices[k] < maxProfitBuyValue:
            maxProfitBuyValue = stockPrices[k]
            maxProfitBuyIndex = k
            
    maxProfitSellIndex = mid
    maxProfitSellValue = stockPrices[mid]
    for k in range (mid+1, stop+1):
        if stockPrices[k] > maxProfitSellValue:
            maxProfitSellValue = stockPrices[k]
            maxProfitSellIndex = k        
            
    # those two points generate the maximum cross border profit
    maxProfitCrossBorder = maxProfitSellValue - maxProfitBuyValue
    
    # and now compare all three options and find the best one
    if maxProfit2 > maxProfit1:
        if maxProfitCrossBorder > maxProfit2:
            return maxProfitCrossBorder, maxProfitBuyIndex, maxProfitSellIndex
        else:
            return maxProfit2, buy2, sell2
    else:
        if maxProfitCrossBorder > maxProfit1:
            return maxProfitCrossBorder, maxProfitBuyIndex, maxProfitSellIndex
        else:
            return maxProfit1, buy1, sell1
            

def stock_strategy_divide_and_conquer (stockPrices):
    return max_stock_profit_dc (stockPrices, 0, len(stockPrices)-1)
    

prices = [30, 35, 15, 5, 10, 20, 25, 30, 35, 15, 5, 10, 20, 25, 30, 35, 15, 5, 10, 20, 25, 30, 35, 15, 5, 10, 20, 25]
start_time = time.time()
print (stock_strategy_divide_and_conquer (prices))    
end_time = time.time()
print(end_time - start_time)
