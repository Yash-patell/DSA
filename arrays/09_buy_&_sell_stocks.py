prices = [7,1,5,3,6,4]

def stocks(prices):
    if not prices or len(prices) < 2:
        return 0 
    
    else:
        
        max_profit = 0
        max_price = 0
        min_buy_price = prices[0] # assume that min buy price is the 1st element
        
        for i in range(1,len(prices)):
            n = prices[i]
            
            current_price = n #current price = current element
            
            current_profit = current_price - min_buy_price #calculate the current profit
                
            if current_profit > max_profit:
                max_profit = current_profit
            # max_profit = max(current_profit, max_profit)
                
            if current_price < min_buy_price:
                min_buy_price = current_price
            # min_buy_price = min(min_buy_price, current_price)
            
            if current_price > max_price:
                max_price = current_price
            # max_price = max(max_price, current_price)
                
        return f'min buy price : {min_buy_price}, max selling price : {max_price}, profit: {max_profit}'
        
    
print(stocks(prices))
                
            
            
            
        
        