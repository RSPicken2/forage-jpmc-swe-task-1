import unittest
from client3 import *

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    for q in quotes:
        assert getDataPoint(q) == (q["stock"], q['top_bid']['price'], q['top_ask']['price'], (q['top_bid']['price'] + q['top_ask']['price'])/2)


  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    for q in quotes:
        assert getDataPoint(q) == (q["stock"], q['top_bid']['price'], q['top_ask']['price'], (q['top_bid']['price'] + q['top_ask']['price'])/2)


  def test_getRatio(self):
      assert getRatio(12.0, 6.0) == 2.0


  def test_getRatioFloat(self):
      assert getRatio(5, 2) == 2.5


  def test_getRatioZeroDivision(self):
      assert getRatio(12.0, 0) == None

if __name__ == '__main__':
    unittest.main()
