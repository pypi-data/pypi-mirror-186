import pandas as pd
import re

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import TimeoutException

class Sel:
    def dual_series_graph(url, units = False):
        """
        Pulls information from a Highcharts graph from economy.com. The graph must contain
        two series (typically values, and rate of change).

        Note: parameter units (bool) is used to save an extra selenium operation if the
        graph needs to be adjusted for unit scales (e.g. displayed values are in Mil's).
        However, units can still be pulled separately as a function under this class (Sel).
        
        :Params:
        * url (str): url looked up by selenium
        * units (bool): True for unit-adjustment, False for no adjustment.
                        
        :Returns:
        * df (DataFrame): contains up to last 12 available data points, indexed by date 
                          (graph x values)
        """
        options = webdriver.ChromeOptions()
        options.add_argument("--ignore-certificate-errors")     # Ignores SSL
        options.add_argument("--incognito")                     # Incognito
        options.add_argument("--headless")                      # No pop-up

        driver = webdriver.Chrome(ChromeDriverManager().install(), options = options)
        driver.get(url)

        # Wait until table renders (no retry mechanic needed as of right now)
        try:
            WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.CLASS_NAME, "ng-scope"))
            )
            located = True
        except TimeoutException:
            pass

        # Basically doing a nested dictionary lookup until data is found, and then list created through "map"
        dates = driver.execute_script("return Highcharts.charts[0].series[0].data.map(x => x.category)")
        index_values = driver.execute_script("return Highcharts.charts[0].series[1].data.map(x => x.y)")
        rate_of_change = driver.execute_script("return Highcharts.charts[0].series[0].data.map(x => x.y)")

        # Saves an extra operation by converting values by their units if param is True
        if units == True:
            print("Looking for element!")
            elem = driver.find_element(By.XPATH, "//*[@id='Page']/div[2]/div/div[1]/div[4]/div[1]/div/table/tbody/tr[3]/td").text
        
            # Using list comprehension to speed up multiplying every element in list
            if "Ths" in elem:
                index_values = [element * 10**3 for element in index_values]
            elif "Ten" in elem:
                index_values = [element * 10**4 for element in index_values]
            elif "Mil" in elem:
                index_values = [element * 10**6 for element in index_values]
            elif "Bil" in elem:
                index_values = [element * 10**9 for element in index_values]
            # Else in base currency (units of 1)
            else:
                pass

        driver.quit()

        # Set data for df conversion
        data = {
            "Values":index_values,
            "% Change":rate_of_change
        }

        df = pd.DataFrame(data, index=dates)
        return df

    def single_series_graph(url):
        pass

    def units(url):
        options = webdriver.ChromeOptions()
        options.add_argument("--ignore-certificate-errors")     # Ignores SSL
        options.add_argument("--incognito")                     # Incognito
        options.add_argument("--headless")                      # No pop-up

        driver = webdriver.Chrome(ChromeDriverManager().install(), options = options)
        driver.get(url)

        try:
            WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.CLASS_NAME, "col-md-6"))
            )
        except TimeoutException:
            pass

        elem = driver.find_element(By.XPATH, "//*[@id='Page']/div[2]/div/div[1]/div[4]/div[1]/div/table/tbody/tr[3]/td").text
        
        if "Ths" in elem:
            return 10**3
        elif "Ten" in elem:
            return 10**4
        elif "Mil" in elem:
            return 10**6
        elif "Bil" in elem:
            return 10**9
        # Else in base currency (units of 1)
        else:
            return 1

class Input:
    def parse_country(country):
        """
        Implement! Cleans up country input into macro functions
        """
        pass

class Country:
    def list_countries():
        countries = []
        f = open('../countries.txt', 'r').readlines()
        for country in f:
            a = country.strip()
            a = a.replace(" ","-")
            a = a.replace("/","-per-")
            a = re.sub(r"[(){}'.]", "", a)
            a = a.lower()
            countries.append(a)
        return countries