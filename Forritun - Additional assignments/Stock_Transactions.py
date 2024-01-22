#Ask for data input and assign input to variables. 

#Stock ID
symbol = input()

#Amount of shares
nshares = int(input())

#buying price
bprice = float(input())

#selling price
sprice = float(input())


#Calculate total buying price and buying commission.
buy_commission = (bprice*nshares) * 0.03
total_buy_price = (bprice*nshares)

#Calculate total selling price and selling commission.
sell_commission = (sprice*nshares) * 0.03
total_sell_price = (sprice*nshares)


#Calculate whether profit or loss.
profit_loss = ((total_sell_price - sell_commission) - (total_buy_price + buy_commission))

#Print formatted results.
print(F"The stock symbol:\nNumber of shares:\nThe stock buying price:\nThe stock selling price: \nTransactions for stock: {symbol}\nBought {nshares} shares @ {bprice}\nPaid {round(total_buy_price,2)}\nCommission when buying: {round(buy_commission,2)}\nSold {nshares} shares @ {sprice}\nReceived {round(total_sell_price,2)}\nCommission when selling: {round(sell_commission,2)}\nProfit or loss: {round(profit_loss,2)}")