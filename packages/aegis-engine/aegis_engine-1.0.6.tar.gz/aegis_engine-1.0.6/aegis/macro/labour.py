import macro.endpoints as monfig
import macro.utils as mtils

class Labour:

    def employment(country):
        
        # Get URL from endpoints and substitute country for placeholder
        url = monfig.Endpoints.Labour.employment.format(country)
        
        # Pull data, unit adjustment done inside function
        try:
            df = mtils.Sel.dual_series_graph(url, units = True)
        except Exception:
            return None

        return df

    def unemployment(country):
        url = monfig.Endpoints.Labour.unemployment.format(country)
        df = mtils.Sel.dual_series_graph(url, units = True)
        return df

    def unemployment_rate(country):
        url = monfig.Endpoints.Labour.unemp_rate.format(country)
        df = mtils.Sel.single_series_graph(url)
        return df

    def labour_force(country):
        """
        Not always available!
        """
        url = monfig.Endpoints.Labour.labour_force.format(country)
        df = mtils.Sel.dual_series_graph(url, units = True)
        return df

    def salaries(country, type = "nominal"):
        if type == "nominal":
            url = monfig.Endpoints.Labour.salaries.nominal.format(country)
        elif type == "real":
            url = monfig.Endpoints.Labour.salaries.real.format(country)

        df = mtils.Sel.dual_series_graph(url, units = True)
        
        return df