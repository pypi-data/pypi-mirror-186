import equity.utils as etils

class Debt:
    def yields(maturity):
        """
        * 13 Week (1yr)
        Retrieves risk free return, 13 month CBOE Interest Rate Composite Index (proxy to T-Bill).
        Checked and re-checked, can be trusted. Sources:
        https://help.streetsmart.schwab.com/edge/1.12/Content/Theoretical%20View.htm
        https://www.ruf.rice.edu/~kemmer/Words04/usage/jargon_financial.html

        :Params:
        * maturity (str): "1yr", "5yr", "10yr", "30yr"
        
        :Returns:
        * rf (float): in % form (1.56 = 1.56% YTM)
        """
        # One year T-bill (13 weeks)
        if maturity == "1yr":
            one_yr = etils.Admin.info("^IRX")["regularMarketPrice"]
            return one_yr

        # Five year t-bill
        elif maturity == "5yr":
            five_yr = etils.Admin.info("^FVX")["regularMarketPrice"]
            return five_yr
        
        # Ten year t-bill
        elif maturity == "10yr":
            ten_yr = etils.Admin.info("^TNX")["regularMarketPrice"]
            return ten_yr
        
        # Thirty year t-bill
        elif maturity == "30yr":
            thirty_yr = etils.Admin.info("^TYX")["regularMarketPrice"]
            return thirty_yr