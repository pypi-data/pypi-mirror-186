import equity.utils as etils
import equity.growth as growth
import equity.risk as risk

class Valuation:
    def div_yield(ticker):
        divs = etils.Dividends.ytd_dividend(ticker)
        price = etils.Admin.info(ticker)["regularMarketPrice"]
        return divs/price

    def dupont(ticker):
        pass

    def book_val(ticker):
        """
        Book value according to assets and liabilities
        
        :Params:
        * ticker (str): ticker lookup
        
        :Returns:
        * book_val (float): basic book value per share
        """
        bs = etils.Statement.bs(ticker)
        info = etils.Admin.info(ticker)
        
        # Total assets
        assets = bs.loc["Total Assets"][0]
        
        # Total liabilities
        liabilities = bs.loc["Total Liab"][0]
        
        # Should be avg ! <!-- good to implement
        sh_outstanding = info["sharesOutstanding"]
        
        book_val = (assets - liabilities) / sh_outstanding
        
        return book_val
    
    def future_price(ticker, years = 1):
        """
        Price in x number of years based on today's price multipied by growth rate. 
        Believes price already reflects risk (therefore yield = growth + risk).
        
        :Params:
        * ticker (str): ticker lookup
        
        :Returns:
        * p1 (float): expected price in x number of yrs
        """
        
        info = etils.Admin.info(ticker)

        p0 = info["regularMarketPrice"]
        g = growth.Growth.growth(ticker)
        
        p1 = p0*(1+g) ** years
        
        return p1
    
    def fixed_dividend_model(ticker):
        """
        Assumes g = 0, often try for REIT's or fixed investment vehicles. Typically
        designed for long-term investments.
        
        :Params:
        * ticker (str): ticker lookup
        
        :Returns:
        * v0 (float): intrinsic value
        """
        
        d1 = growth.Growth.dividend(ticker, forward = True)
        k = risk.Risk.cost_of_equity(ticker)
        
        v0 = d1 / k
        
        return v0
    
    def no_growth_model(ticker):
        """
        Similar to fixed_dividend_model by assuming g = 0. fixed_dividend_model
        requires a company to pay dividends, whereas no_growth assumes there are
        no dividends being paid. no_growth assumes that all of EPS is
        paid out (b = 0).
        
        :Params:
        * ticker (str): ticker lookup
        
        :Returns:
        * v0 (float): intrinsic value with full dividend payout
        """
        
        info = etils.Admin.info(ticker)
        eps1 = info["forwardEps"]
        k = risk.Risk.cost_of_equity(ticker)
        
        v0 = eps1 / k
        
        return v0
    
    def gordons_model(ticker):
        """
        Assumes that dividends grow constantly. The classic evaluation model.
        Requires k > g.
        
        Returns 0 if condition fails.
        
        :Params:
        * ticker (str): ticker lookup
        
        :Returns:
        * v0 (float): intrinsic value
        """
        
        d1 = growth.Growth.dividend(ticker, forward = True)
        k = risk.Risk.cost_of_equity(ticker)
        g = growth.Growth.growth(ticker)

        # Condition
        if k > g:
            
            v0 = d1 / (k - g)
            
            return v0
        
        else:
            return 0
    
    def ddm(ticker, years = 5):
        """
        Dividend discount model (DDM) - calculates intrinsic value based on
        dividend growth and final expected price.

        Assumes fixed dividend. !! <-- Fix to increase with g?
        
        If years are set to high values (8+) the price will decline to 0 if 
        k > g. This is bc the asset doesn't beat the market, over that
        many years the market is expected to have caught up.
        
        E.g. As of today 10 year V0 for MSFT is $79 since k > g by almost 2x.
        
        Returns None if company does not pay dividends.
        
        :Params:
        * ticker (str): ticker lookup
        * years (int): years the asset is estimated to be held
        
        :Returns:
        * v0 (float): intrinsic value
        """

        d0 = growth.Growth.dividend(ticker, forward = False)
        p1 = Valuation.future_price(ticker, years)
        k = risk.Risk.cost_of_equity(ticker)
        g = growth.Growth.growth(ticker)

        dividends = []

        # All intermediary years
        for t in range(1,years):
            
            # Present value of dividend @ t
            d_t = (d0*(1+g)**t) / ((1+k)**t)
            
            # Add to list
            dividends.append(d_t)
            
        # Final year
        d_t = (p1 + d0*(1+g)**years) / (1+k)**years
        
        # Calculating intrinsic
        v0 = sum(dividends) + d_t
        
        return v0
    
    def pvgo(ticker):
        """
        Present value of growth opportunities measures the speculative portion
        of a stock price. Price is comprised of the stock no-growth value (full
        dividend payment) plus the pvgo. 
        
        :Params:
        * ticker (str): ticker lookup
        
        :Returns:
        * pvgo (float): present value of growth opportunities (speculation)
        """
        
        growth = Valuation.gordons_model(ticker)
        
        # Incase k < g use DDM
        if growth == 0:
            growth = Valuation.ddm(ticker)
            
        # Incase growth still = 0 bc no dividends, use future price (inaccurate)
        elif growth == 0:
            growth = Valuation.future_price(ticker, 3)
        
        no_growth = Valuation.no_growth_model(ticker)

        pvgo = growth - no_growth
        
        return pvgo

    def pe(ticker, method = "classic"):
        """
        Price to earnings (P/E) for EOY. Assumes EOY P/E is priced into current
        market price. This is an important assumption for PEG.
        
        :Params:
        * ticker (str): ticker lookup
        * method (str): "classic","pvgo","roe"
        
        :Returns:
        * pe (float): price to earnings ratio
        """
        
        info = etils.Admin.info(ticker)
        
        if method == "classic":
            p1 = Valuation.future_price(ticker, 1)
            eps1 = info["forwardEps"]
            
            pe = p1 / eps1
            
            return pe
        
        if method == "pvgo":
            k = risk.Risk.cost_of_equity(ticker)
            eps1 = info["forwardEps"]
            pvgo = Valuation.pvgo(ticker)
            
            pe = (1/k) * (1+ (pvgo / (eps1 / k)))
        
            return pe
        
        if method == "roe":
            k = risk.Risk.cost_of_equity(ticker)
            b = growth.Growth.pb(ticker)
            roe = growth.Growth.roe(ticker)
            
            pe = (1-b) / (k- (roe * b))
            
            return pe
        
    def peg(ticker):
        """
        P/E to Growth. PEG expected to sit around 1 since price, earnings, and
        growth should be roughly equal for fairly valued assets. PEG's < 1 suggest
        price is lower than earnings and growth expectations, and PEG's > 1
        suggest higher speculative prices than earnings and growth expectations.
        
        Avoid negative PEG's since it suggests either Growth is negative or
        EPS is negative (or both due to calculation modification). 
        
        :Params:
        * ticker (str): ticker lookup
        
        :Returns:
        * peg (float): price to earnings to growth ratio
        """
        
        pe = Valuation.pe(ticker)
        
        # Has to be used in 100% format otherwise calculation incorrect
        g = growth.Growth.growth(ticker) * 100
        
        # If both EPS and G are negative, to prevent it from being registereed
        # as a positive number when divided, the post-calc value is multiplied
        # by -1
        
        if (pe <=0) and (g <= 0):

            peg = -1 * (pe / g)
            
            return peg
        
        # Normal calculation
        peg = pe / g
        
        return peg

    def grindold_kroner(ticker):
        div_yield = Valuation.div_yield(ticker)
        change_in_shares = None
        inflation = None
        earnings_growth = None
        pe_change = None
        expected_return = div_yield - change_in_shares + inflation + earnings_growth + pe_change
        return expected_return