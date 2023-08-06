from charts.indicators import Indicators
import equity.utils as etils

class Trend:
    def bullish(ticker, period, window):
        """
        Check if SMA supports current price of ticker.
        
        :Params:
        * ticker (str): ticker lookup
        * period (str): 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
        * window (int): smoothing window in days
        
        :Returns:
        * Boolean (bool): True if price is above SMA, False if trend broken
        """        
        # calculates SMA for period and select most recent value 
        # to compare to current price
        data = Indicators.sma(ticker, period, window)
        sma_value = data[-1]
        
        # current price
        price = etils.Financial.price(ticker,"1d")["Close"].item()

        # Price is above latest sma_value
        if price > sma_value:
            return True
        else:
            return False
        