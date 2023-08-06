import equity.utils as etils

class Bounds:
    def ath(ticker, period):
        """
        All time high
        
        :Params:
        * ticker (str): ticker lookup
        * period (str): 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
        
        :Returns:
        * ath (float): all time high price
        """
    
        data = etils.Financial.price(ticker, period)
        return data["Close"].max()
        
    def atl(ticker, period):
        """
        All time low
        
        :Params:
        * ticker (str): ticker lookup
        * period (str): 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
        
        :Returns:
        * atl (float): all time low price
        """
        
        data = etils.Financial.price(ticker, period)
        return data["Close"].min()