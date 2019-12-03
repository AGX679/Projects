import matplotlib.pyplot as plt
import numpy as np
from scipy import genfromtxt

# number 1
def convert_date_to_float(str):
    """Convert a data string in format of 'yyyy-mm-dd' to a float number
    
    Position Input Parameter:
        input1: a string of the format of "yyyy-mm-dd"
            
    Keyword Input Parameters:
        None
        
    Examples:
    >>> print(convert_date_to_float('1950-01-31'))
    19500131.0
    """
    # form a num string from the input date string by split
    num_str = ''
    num_str_list = str.split('-')
    for i in range(len(num_str_list)):
        num_str = num_str + num_str_list[i]

    # convert to float number
    flt_str = float(num_str)
    return flt_str


print('number 1: construct a function to convert date to float. 1950-01-31 => ', convert_date_to_float('1950-01-31'))


# number 2 read csv file into a floating point array

file_obj = open('sp500_1950-01-03_to_2016-10-07.csv', 'r')
contents = file_obj.readlines()  # list of str
file_obj.close()

data2 = np.zeros((len(contents) - 1, 7), dtype='d')  # excluding 1st column_name line, total 7 columns
# spilt each line of data, convert 1st date item into float, load into data2 array
for i in range(len(contents) - 1):
    split_istr = contents[i + 1].split(',') #placeholder for a line of data
    split_istr[0] = convert_date_to_float(split_istr[0]) #converts date inside of placeholder
    #print ('split', split_istr)
    data2[i, :] = split_istr[:]

print('number 2 read data file into a floating point array, data2 =  \n', data2)
#print(data2[:, 1:])
#print(data2[:, 6])

#number 3 read data file into data3 array by using gen
data3 = genfromtxt('sp500_1950-01-03_to_2016-10-07.csv', delimiter=",", skip_header=1, dtype='d')
print('number 3 using genfromtxt to read data file into a floating point array, data3 = \n', data3)

#print(data3[:, 1:])

# number 4 compare data2 to data3
print('Is data2 equal to data3? ', np.allclose(data2[:, 1:], data3[:, 1:]))  # skip the 1st column by slicing

# number 5 plot adj column y and trading days x
adj_array = data2[:, 6]  # getting adj_close array by slicing
#print(np.shape(data2))
trading_days = np.arange(np.shape(data2)[0])  # get total number of rows
print(trading_days)

fig1 = plt.figure()
fig1.clear()
plt.plot(trading_days, adj_array, 'b-', label="S&P500")
plt.xlabel('Trading Days Since Jan 3, 1950')
plt.ylabel('Adjusted Close [USD]')
plt.title('S&P 500 Index Daily Close')
plt.legend()
plt.savefig('number_5_Fig.png', dpi=300)  # by default it is saved into the current working directory
plt.show()
plt.close(fig1)
print("number 5:  Plotting S&P 500 Index Adjusted Close data figure w/ Title as 'S&P 500 Index Daily Close'")

#number 6 - plotting high minus low
high_low_array = data2[:, 2] - data2[:, 3]  # getting array of high-low by array syntax
#print(high_low_array)
fig2 = plt.figure()
fig2.clear()
plt.plot(trading_days, high_low_array, 'b-', label="S&P500")
plt.xlabel('Trading Days Since Jan 3, 1950')
plt.ylabel('Daily High - Low [USD]')
plt.title('S&P 500 Index Daily High Minus Low')
plt.legend()
plt.savefig('number_6_Fig.png', dpi=300)  # by default it is saved into the current working directory
plt.show()
plt.close(fig2)
print("number 6:  Plotting S&P 500 Index Daily high minus low data figure w/ Title as 'S&P 500 Index Daily High Minus Low'")