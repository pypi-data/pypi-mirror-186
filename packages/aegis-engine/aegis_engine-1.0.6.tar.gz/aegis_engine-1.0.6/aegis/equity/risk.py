import equity.utils as etils
import equity.growth as growth
import equity.stats as stats
import debt.utils as dtils

class Risk:
    def beta(ticker):
        """
        :Params:
        * ticker (str): ticker lookup
        
        :Returns:
        * beta (float): Beta of asset
        """
        beta = etils.Admin.info(ticker)["beta"]
        return beta

    def safety_ratio(ticker, threshold):
        annual_return = etils.Equity.annual_return(ticker)
        std = stats.Stats.std(ticker, "1y")
        return (annual_return - threshold) / std

    def sharpe(ticker):
        """
        Sharpe indicates how much return is made per unit of risk.

        E.g. if Sharpe = 0.05, that means 0.05% is made per unit of risk,
        risk being based on rf.
        
        :Params:
        * ticker (str): ticker lookup
        
        :Returns:
        * sharpe (float): Excess return per unit of risk
        """

        k = Risk.cost_of_equity(ticker)
        std = stats.Stats.std(ticker)
        
        sharpe = k / std
        
        return sharpe
    
    def cost_of_equity(ticker, method = "capm"):
        """
        Calculates expected return (cost of equity)

        :Params:
        * ticker (str): ticker lookup
        * method (str): "capm", "forward_eps"
        
        :Return:
        * k (float): expected return % (cost of equity)
        """
        
        if method == "capm":
            # CAPM suggests the expected growth given the level of risk of an asset,
            # the risk of the market, and the risk free asset.
            
            rf = dtils.Debt.yields("1yr")
            rm = etils.Equity.rm()
            beta = Risk.beta(ticker)
           
            # Calculating k
            k = rf + beta * (rm - rf)

            return k

        elif method == "forward_eps":
            # Assuemes that V0 = P0, so the expected yield already reflects the
            # risk. Only works if markets are perfectly efficient.
            # Rarely use - only if other data not present.

            d1 = growth.Growth.dividend(ticker, forward = True)
            p0 = etils.Admin.info(ticker)["regularMarketPrice"]
            g = growth.Growth.growth(ticker)
            
            # Calculating k
            k = (d1 / p0) + g
            
            return k
    
    def wacc(ticker):
        """
        Weighted average cost of capital - annual value from Jan 1. Cost of raising new capital, 
        either debt or equity.
        
        E.g. If WACC is 25%, for every $1 the company earns, $0.25 
        has to be paid to investors
        
        :Params:
        * ticker (str): ticker lookup
        
        :Returns:
        * wacc (float): cost of current capital
        """

        bs = etils.Statement.bs(ticker)
        pnl = etils.Statement.pnl(ticker)
        
        # Market value of equity
        e = bs.loc["Total Stockholder Equity"][0]
        
        # Market value of debt
        d = bs.loc["Total Liab"][0]

        # Cost of equity
        k_e = Risk.cost_of_equity(ticker)

        # Cost of debt
        interest_expense = pnl.loc["Interest Expense"][0]
        
        # Absolute value since interest expense typically negative
        interest_expense = abs(interest_expense)
        
        # Find interest accruing debt (assume only long term debt)
        short_long_term_debt = bs.loc["Short Long Term Debt"][0]
        long_term_debt = bs.loc["Long Term Debt"][0]

        # If no short-long-term debt make it None
        if type(short_long_term_debt) != int:
            short_long_term_debt = 0
        
        interest_accruing_debt = short_long_term_debt + long_term_debt
        
        k_d = (interest_expense / interest_accruing_debt)

        # Marginal tax rate
        income_before_tax = pnl.loc["Income Before Tax"][0]
        ebit = pnl.loc["Ebit"][0]

        t = (ebit - income_before_tax) / income_before_tax
        
        t = abs(t)
        
        # Calculating WACC
        equity_portion = (e / (e+d)) * k_e
        debt_portion = (d / (e+d)) * k_d
        tax_portion = 1-t

        wacc = equity_portion + debt_portion * tax_portion

        return wacc