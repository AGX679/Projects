import stocks
import statistics
import matplotlib.pyplot as plt
#run this method for the calculations of the stock indexes
def calculations():
    #assigning variables to the results of mean calculations
    nm = statistics.mean(stocks.nasdaq) 
    sm = statistics.mean(stocks.sp500)
    dm = statistics.mean(stocks.djia)
    #assigning variables to the results of standard deviation calculations
    nsd = statistics.stdev(stocks.nasdaq)
    ssd = statistics.stdev(stocks.sp500)
    dsd = statistics.stdev(stocks.djia)
    #assigning variabels to the standard deviation as a ratio of the mean
    x = nsd/nm
    y = ssd/sm
    z = dsd/dm
    #printing to the console
    print('DJIA mean: ' + str(dm))
    print('S&P500 mean: ' + str(sm))
    print('NASDAQ mean: ' + str(nm))
    print('DJIA standard deviation:  ' + str(dsd))
    print('S&P500 standard deviation: ' + str(ssd))
    print('NASDAQ standard deviation: ' + str(nsd))
    print('DJIA standard deviation as ratio of mean: ' + str(z))
    print('S&P500 standard deviation as ratio of mean: ' + str(y))
    print('NASDAQ standard deviation as ratio of mean: ' + str(x))
    
    return
print(calculations())
    
    
#run this method to show the plots for the indexes    
def plots():
    #assigning index values to variables
    djia = stocks.djia
    sp500 = stocks.sp500
    nasdaq = stocks.nasdaq
    days = stocks.trading_days 
    
    #plotting the individual graphs 
    plt.figure(1)
    plt.plot(days, djia,'b-')
    plt.axis([0, 70, 17000, 18800])
    plt.savefig('djiaplot.png', dpi = 300) #saving the plot as a png to the file
    
    plt.figure(2)
    plt.plot(days, nasdaq, 'r-')
    plt.axis([0, 70, 4500, 5500])
    plt.savefig('nasdaqplot.png', dpi = 300)
    
    plt.figure(3)
    plt.plot(days, sp500, 'g-')
    plt.axis([0, 70, 1500, 2500])
    plt.savefig('sp500plot.png', dpi = 300)
    
    #plotting the collective graph with a legend
    plt.figure(4)
    plt.plot(days, djia, 'b-', label = "DJIA") 
    plt.plot(days, nasdaq, 'r-', label = "NASDAQ")
    plt.plot(days, sp500, 'g-', label = "S&P500")
    plt.axis([0, 70, 2000, 20000])
    plt.legend()
    plt.savefig('combinedplot.png')
    #rendering all figures 
    plt.show()
    #print("end")
 
    return
    
plots()