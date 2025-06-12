import unittest
from src import ticker

class TestTicker(unittest.TestCase):
    def setUp(self):
        self.companies = [
            {'id': '1', 'name': 'Company A', 'ticker': 'CMPA'},
            {'id': '2', 'name': 'Company B', 'ticker': 'CMPB'},
        ]

    def test_update_exists(self):
        updated = ticker.update_ticker(self.companies, '1', 'NEW1')
        self.assertTrue(updated)
        self.assertEqual(self.companies[0]['ticker'], 'NEW1')

    def test_update_missing(self):
        updated = ticker.update_ticker(self.companies, '3', 'NEW3')
        self.assertFalse(updated)

if __name__ == '__main__':
    unittest.main()
