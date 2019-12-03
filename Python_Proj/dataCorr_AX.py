import matplotlib.pyplot as plt
import numpy as np
import stocks


# number 1
def calculate_correlation(x, y):
    """Calculates and returns the correlation coefficient between 2 stock indexes arrays over a period of time.
        1. Calculate the mean of each of those 2 input arrays - Mx, My
        2. Calculate the standard deviation of each of those 2 input arrays - Sx, Sy
        3. Calculate the standardized value for each element of these 2 input arrays - Zx=(x-Mx)/Sx,Zy=(y-My)/Sy
        4. Multiply corresponding standardized values for each element in these 2 input array: (Zx)(Zy)
        5. r = Sum(Zx * Zy) / (size of array) - 1
    
    Position Input Parameter:
        input1: an 1-D array of float or int numeric values of stock index
        input2: an 1-D array of float or int numeric values of stock index
            
    Keyword Input Parameters:
        None
        
    Examples:
    >>> print(calculate_correlation(np.array(stocks.djia), np.array(stocks.sp500))
    r_xy 0.990238980023
    """
    # 1. calculate mean
    mean_x = sum(x)/len(x)
    #print(mean_x)
    mean_y = sum(y)/(len(y))
    #print(mean_y)

    # 2. calculate standard deviation
    square_difference_x = (x-mean_x)**2
   # print("square_difference_x", square_difference_x)
    square_difference_y = (y-mean_y)**2
    
    sd_x = (sum(square_difference_x)/np.size(square_difference_x))**0.5
    
    #print('sd for x', sd_x)
    sd_y = (sum(square_difference_y)/np.size(square_difference_y))**0.5

    # 3. standardized values
    std_value_x = (x - mean_x)/sd_x
    #print('std_value_x', std_value_x)
    std_value_y = (y - mean_y)/sd_y

    # 4. product of std_value_x and std_value_y
    product_std_value_xy = std_value_x * std_value_y
    
    # 5. correlation coefficient
    r_xy = sum(product_std_value_xy)/(np.size(product_std_value_xy)) #for sample, subtract 1 from size
    #print('r_xy', r_xy)
    return r_xy


print("Correlation coefficient between DJIA and SP500: ",calculate_correlation(np.array(stocks.djia), np.array(stocks.sp500)))
print("Correlation coefficient between DJIA and NASDAQ: ",calculate_correlation(np.array(stocks.djia), np.array(stocks.nasdaq)))
print("Correlation coefficient between NASDAQ and SP500: ",calculate_correlation(np.array(stocks.sp500), np.array(stocks.nasdaq)))

# number 2 calculate lag autocorrelation for stock indexes
def calculate_lag_autocorrelation(idx_list, lag_num):
    """Calculates the lag autocorrelation for each of the three stock indices. Only postive lags are considered
    
    Position Input Parameter:
        input1: an 1-D array of stock indexes
        input2: an integer to represent lag
            
    Keyword Input Parameters:
        None
        
    Examples:
    >>> print(calculate_lag_autocorrelation(stocks.djia, 10))
    [1.0, 0.94274477606224005, 0.87613897858876788, 0.82053907230460599, 0.78902603514220415, 
    0.77658686261377485, 0.75364691598615852, 0.71420725321334066, 0.67252352766884349, 0.61235507721533955, 0.56619517510107154]
    """
    lags = np.arange(lag_num+1) #from day 0 to day 10
    correlation = []
    for ilag in lags:
        if ilag == 0:
            correlation.append(1.0)
        else:
            x = idx_list[0:-ilag]
            #print('lag before',ilag, x)
            y = idx_list[ilag:]
            #print('lag after',ilag, y)
            correlation.append(calculate_correlation(np.array(x), np.array(y)))
    return correlation


print('Lag Autocorrelation of DJIA: ', calculate_lag_autocorrelation(stocks.djia, 10))
print('Lag Autocorrelation of NASDAQ: ',calculate_lag_autocorrelation(stocks.nasdaq, 10))
print('Lag Autocorrelation of SP500: ',calculate_lag_autocorrelation(stocks.sp500, 10))

# number 3   plot the lag correlation, 10 days,  data for stock indexes
lag_num = 10
lag_autocorrelation_djia = calculate_lag_autocorrelation(stocks.djia, 10)
lag_autocorrelation_sp500 = calculate_lag_autocorrelation(stocks.sp500, 10)
lag_autocorrelation_nasdaq = calculate_lag_autocorrelation(stocks.nasdaq, 10)
lags = np.arange(lag_num+1)

#print(lag_autocorrelation_djia)
#print(lag_autocorrelation_sp500)
#print(lag_autocorrelation_nasdaq)

fig1 = plt.figure()
fig1.clear()
plt.plot(lags, lag_autocorrelation_djia, 'b--o', label="DJIA")
plt.plot(lags, lag_autocorrelation_sp500, 'g--o', label="S&P500")
plt.plot(lags, lag_autocorrelation_nasdaq, 'r--o', label="NASDAQ")
plt.xlabel('Lag in Number of Days')
plt.ylabel('Correlation Coefficient')
plt.title('Lag Autocorrelation for DJIA, S&P500 and NASDAQ')
plt.legend()
plt.savefig('number_3.png', dpi=300)  # by default it is saved into the current working directory
plt.show()
plt.close(fig1)
print("number-3  Plotting lag autocorrelation data figure w/ Title as 'Lag Autocorrelation for DJIA, S&P500 and NASDAQ ' \n")

#number 4
"""There is a closer relationship between the correlation coefficient for DJIA and SP500 compared to NASDAQ, as the first two are nearly identical up until day 3.
    Overall, the correlation coefficent for all three stock indexes show a downward trend as the number of days increase. 
    """
