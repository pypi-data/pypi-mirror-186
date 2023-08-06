import equity.utils as etils

# Determine business asset composition
class Accounting:
    
    def asset_composition(ticker):
        bs = etils.Financial.bs(ticker)
        print(bs)