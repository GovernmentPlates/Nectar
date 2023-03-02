# N.E.C.T.A.R.
**N**ationwide **E**x**C**hange ra**T**e scr**A**pe**R**

A quick and dirty Python script to scrape [nationwide.co.uk's foreign exchange rates](https://www.nationwide.co.uk/help/payments/foreign-exchange-rates/) page

## Installation
Install the requirements using `pip install -r requirements.txt` (uses Selenium)

## Docs

|           Method |    Notes | Type |
| ---------------- | ---------- | ---- |
| `get_last_updated()` | Returns the DD/MM/YYYY timestamp of when the exchange rate data was last updated | `str` |
| `get_exchange_rate("currency")` | Returns the exchange rate for a specified `currency` (i.e. CHF, USD etc.) | `float` |
| `_get_exchange_rates()` | Returns a dictionary of currencies and exchange rates (`{'currency': 'exchange_rate'}`) | `dict` |

## Example
```python
>>> from main import ExchangeRateCalculator
>>> ExchangeRateCalculator().get_last_updated()
02/03/2023
>>> ExchangeRateCalculator().get_exchange_rate('CHF')
1.1012
```

## License
Licensed under GNU General Public License v3.0
