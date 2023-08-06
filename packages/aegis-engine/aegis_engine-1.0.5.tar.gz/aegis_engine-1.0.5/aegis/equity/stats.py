import numpy as np
import equity.utils as etils

class Stats:
    def price(ticker):
        return etils.Admin.info(ticker)["regularMarketPrice"]

    def var(ticker, period):
        """
        Returns sample variance (volatility) of a stock over a period of time
        
        :Params:
        * ticker (str): ticker lookup
        * period (str): period of time for lookup
        
        :Returns:
        * var (float): Variance of closing price over period in relation to mean
        """
        # Prices
        close_prices = etils.Financial.price(ticker, period)["Close"]
        
        # Mean
        mean = int(np.mean(close_prices))
        
        # Error (xi - x_bar)^2
        sum_vals = 0
        for num in close_prices:
            sum_vals += (int(num) - mean)**2
        
        #Divide by n-1 (sample pop)
        n = len(close_prices) - 1
        
        var = sum_vals / n
        
        return var
    
    def std(ticker, period):
        """
        Calculates standard deviation of an asset
        
        :Params:
        * smybol (str): ticker lookup
        * period (int): period data requested
        
        :Returns:
        * std (float): Standard deviation
        """
        var = Stats.var(ticker, period)
        
        std = np.sqrt(var)

        return std
    
    def cov(tick_1, tick_2, period):
        """
        Calculates covariance between two assets
        
        :Params:
        * tick_1 (str): Ticker lookup #1
        * tick_2 (str): Ticker lookup #2
        * period (int): Period of data to be considered
        
        :Returns:
        * cov (float): Covariance  
        """
        # Close prices
        closes_1 = etils.Financial.price(tick_1, period)["Close"]
        closes_2 = etils.Financial.price(tick_2, period)["Close"]
        
        # Mean
        mean_1 = np.mean(closes_1)
        mean_2 = np.mean(closes_2)

        # Sum of (return a - mean a * return b - return b) - COV formula
        diff_1 = closes_1 - mean_1
        diff_2 = closes_2 - mean_2

        sum_vals = 0
        for i in range(len(diff_1)):
            sum_vals += diff_1[i] * diff_2[i]

        #Divide by n-1 (bc of sample population)
        n = len(closes_1) - 1
        
        cov = (sum_vals / n)
        
        return cov
    
    def corr(tick_1, tick_2, period):
        """
        Calculates correlation between two assets
        
        :Params:
        * tick_1 (str): Ticker lookup #1
        * tick_2 (str): Ticker lookup #2
        * period (int): Period of data to be considered
        
        :Returns:
        * corr (float): Correlation value
        """
        cov = Stats.cov(tick_1, tick_2, period)
        std_1 = Stats.std(tick_1, period)
        std_2 = Stats.std(tick_2, period)
        
        corr = cov / (std_1 * std_2)
        
        return corr