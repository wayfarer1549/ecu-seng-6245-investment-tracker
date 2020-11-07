import unittest
import Investment

class TestInvestments(unittest.TestCase):

	def setUp(self):
		date = "2020-10-03"
		inv_name = "Test Investment"
		self.new_investment = Investment(date, inv_name)

	def tearDown(self):
		self.new_investment.dispose()

	def test_base_investment_constructor(self):
		date = "2020-10-03"inv_name = "Test Investment"

		self.assertEqual(
			self.new_investment.date, date)
		
	def test_get_name(self):
		name = "Test Investment"

		self.assertEqual(
			self.new_investment.get_name(),
			name)
