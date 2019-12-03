import matplotlib.pyplot as plt
import scipy as sp
import numpy as np
import stocks

# number 1
def percent_of_mean(input_array):
    """Convert daily stock index into a percent of the mean over a period of time.
    
        It calculates an array (1-D) of the value of the stock index for each day as a
      percent of the mean value over the period covered by the array and returns
      an array of the value of percent of the mean.
    
    Position Input Parameter:
        input: an 1-D array of float or int numeric values of stock index
            
    Keyword Input Parameters:
        None
        
    Examples:
    >>> print(percent_of_mean(np.array(stocks.nasdaq)))
    [ 98.34635362  98.72585493  98.15312669  98.67323073  98.53501339
  98.79099764  98.47285729  97.20048987  96.28479761  96.18768477
  96.01650822  96.21489382  95.32958146  96.06178229  96.19185437
  95.98452836  97.50810924  93.49541399  91.24063105  93.17548946
  94.91075987  96.17021124  96.56540187  95.77759993  96.49768954
  96.84819761  98.43591272  99.06902257  99.74779435  99.40840845
  99.97101332  99.88223966 100.4023437  100.01688859 101.0805337
 100.76218971 101.28369009 101.23344159 101.48008787 102.07109447
 102.37235277 102.51434215 102.95263479 102.02978634 102.46688629
 102.59616324 103.68582469 103.52735088 103.77240688 103.35735732
 103.83039338 103.91956462 104.49805273 103.8047746  103.83556175
 104.06373573 104.02858506 104.15211184 104.45952757 103.61770509
 103.50868464 103.64213119 103.90844245 103.7229632  103.52894114]
    """
    mean_of_array = sp.mean(input_array)
    percent_array = input_array / mean_of_array * 100
    return percent_array
#prints example with nasdaq info
print(percent_of_mean(np.array(stocks.nasdaq)))

# number 2
#     calculate the percent_of_mean for stock indexes
percent_of_mean_djia = (percent_of_mean(np.array(stocks.djia)))
percent_of_mean_sp500 = (percent_of_mean(np.array(stocks.sp500)))
percent_of_mean_nasdaq = (percent_of_mean(np.array(stocks.nasdaq)))

#    plot the percent_of_mean data
fig1 = plt.figure()
fig1.clear()
plt.plot(stocks.trading_days, percent_of_mean_djia, 'b-', label="DJIA")
plt.plot(stocks.trading_days, percent_of_mean_sp500, 'g-', label="S&P500")
plt.plot(stocks.trading_days, percent_of_mean_nasdaq, 'r-', label="NASDAQ")
plt.xlabel('Trading Days Since Jun1, 2016')
plt.ylabel('Percent of Mean')
plt.title('Indices as Percent of Their Means')
plt.legend()
plt.savefig('number_2.png', dpi=300)  # by default it is saved into the current working directory
plt.show()
plt.close(fig1)
print("Plotting percent_of_mean data on figure shown w/ Title as 'Indices as Percent of Their Means' \n")


# number 3
def num_days_big_percent_chg(input_array, percent_chg):
    """Calculates the number of days for defined big changes.
    
      It calculates and returns the total number of trading days where the 
    magnitude of the percent change(up and down) in the stock index since the 
    previous day is greater than the value of the percent input into the function.
    
    Position Input Parameters:
        input 1: an array of float or int numeric values of stock index
        input 2: a float or int numeric value of percent change magnitude
            
    Keyword Input Parameters:
        None
        
    Examples:
    >>> print(num_days_big_percent_chg(np.array(stocks.nasdaq),0.6)
    20
    """
    a1 = np.array(input_array[:len(input_array)-1])
    a2 = np.array(input_array[1:])
    a3 = str(np.logical_or((a2-a1)/a1*100 > percent_chg, (a2-a1)/a1*100 < percent_chg * (-1)))
    num_days = np.char.count(a3, 'True')
    return num_days
#number 3 printed out
print(num_days_big_percent_chg(np.array(stocks.nasdaq),0.6))


# number 4
percent_chg = [0.2, 0.4, 0.6, 0.8, 1.0]  # defined percent change magnitude

number_days_djia = []  # def the list of days that dow index exceed the percent chg magnitude
number_days_snp500 = []  # def ... that snp500...
number_days_nasdaq = []  # def ... that nasdaq...

#    calculate the number of days that each index has that exceeded the percent chg magnitude
for i in range(len(percent_chg)):
    number_days_djia.append(num_days_big_percent_chg(np.array(stocks.djia), percent_chg[i]))
    number_days_snp500.append(num_days_big_percent_chg(np.array(stocks.sp500), percent_chg[i]))
    number_days_nasdaq.append(num_days_big_percent_chg(np.array(stocks.nasdaq), percent_chg[i]))

#    plot the number_of_days data for stock indexes
fig2 = plt.figure()
fig2.clear()
plt.plot(percent_chg, number_days_djia, 'b-', label="DJIA")
plt.plot(percent_chg, number_days_snp500, 'g-', label="S&P500")
plt.plot(percent_chg, number_days_nasdaq, 'r-', label="NASDAQ")
plt.xlabel('Percent Threshold Value')
plt.ylabel('Number of Days')
plt.title('Number of Days the Daily Percent Change \nExceeded a Threshold Magnitude')
plt.legend()
plt.savefig('number_4.png', dpi=300)  # by default it is saved into the current working directory
plt.show()
plt.close(fig2)
print("Plotting number_of_days data on figure shown w/ Title as 'Number of Days the Daily Percent Change' \n")


# number 5
def moving_average(stock_index_array):
    """Calculate Three-Day moving average for stock index values over a period of time.
    
      It takes an array of stock index values to calculate 3-day moving average for each
    index value over a list of trading days that correspond to the given daily stock index values.
    
    Position Input Parameters:
        input: a 1-D array of float or int numeric values of daily stock index
            
    Keyword Input Parameters:
        None
        
    Examples:
    >>> print(moving_average(np.array(stocks.djia)))

    """
    #creates 3 arrays and populates them with offset versions of the input array, (by 3 days)
    a1 = stock_index_array[:len(stock_index_array)-2]
    a2 = stock_index_array[1:len(stock_index_array)-1]
    a3 = stock_index_array[2:]
    #calculating average between arrays
    moving_average_3_day = (a1+a2+a3)/3
    return moving_average_3_day
#prints example using DJIA stock index
print(moving_average(np.array(stocks.djia)))


# number 6
#storing the stocks in a list, storing the moving averages in variables
stock_index_list = ['DJIA', 'S&P500', 'NASDAQ']
moving_average_3day_djia = moving_average(np.array(stocks.djia))
moving_average_3day_snp500 = moving_average(np.array(stocks.sp500))
moving_average_3day_nasdaq = moving_average(np.array(stocks.nasdaq))
#array for the number of trading days, to be used in plotting
moving_average_3day_trading_days = np.array(stocks.trading_days)[2:]

#Looping through the stock_index_list to individually plot all three graphs
for i in range(len(stock_index_list)):
    fig3 = plt.figure()
    fig3.clear()
    if stock_index_list[i] == "DJIA":
        plt.plot(moving_average_3day_trading_days, moving_average_3day_djia, 'b-', label="MA")
        plt.plot(stocks.trading_days, stocks.djia, 'g-', label="non-MA")
    elif stock_index_list[i] == "S&P500":
        plt.plot(moving_average_3day_trading_days, moving_average_3day_snp500, 'b-', label="MA")
        plt.plot(stocks.trading_days, stocks.sp500, 'g-', label="non-MA")
    elif stock_index_list[i] == "NASDAQ":
        plt.plot(moving_average_3day_trading_days, moving_average_3day_nasdaq, 'b-', label="MA")
        plt.plot(stocks.trading_days, stocks.nasdaq, 'g-', label="non-MA")
    else:
        print("Unknown stock index defined, no data available.") #debug
    #plot labels
    plt.xlabel('Trading Days Since Jun 1, 2016')
    plt.ylabel('Moving Average of Index')
    plt.title('Three-Day Moving Average of ' + stock_index_list[i])
    plt.legend()
    plt.savefig('number_6' + stock_index_list[i] + '.png', dpi=300)  # by default saved into the current working directory
    plt.show()
    plt.close(fig3)
print("Plotting moving average data on figure saved w/ Title as 'Three-Day Moving Average of [Stock Index]' \n")


