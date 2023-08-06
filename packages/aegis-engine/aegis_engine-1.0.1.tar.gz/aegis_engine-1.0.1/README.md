# Aegis
<p align="center">
    </a>
    <h4 align="center">Multi-dimensional asset valuation engine for capital market securities.</h4>
</p>

<div align="center">
    <a href="https://github.com/itchysnake/aegis/blob/master/LICENSE" target="blank">
        <img src="https://img.shields.io/github/license/itchysnake/aegis" alt="aegis licence"/>
    </a>
    <a href="https://github.com/itchysnake/aegis/fork" target="blank">
        <img src="https://img.shields.io/github/forks/itchysnake/aegis" alt="aegis forks"/>
    </a>
    <a href="https://github.com/itchysnake/aegis/issues" target="blank">
        <img src="https://img.shields.io/github/issues/itchysnake/aegis" alt="aegis issues"/>
    </a>
    <a href="https://github.com/itchysnake/aegis/pulls" target="blank">
        <img src="https://img.shields.io/github/issues-pr/itchysnake/aegis" alt="aegis pull-requests"/>
    </a>
    <img src="https://img.shields.io/github/last-commit/itchysnake/aegis" alt="aegis last-commit"/>
</div>

<p align="center">
    <a href="https://github.com/itchysnake/aegis/issues/new/choose">Report Bug</a>
    ·
    <a href="https://github.com/itchysnake/aegis/issues/new/choose">Request Feature</a>
</p>

# What is Aegis?

`Aegis` is an open source asset valuation engine that uses many dimensions to create a price profile for an asset. A **dimension** is a general category of evaluation. This evaluation may or may not be a _valuation_ as it could just relate to a general fact/figure such as employment statistics.

**Dimensions** are further broken down into components. For example "charts" is a **dimension** which is comprised of **components**: technical indicators, trading psychology, boundaries, and patterns. 

> In terms of package hierarchy: Aegis > Dimension > Component > Class > Function

> E.g. Aegis > Equity > Risk > Risk > Sharpe()

**Dimensions** exist as sub-packages within the Aegis package and can/should be combined by the developer with various other dimensions/components to create hollistic asset valuation. The dimensions and their components are broken down as follows:
* Charts (incomplete)
    * Bounds (e.g. all_time_high, all_time_low))
    * Indicators (e.g. RSI, OBV, SMA)
    * Shapes (e.g. square_consolidating, head_and_shoulders)
    * Trend (e.g. strength, forecast)
* Debt
    * Utilities
* Equity
    * Accounting (e.g. asset_composition, liquidity)
    * Growth (e.g. plowback, roe, growth)
    * Risk (e.g. beta, cost_of_capital, wacc)
    * Statistics (e.g. var, covariance, correlation)
    * Valuation (e.g. div_yield, ddm, fixed_div, gordons, PVGO)
* Macroeconomic (incomplete)
    * GDP (e.g. GDP, gov_consum, investment)
    * Labour (e.g. employment, unemployment, labour_force)
    * Price (e.g. cpi, ppi)
    * Trade
* Rates (incomplete)
* Sentiment (incomplete)

These dimensions and their relevant components allow `Aegis` to evaluate most assets not only according to their accounting book value, but also in accordance with the market, similar-risk products, macro conditions, and more.

# Getting Started

`Aegis` uses common data science libraries such as `pandas` for most of its needs.

### Installation
1. To get started with `aegis`:
```bash
pip install git+ttps://github.com/itchysnake/aegis
```

If this is giving you errors you can alternatively try:

```bash
python -m pip install git+ttps://github.com/itchysnake/aegis
```

2. Check your installation directory

### Usage
Once installed you can get started by calling the package:

```
import aegis

# Using 'charts' dimension
amzn_ath = aegis.charts.bounds.Bounds.ath("AMZN","6mo")
nflx_rsi = aegis.charts.indicators.Indicators.rsi(
    ticker = "NFLX", 
    period =" 6mo",
    window = 14
)

# Using 'equity' dimension
aapl_roe = aegis.equity.growth.Growth.roe("AAPL")
msft_risk = aegis.equity.risk.Risk.sharpe("MSFT")

# Using 'macro' dimension
spain_labour = aegis.macro.labour.Labour.unemployment("Spain")
jpn_gdp = aegis.macro.gdp.GDP.gdp("Japan", type = "real")
```

Feel free to experiment and combine indicators to create valuable insights into the markets.

# Data Procurement

Data procurement is not included in Aegis natively. I am currently building a package to integrate Aegis with the existing [Alpaca Markets API](https://github.com/alpacahq/alpaca-trade-api-python). At this time you must use whatever is comfortable for you.

# License

Aegis is released under the [MIT License](https://github.com/itchysnake/aegis/blob/master/LICENSE).