import matplotlib.pyplot as plt
import scipy as sp
import stocks as mydata
import math 

# number 1 
def percent_of_mean(idx_list):
    """Convert daily stock index into a percent of the mean over a period of time.
    
        It calculates a list of the value of the stock index for each day as a 
      percent of the mean value over the period covered by the list and returns
      the list with the value of percent of the mean.
    
    Position Input Parameter:
        input: a list of float or int numeric values of stock index
            
    Keyword Input Parameters:
        None
        
    Examples:
    >>> print(percent_of_mean(stocks.nasdaq)
    [99, 99, 99, 99, 99, 99, 99, 98, 97, 97, 97, 97, 96, 97, 97, 96, 98, 94, 92,
    94, 95, 97, 97, 96, 97, 97, 99, 100, 100, 100, 100, 100, 101, 101, 102, 101,
    102, 102, 102, 103, 103, 103, 103, 103, 103, 103, 104, 104, 104, 104, 104,
    104, 105, 104, 104, 105, 105, 105, 105, 104, 104, 104, 104, 104, 104]
    """
    percent_list = []
    mean_of_list = sp.mean(idx_list)
    
    for i in range(len(idx_list)):
        percent_list.append(math.ceil((idx_list[i]/mean_of_list *100)))
    return percent_list

# number 3
def num_days_big_percent_chg(idx_list,percent_chg):
    """Calculates the number of days for defined big changes.
    
      It calculates and returns the total number of trading days where the 
    magnitude of the percent change(up and down) in the stock index since the 
    previous day is greater than the value of the percent input into the function.
    
    Position Input Parameters:
        input 1: a list of float or int numeric values of stock index
        input 2: a float or int numeric value of percent change magnitude
            
    Keyword Input Parameters:
        None
        
    Examples:
    >>> print(num_days_big_percent_chg(stocks.nasdaq,0.6)
    20
    """
    num_days = 0
    for i in range(len(idx_list)):
        if i < len(idx_list)-1:
            if abs((idx_list[i+1] - idx_list[i])/idx_list[i]*100) > percent_chg:
                num_days = num_days +1
    return num_days

# number 5  
def ascending_trading_days (day_list,index_list):
    """Sorts a list of trading days in asc order of daily stock index values.
    
      It sorts a list of stock index values in asc order and returns a list of
    trading days that correspond to the sorted daily stock index values.
    
    Position Input Parameters:
        input 1: a list of int values of trading day
        input 2: a list of float or int numeric values of daily stock index
            
    Keyword Input Parameters:
        None
        
    Examples:
    >>> print(ascending_trading_days(stocks.trading_days, stocks.nasdaq))
    [18, 19, 17, 20, 12, 23, 15, 10, 13, 21, 9, 14, 11, 8, 24, 22, 25, 7, 16, 
    2, 0, 26, 6, 4, 3, 1, 5, 27, 29, 28, 31, 30, 33, 32, 35, 34, 37, 36, 38, 
    43, 39, 40, 44, 41, 45, 42, 49, 60, 47, 64, 59, 61, 46, 63, 48, 53, 50, 54,
    62, 51, 56, 55, 57, 58, 52]
    """
    sort_index_list = index_list.copy()
    sort_day_list = day_list.copy()

    for i in range(len(sort_index_list)):
        # Find the minimum element in remaining
        minPosition = i
        for j in range(i+1, len(sort_index_list)):
            if sort_index_list[minPosition] > sort_index_list[j]:
                minPosition = j
        # Swap the found minimum element with minPosition in index_list     
        temp_index = sort_index_list[i]
        sort_index_list[i] = sort_index_list[minPosition]
        sort_index_list[minPosition] = temp_index
        # Swap the found minimum element with minPosition in day_list     
        temp_day = sort_day_list[i]
        sort_day_list[i] = sort_day_list[minPosition]
        sort_day_list[minPosition] = temp_day    
    return sort_day_list

    
# number 2
percent_of_mean_djia=[] 
percent_of_mean_sp500=[] 
percent_of_mean_nasdaq=[] 

#     calculate the percent_of_mean for stock indexes
percent_of_mean_djia=(percent_of_mean(mydata.djia))
percent_of_mean_sp500=(percent_of_mean(mydata.sp500))
percent_of_mean_nasdaq=(percent_of_mean(mydata.nasdaq))
    
#    plot the percent_of_mean data
fig1 = plt.figure()
fig1.clear()
plt.plot(mydata.trading_days, percent_of_mean_djia,'b-',label="DJIA")
plt.plot(mydata.trading_days, percent_of_mean_sp500,'g-', label="S&P500")
plt.plot(mydata.trading_days, percent_of_mean_nasdaq,'r-', label="NASDAQ")
plt.xlabel('Trading Days Since Jun1, 2016')
plt.ylabel('Percent of Mean')
plt.title('Indices as Percent of Their Means')
plt.legend()
#plt.savefig('SDA.png', dpi=300) #by default it is saved into the current working directory
plt.show()
#plt.close(fig1)

# number 4
percent_chg = [0.2,0.4,0.6,0.8,1.0] #defined percent change magnitude

number_days_djia=[] #def the list of days that dow index exceed the percent chg magnitude
number_days_snp500=[] # def ... that snp500...
number_days_nasdaq=[] # def ... that nasdaq...

#    calculate the number of days that each index has that exceeded the percent chg magnitude
for i in range (len(percent_chg)):
    number_days_djia.append(num_days_big_percent_chg(mydata.djia,percent_chg[i]))
    number_days_snp500.append(num_days_big_percent_chg(mydata.sp500,percent_chg[i]))
    number_days_nasdaq.append(num_days_big_percent_chg(mydata.nasdaq,percent_chg[i]))

#    plot the number_of_days data for stock indexes
fig2 = plt.figure()
fig2.clear()
plt.plot(percent_chg, number_days_djia,'b-', label="DJIA")
plt.plot(percent_chg, number_days_snp500,'g-', label="S&P500")
plt.plot(percent_chg, number_days_nasdaq,'r-', label="NASDAQ")
plt.xlabel('Percent Threshold Value')
plt.ylabel('Number of Days')
plt.title('Number of Days the Daily Percent Change Exceeded \n a Threshold Magnitude')
plt.legend()
#plt.savefig('SDA.png', dpi=300) #by default it is saved into the current working directory
plt.show()
#plt.close(fig2)

# number 6
idx_list = [mydata.djia, mydata.sp500, mydata.nasdaq]
highest_day_list_djia = []
highest_day_list_sp500 = []
highest_day_list_nasdaq = []
output_amount = 5 # amount of output data

#   finds the asked number of highest trading days for each stock index
for i in range(len(idx_list)):
    asc_day_list = ascending_trading_days(mydata.trading_days, idx_list[i])
    asc_day_list.reverse()
    for j in range(output_amount):
        if i==0:
            highest_day_list_djia.append(asc_day_list[j])
        else:
            if i==1:
                highest_day_list_sp500.append(asc_day_list[j])
            else:
                if i==2:
                    highest_day_list_nasdaq.append(asc_day_list[j])
                    
#   print out 5 highest trading days for each stock index
txt = "The "+ str(output_amount)+ " highest trading days for "         
print(txt + "DJIA: " )
print(highest_day_list_djia)
print(txt + "S&P500: " )
print( highest_day_list_sp500)
print(txt + "NASDAQ: " )
print( highest_day_list_nasdaq)
