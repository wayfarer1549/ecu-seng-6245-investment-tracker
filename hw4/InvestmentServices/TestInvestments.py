import unittest
from Investment import Investment

class TestInvestments(unittest.TestCase):

	def setUp(self):
		date = "2020-10-03"
		inv_name = "Test Investment"
		self.new_investment = Investment(date, inv_name)


	def test_base_investment_constructor(self):
		date = "2020-10-03"
		inv_name = "Test Investment"

		self.assertEqual(
			self.new_investment.purchase_date, date)
		
	def test_get_name(self):
		name = "Test Investment"

		self.assertEqual(
			self.new_investment.get_name(),
			name)
if __name__ == '__main__':
    unittest.main()