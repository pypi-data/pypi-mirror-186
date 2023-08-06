import pandas as pd

# Testing equity
from equity import risk
from equity import growth
from equity import valuation
import equity.utils as etils

# Testing debt
import debt.utils as dbtils
#print(dbtils.Debt.yields("5yr"))

# testing macro 
import macro
import macro.utils as mtils

# Testing charts and plotting
from charts.trend import Trend
from charts.indicators import Indicators
import plot.utils as ptils

# Strategy type test
import strategy.stocks

strategy.stocks.run()

"""
events:
    cost-push inflation
        cost of labour up
        commodities up
        inflation up
    demand-pull inflation
        increase in money supply
            low rates
            growing wage / disposable income
        increase gov spending in private sector
        aggregate demand > aggregate supply
        foreign interest in domestic goods
        inflation up

GICS


#Buy!? Table!
            equity          debt            cash        real assets         commodities
infl        *1              no!             no!         yes!                *2 
intrst up   no!             *3              none        none                none


infl        REITs           IT          ConsumerDescr

*1: Yes! if the equity passes on growing inflation to consumers
*2: Yes! Depends on the commodities tho: gold is a hedge, while others represent 
    increased demand for goods
*3: New debt: yes!, existing debt: no!

if inflation is high, don't hold cash!

if inflation is low, ok to hold cash!
"""