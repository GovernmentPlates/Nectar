import unittest
from unittest.mock import MagicMock, patch
from nectar import Nectar


class TestNectar(unittest.TestCase):

    @patch('main.webdriver.Chrome')
    def setUp(self, mock_webdriver):
        self.calculator = Nectar()

    def test_get_last_updated(self):
        mock_element = MagicMock()
        mock_element.text = 'Last updated on 02/03/2023'
        self.calculator.driver.find_element.return_value = mock_element

        last_updated = self.calculator.get_last_updated()

        self.assertEqual(last_updated, '02/03/2023')

    def test_get_exchange_rate(self):
        mock_exchange_rates = {'CHF': '1.1012', 'USD': '1.1696'}
        self.calculator._get_exchange_rates = MagicMock(return_value=mock_exchange_rates)

        exchange_rate = self.calculator.get_exchange_rate('CHF')

        self.assertEqual(exchange_rate, 1.1012)
