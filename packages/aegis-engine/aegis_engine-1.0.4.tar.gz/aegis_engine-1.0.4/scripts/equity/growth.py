import equity.utils as etils

class Growth:
    def dividend(ticker, forward = False):
        """
        Dividend function to calculate 1yr dividend payments, or expected
        annual dividend payments.
        
        :Params:
        * ticker (str): ticker lookup
        * forward (bool): True for projecting forward, False for YTD
                        
        :Returns:
        * d0 or d1 (float): YTD dividend (d0) or forward dividend (d1)
        """
        
        # Getting D0 (annual)
        if forward == False:
            
            d0 = etils.Dividends.ytd_dividend(ticker)
            d0 = sum(d0)
            
            return d0
        
        # Getting D1 (annual)
        elif forward == True:
            
            # D1 = EPS1 * (1 - pb)
            eps1 = etils.Admin.info(ticker)["forwardEps"]
            pb = Growth.pb(ticker)
            d1 = eps1 * (1-pb)
            
            return d1
    
    def pb(ticker):
        """
        Plowback ratio of how much is reinvested into the company from earnings
        
        :Params:
        * ticker (str): ticker lookup
        
        :Returns:
        * pb (float): percentage reinvested (%)
        """
        
        info = etils.Admin.info(ticker)

        # Uses value when avialable
        try:
            pb = 1 - info["payoutRatio"]
            return pb
            
        # Set to 0 incase of Error for manual calculation
        except Exception:
            pb = 0

        # Setting to 0 incase of NoneType for manual calculation
        if pb is None:
            pb = 0

        ytd_divs = etils.Dividends.ytd_dividend(ticker)

        # No divs, so pb = 1
        if ytd_divs.empty is True:
            pb = 1
            return pb

        dividend_value = sum(ytd_divs)        

        # Technically we want avg shareholders over ytd <-- good to implement
        sh_outstanding = info["sharesOutstanding"]

        total_dividends = dividend_value * sh_outstanding

        earnings = earnings.iloc[-1,-1]

        # Recalculated plowback
        pb = 1 - (total_dividends / earnings)

        return pb
    
    def roe(ticker):
        """
        Return on equity - how much return is generated from equity investment
        
        :Params:
        * ticker (str): ticker lookup
        
        :Returns:
        * roe (float): return on equity
        """
        
        earnings = etils.Financial.earnings(ticker)
        bs = etils.Statement.bs(ticker)

        net_income = earnings.iloc[-1,-1]
        
        # shareholders equity in $ amount
        sh_equity = bs.loc["Total Stockholder Equity"][0]

        roe = net_income / sh_equity
        
        return roe
    
    def growth(ticker):
        """
        Expected % growth of company based on reinvestment. Incorporates
        ROE and pb.
        
        :Params:
        * ticker (str): ticker lookup
        
        :Returns:
        * g (float): expected % growth
        """
        
        roe = Growth.roe(ticker)
        b = Growth.pb(ticker)
        
        g = roe * b
        
        return g