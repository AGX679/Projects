import numpy as np
import stocks
#number 1
#creates numpy arrays from stocks 
nasdaq_array = np.array(stocks.nasdaq)
sp500_array = np.array(stocks.sp500)
djia_array = np.array(stocks.djia)
days_array = np.array(stocks.trading_days)
print('NASDAQ = ', nasdaq_array)
print('S&P500 = ', sp500_array)
print('DJIA = ', djia_array)

# number 2
# Printing out data type and typecode
print('NASDAQ: ', nasdaq_array.dtype) 
print('NASDAQ: ', nasdaq_array.dtype.char)
print('S&P500: ', sp500_array.dtype) 
print('S&P500: ', sp500_array.dtype.char)
print('DJIA: ', djia_array.dtype)
print('DJIA: ', djia_array.dtype.char)
print('Trading Days: ', days_array.dtype)
print('Trading Days: ', days_array.dtype.char)

#number 3
#printing out shapes of the 4 arrays
print('Array Shapes: ')
print(nasdaq_array.shape)
print(sp500_array.shape)
print(djia_array.shape)
print(days_array.shape)

#number 4
#checks if arrays are equal to each other
if nasdaq_array.shape == sp500_array.shape and djia_array.shape == days_array.shape:
    if nasdaq_array.shape == djia_array.shape:
        print('All arrays are the same shape')
    else: print('All arrays are not the same shape')
else: print('All arrays are not the same shape')

#number 5
#creates array of zeros based on the length of days_array
combined_array = np.zeros((len(days_array),3),dtype='f')
#Fills each column with stock index 
combined_array[:,0] = nasdaq_array
combined_array[:,1] = sp500_array
combined_array[:,2] = djia_array
print(combined_array)

#number 6
#slices elements 21 - 39 from the left 2 columns (SP500 & DJIA)
sub_array = (combined_array[21:40, 1:])
print(sub_array)
print('Shape is: ', sub_array.shape) 
