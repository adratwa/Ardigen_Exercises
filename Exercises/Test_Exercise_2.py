import unittest
from pandas.testing import assert_frame_equal
import pandas as pd
import os
import Exercise_2


class TestValuationService(unittest.TestCase):

    def setUp(self):
        # data that will be used for testing
        self.data = pd.DataFrame({
            'id': [1, 2, 3, 4, 5, 6, 7, 8, 9],
            'price': [1000, 1050, 2000, 1750, 1400, 7000, 630, 4000, 1400],
            'currency': ['GBP', 'EU', 'PLN', 'EU', 'EU', 'PLN', 'GBP', 'EU', 'GBP'],
            'quantity': [2, 1, 1, 2, 4, 3, 5, 1, 3],
            'matching_id': [3, 1, 1, 2, 3, 2, 3, 3, 1]
        })
        self.currencies = pd.DataFrame({
            'currency': ['GBP', 'EU', 'PLN'],
            'ratio': [2.4, 2.1, 1]
        })
        self.matchings = pd.DataFrame({
            'matching_id': [1, 2, 3],
            'top_priced_count': [2, 2, 3]
        })

    def test_load_data(self):
        # Test that load_data function returns the correct dataframes
        data, currencies, matchings = Exercise_2.load_data('data.csv', 'currencies.csv', 'matchings.csv')

        assert_frame_equal(data, self.data)
        assert_frame_equal(currencies, self.currencies)
        assert_frame_equal(matchings, self.matchings)

    def test_currency_convertor_to_pln(self):
        # test that currency_convertor_to_pln function returns correct values
        result = Exercise_2.currency_convertor_to_pln(self.data, self.currencies)

        # expected results after conversion
        expected_result = self.data.copy()
        expected_result['price'] = [2400.0, 2205.0, 2000.0, 3675.0, 2940.0, 7000.0, 1512.0, 8400.0, 3360.0]
        expected_result['currency'] = 'PLN'

        assert_frame_equal(result, expected_result)

    def test_get_top_priced(self):
        # test that get_top_priced function returns correct values
        result = Exercise_2.get_top_priced(self.data, self.currencies, self.matchings)

        # expected results for top priced products
        expected_result = pd.DataFrame({
            'matching_id': [1, 1, 2, 2, 3, 3, 3],
            'total_price': [10080.0, 2205.0, 21000.0, 7350.0, 11760.0, 8400.0, 7560.0],
            'avg_price': [6142.5, 6142.5, 14175.0, 14175.0, 9240.0, 9240.0, 9240.0],
            'currency': ['PLN', 'PLN', 'PLN', 'PLN', 'PLN', 'PLN', 'PLN'],
            'ignored_products_count': [1, 1, 0, 0, 1, 1, 1]
        })
        assert_frame_equal(result, expected_result)


if __name__ == '__main__':
    unittest.main()
