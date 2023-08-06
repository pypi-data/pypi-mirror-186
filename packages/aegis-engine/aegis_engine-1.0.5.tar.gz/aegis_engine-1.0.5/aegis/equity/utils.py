import yfinance as yf

class Financial:
    def price(ticker, period, interval = "1d"):
        """
        Return price history for set period.
        
        :Params:
        * ticker (str): ticker lookup
        * period (str): 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
        * interval (str): 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
        
        :Returns:
        * df (DataFrame): cols[open,high,low,close,volume,dividends,stock_splits]
        """
        return yf.Ticker(ticker).history(
            period = period,
            interval = interval
        )

    def price_range(ticker, start, end, interval = "1d"):
        return yf.Ticker(ticker).history(
            start = start,
            end = end,
            interval = interval
        )

    def dividends(ticker):
        return yf.Ticker(ticker).dividends

    def earnings(ticker):
        return yf.Ticker(ticker).earnings

class Admin:
    def object(ticker):
        return yf.Ticker(ticker)

    def info(ticker):
        return yf.Ticker(ticker).info

    def recommendations(ticker):
        return yf.Ticker(ticker).recommendations

    def calendar(ticker):
        return yf.Ticker(ticker).calendar
    
    def holders(ticker):
        return yf.Ticker(ticker).major_holders

class Statement:
    def pnl(ticker):
        return yf.Ticker(ticker).financials

    def bs(ticker):
        return yf.Ticker(ticker).balance_sheet

    def cashflow(ticker):
        return yf.Ticker(ticker).cashflow

class Dividends:
    def ytd_dividend(ticker):
        divs = Financial.dividends(ticker)
        return sum(divs.tail(4))

class Equity:
    def annual_return(ticker):
        """
        :Params:
        * ticker (str): ticker lookup
        
        :Returns:
        * annual_return (float): price change in %
        """
        
        prices = Financial.price(ticker, "1y")
        
        # Select most recent and start price
        start = prices.iloc[0]["Close"]
        end = prices.iloc[-1]["Close"]
        
        # Calculate % change over time
        annual_return = (end - start) / start
        
        return annual_return

    def rm(ticker = "SPY"):
        """
        Market return of index across 1 year. Default SPY.
        
        :Params:
        * ticker (str): index ETF selection, SPY / QQQ recommended
        
        :Returns:
        * rm (float): in % form (15.6 = 15.6% annual return)
        
        """
        # Pull prices
        prices = Financial.price(ticker, "1y")
        
        # Select most recent and start price
        start = prices.iloc[0]["Close"]
        end = prices.iloc[-1]["Close"]
        
        # Calculate % change over time
        rm = (end - start) / start
        
        return rm