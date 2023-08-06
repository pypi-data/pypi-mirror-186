import equity.utils as etils
import charts.utils as ctils
import pandas as pd

class Indicators:
    def sma(ticker, period, window):
        """
        Smoothed price series over a period of time averaged by a window
        
        :Params:
        * ticker (str): ticker lookup
        * period (str): 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
        * window (int): smoothing window in days
        
        :Returns:
        * sma (series): Simple moving average price sequence
        """
        
        data = etils.Financial.price(ticker, period)

        # pd.series for holding data
        sma = pd.Series(dtype="float64")
        
        # calculate sma for closing prices located at [:,3]
        sma = data.iloc[:,3].rolling(window=window).mean()
        
        return sma
        
    def roc(ticker, period, window, smooth=False):
        """
        Speed at which price changes (derivative of price action)
        
        :Params:
        * ticker (str): ticker lookup
        * period (str): 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
        * window (int): smoothing window in days
        
        :Returns:
        * roc (series): Rate of price change between days
        """
        
        data = etils.Financial.price(ticker, period)
        roc = pd.Series(dtype="float64")
        
        # calculating roc
        data = data["Close"]
        
        for i in range(len(data)-1):
            
            # calculating dydx
            calc = ((data[i+1]-data[i]) / data[i])*100
            calc = float(round(calc,2))
            
            # getting index
            index = data.index[i]
            
            # setting [index, value] in pd.series
            roc[index] = calc

        # smoothed roc
        if smooth == True:
            roc = ctils.smooth(roc,window)
            return roc
        
        return roc
    
    def obv(ticker, period, window, smooth=False):
        """
        Change in trading volume over a period depending on price action
        
        :Params:
        * ticker (str): ticker lookup
        * period (str): 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
        * window (int): smoothing window in days(tighter here for greater responsiveness)
        
        :Returns:
        * obv (series): Smoothed change in trading volume over time
        
        :Issues:
        * Return being presented as float, not int
        """
        # data pull
        data = etils.Financial.price(ticker, period)
        
        # pd.series for holding data
        obv = pd.Series(dtype="int64")
        
        # calculating obv
        volume = data["Volume"]
        close = data["Close"]
        
        # initial OBV is just the day 0 volume
        index = data.index[0]
        obv[index] = volume[0]

        # three possibilities depending on price movement
        # starting from day+1 so we can compare to "yesterday" - makes notation easier        
        for i in range(1, len(data)):
            
            #if todays close > yesterdays close, add todays vol to yesterdays obv
            if close[i-1] < close[i]:
                daily_obv = obv[i-1] + volume[i]
                
            # if todays close = yesterdays close, add 0 to yesterdays obv
            elif close[i-1] == close[i]:
                daily_obv = obv[i-1] + 0
            
            # if todays close < yesterdays close, subtract todays vol from yesterdays obv
            elif close[i-1] > close[i]:
                daily_obv = obv[i-1] - volume[i]
                
            # getting index
            index = data.index[i]
            
            # setting [index, value] in pd.series
            obv[index] = daily_obv

        # smoot obv
        if smooth == True:
            obv = ctils.smooth(obv,window)
            return obv

        return obv
    
    def rsi(ticker, period, window):
        """
        Number of recurring positive or negative opens
        
        :Params:
        * ticker (str): ticker lookup
        * period (str): 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
        * window (int): smoothing window in days
        
        :Returns:
        * rsi (series): Smoothed relative strength of trend
        """
        data = etils.Financial.price(ticker, period)
        data = data["Close"]
        
        # difference in price from previous step
        delta = data.diff()
        
        # removing first row of NaN
        delta = delta[1:] 
        
        # Make the positive gains (up) and negative gains (down) Series
        up, down = delta.copy(), delta.copy()
        up[up < 0] = 0
        down[down > 0] = 0
        
        # Calculate the SMA
        roll_up = up.rolling(window).mean()
        roll_down = down.abs().rolling(window).mean()
        
        # Calculate the RSI based on SMA
        rs = roll_up / roll_down
        rsi = 100.0 - (100.0 / (1.0 + rs))
        
        return rsi
    
    def reversion(ticker, period):
        """
        Calculates reversion target price based on period high and low
        
        :Params:
        * ticker (str): ticker lookup
        * period (str): 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
        
        :Returns:
        * target (float): mean of period price (expected reversion target)
        """
        data = etils.Financial.price(ticker,period)
        
        # For 1 day closing price is same, so use high and low
        if period == "1d":
            high = data["High"]
            low = data["Low"]

        else:
            high = data["Close"].max()
            low = data["Close"].min()
        
        target = (high + low) / 2
        
        return target