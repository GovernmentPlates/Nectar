"""
Nationwide Exchange Rate Scraper
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This script uses Selenium to scrape the exchange rates from the Nationwide website.
Rates shown are for GBP (£) to the currency specified.

Basic Usage:
    >>> from nectar import Nectar
    >>> Nectar().get_last_updated()
    '02/03/2023'
    >>> Nectar().get_exchange_rate('CHF')
    1.1012
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options


class Nectar:
    def __init__(self):
        self.chrome_options = Options()
        self.chrome_options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.base_url = 'https://www.nationwide.co.uk/help/payments/foreign-exchange-rates/'

    def get_last_updated(self) -> str:
        r"""
        Returns the last updated date of the exchange rates.

        :return str last_updated: The last updated date of the exchange rates in the format 'dd/mm/yyyy'
        """
        self.driver.get(self.base_url)
        wait = WebDriverWait(self.driver, 10)
        wait.until(ec.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/main/div/div['
                                                             '2]/div/div/div/div/div/div[2]/div/p[1]')))
        last_updated = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/main/div/div['
                                                          '2]/div/div/div/div/div/div[2]/div/p[1]').text
        return last_updated[16:]

    def _get_exchange_rates(self) -> dict:
        r"""
        Returns a dictionary of the exchange rates.

        :return dict exchange_rates: A dictionary of the exchange rates in the format {'currency': 'exchange_rate'}
        """
        self.driver.get(self.base_url)
        wait = WebDriverWait(self.driver, 10)
        wait.until(ec.presence_of_element_located((By.XPATH, '//*[@id="main"]/div[2]/div/div/div/div/div/div['
                                                             '2]/div/div/table')))
        exchange_table = self.driver.find_element(By.XPATH, '//*[@id="main"]/div[2]/div/div/div/div/div/div['
                                                            '2]/div/div/table')

        exchange_rates = {}
        for row in exchange_table.find_elements(By.TAG_NAME, 'tr'):
            if row.find_elements(By.TAG_NAME, 'td'):
                exchange_rates[row.find_element(By.TAG_NAME, 'td').text] = row.find_elements(By.TAG_NAME, 'td')[2].text
        return exchange_rates

    def get_exchange_rate(self, currency: str) -> float:
        r"""
        Returns the exchange rate for the given currency.

        :param str currency: The currency to get the exchange rate for (i.e. 'CHF')
        :return float exchange_rate: The exchange rate for the given currency
        """
        return float(self._get_exchange_rates()[currency])
