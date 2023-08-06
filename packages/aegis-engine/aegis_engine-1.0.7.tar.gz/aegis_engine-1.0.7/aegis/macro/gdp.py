import macro.endpoints as monfig
import macro.utils as mutils

class GDP:

    def gdp(country, type="nominal"):
        
        # Get URL from endpoints and substitute country for placeholder
        if type == "nominal":
            url = monfig.Endpoints.GDP.nominal.format(country)
        elif type == "real":
            url = monfig.Endpoints.GDP.real.format(country)

        # Pull data, unit adjustment done inside function
        try:
            gdp = mutils.Sel.dual_series_graph(url, units = True)
        except Exception:
            raise TypeError("Graph extraction")

        return gdp

    def priv_consum(country, type="nominal"):
        if type == "nominal":
            url = monfig.Endpoints.GDP.consumption.private.nominal.format(country)
        elif type == "real":
            url = monfig.Endpoints.GDP.consumption.private.real.format(country)
        
        try:
            c = mutils.Sel.dual_series_graph(url, units = True)
        except Exception:
            return None
        
        return c

    def gov_consum(country, type="nominal"):
        if type== "nominal":
            url = monfig.Endpoints.GDP.consumption.gov.nominal.format(country)
        elif type == "real":
            url = monfig.Endpoints.GDP.consumption.gov.real.format(country)
        
        g = mutils.Sel.dual_series_graph(url, units = True)

        return g

    def investment(country, type="nominal"):
        if type== "nominal":
            url = monfig.Endpoints.GDP.investment.nominal.format(country)
        elif type == "real":
            url = monfig.Endpoints.GDP.investment.real.format(country)
        
        i = mutils.Sel.dual_series_graph(url, units = True)

        return i
