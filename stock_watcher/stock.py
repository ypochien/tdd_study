# coding=UTF-8
# __author__ == ypochien

import unittest


class Stock(object):
    def __init__(self, symbol):
        self.symbol = symbol
        self.price = None


class StockTest(unittest.TestCase):
    def test_price_of_a_new_stock_class_should_be_None(self):
        stock = Stock("GOOG")
        self.assertIsNone(stock.price)


if __name__ == "__main__":
    unittest.main()
