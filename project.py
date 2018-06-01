""" CSC 161 Milestone : The “Moving Average” Trading Algorithm

This program allows you to buy/sell stocks using your account

Masashi Kawabata
Lab Section MW 3:25-4:40
Spring 2018"""

def bookkeeping():
    cash_balance = 1000
    stocks_owned = 0

    return cash_balance, stocks_owned

#This function is only checking if the data works 
def test_data(filename,col,day):
    file_open = open(filename,"r")
    header = file_open.readline()
    # First row is done

    stats = file_open.readlines()
    stats.reverse() # 1st one is the oldest date
    
    final_list = []
    
    file_open.close()

    for s in range(len(stats)):
        final_list.append(stats[s].split(","))#adding stat list into final list but with separated by commas

    if col == "Date":
            num = 0
    elif col == "Open":
            num = 1
    elif col == "High":
            num = 2
    elif col == "Low":
            num = 3
    elif col == "Close":
            num = 4
    elif col == "Volume":
            num = 5
    else:
        num = 6

    record = final_list[day-1] #subtracting one b/c no usage of dates 
    return(record[num])

def open_data(filename):
    infile = open(filename,"r")
    header = infile.readline() #we don't use first row for finding data
    _data = infile.readlines()
    _data.reverse()
    infile.close()
    stock_list = [] #list to add the data later 

    for i in range(len(_data)):
        stock_data = _data[i].split(",")

        stock_value = eval(stock_data[1])# getting the stock value one by one 
        
        stock_list.append(stock_value)

    return stock_list 
    
    
def alg_moving_average(filename):
    cash_balance, stocks_owned = bookkeeping()
    first_day = 0
    last_day = 20
    stock_data = open_data(filename) # previous function used here

    while first_day < (len(stock_data) - 20):# run this until there is no more first day 
        
        total_sum = sum(stock_data[first_day:last_day])# runs through 0-19, which is 20 days

        average_price = (total_sum / 20)# average price 

        price_21 = stock_data[last_day] # price of 21st day

        #comparison

        if average_price < price_21 * 0.25 and stocks_owned > 0:
            stocks_owned -= 1 # sell the stock
            cash_balance += price_21 
            
        elif average_price > price_21 * 0.25 and price_21 < cash_balance:
            stocks_owned += 1 # buy the stock
            cash_balance -= price_21

        elif average_price == price_21:
            pass

        first_day += 1 # new first day
        last_day += 1 # new last day

    cash_balance += stocks_owned * average_price

    stocks_owned = 0 # need to sell all stocks

    return  stocks_owned, cash_balance

#MILESTONE III Daily Stock Trade
#Instead of trading stocks every 20 days, I decided to trade day by day.
#This is a similar to real investor, who trades stocks everyday.

def alg_mine(filename):
    cash_balance, stocks_owned = bookkeeping()
    yesterday = 0
    today = 1
    stock_market = open_data(filename)
    
    while yesterday < (len(stock_market) - 1):
        total_price = sum(stock_market[yesterday:today])#Calculating yesterday's stock price only
        yesterday_price = total_price / 1 #Although its only one day, I used this calculation to change the datatype 
        today_price = stock_market[today]
        
        if yesterday_price < today_price * 0.15 and stocks_owned > 0:
            stocks_owned -= 1
            cash_balance += today_price
            
        elif yesterday_price > today_price * 0.15 and cash_balance > today_price:
            stocks_owned += 1
            cash_balance -= today_price
            
        elif yesterday_price == today_price:
            pass
        
        yesterday += 1
        today += 1 #goes to the next day 
        
    cash_balance += stocks_owned * today_price
    stocks_owned = 0
    return stocks_owned,cash_balance 

def main():
    filename = input("Please enter a filename for stock data in CSV format: ")

    #calling my milestone II function here
    alg1_stocks, alg1_balance = alg_moving_average(filename)

    print("You have", alg1_stocks,"stocks left.")
    print("Your remaining balance is ${0:0.2f}.\n".format(alg1_balance))

    #calling my daily stock function here

    alg2_stocks, alg2_balance = alg_mine(filename)

    print("I have",alg2_stocks,"stocks left.")
    print("My remaining balance is ${0:0.2f}.\n".format(alg2_balance))

    #MILESTONE IV: Statistics
    #Comparing the moving average versus my program and analyze the difference

    diff = int(alg2_balance - alg1_balance)
    
    print("My program made approximately",diff,"more dollars than the moving average program.")
    print("This is because my program checked the stock price day by day, instead of 20days basis.")
    print("By program checking the stocks everyday, it allows to make best decisions(buy or sell stocks)depending on various situations.")

if __name__ == "__main__":
    main()

    


    
    
    
    
