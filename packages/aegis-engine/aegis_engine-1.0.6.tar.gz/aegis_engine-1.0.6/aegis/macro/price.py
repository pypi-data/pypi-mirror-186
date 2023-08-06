import macro.endpoints as monfig
import macro.utils as mutils

class Price:
    def cpi(country):
        """
        Returns producer price index for a specific country.
        Guide to scraping Highcharts:
        https://levelup.gitconnected.com/trickycases-6-scrape-highcharts-plots-a6b3fc233fe6

        :Params:
        * country (str): country lookup (e.g. "united-states","spain","japan")
        
        :Return:
        * cpi_df (DataFrame): dataframe with price index, and rate of change, indexed by time
        """
        url = monfig.Endpoints.Price.cpi.format(country)
        cpi = mutils.Sel.dual_series_graph(url)
        return cpi

    def ppi(country):
        """
        Returns producer price index for a specific country.

        :Params:
        * country (str): country lookup (e.g. "united-states","spain","japan")
        
        :Return:
        * df (DataFrame): dataframe with price index, and rate of change, indexed by time
        """
        url = monfig.Endpoints.Price.ppi.format(country)
        ppi = mutils.Sel.dual_series_graph(url)
        return ppi