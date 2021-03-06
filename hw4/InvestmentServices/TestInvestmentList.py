import unittest
from Investment import Investment, SharedInvestment
from Investment_List import Investment_List

class TestInvestmentList(unittest.TestCase):

	def setUp(self):
		acct_number = 'CRAN1549'
		self.new_inv_list = Investment_List(acct_number)

	def test_investment_list_constructor(self):
		acct_number = 'CRAN1549'

		self.assertEqual(
			self.new_inv_list.account_number,
			acct_number)
		self.assertEqual(
			len(self.new_inv_list.portfolio),
			0 )

	def test_purchase_investment(self):

		inv1 = SharedInvestment(
			'2020-08-31',
			'Apple Class C Shares',
			'AAPL',
			50,
			109.0,
			'Stock')

		inv2 = SharedInvestment(
			'2020-09-15',
			'Toyota Class A Shares',
			'TYTA',
			25,
			225.0,
			'Stock')

		inv3 = SharedInvestment(
			'2020-10-02',
			'International Paper',
			'ITP',
			45,
			27.25,
			'Stock')

		invs = [inv1, inv2, inv3]

		for inv in invs:
			self.new_inv_list.purchase_investment(inv)

		for inv in invs:
			self.assertIn(
				inv, self.new_inv_list.get_investments())

	def test_purchase_investment_invalid_input(self):
		with self.assertRaises(TypeError):
			inv = 'AAPL'
			self.new_inv_list.purchase_investment(inv)

	def test_sell_investments(self):
		inv1 = SharedInvestment(
			'2020-08-31',
			'Apple Class C Shares',
			'AAPL',
			50,
			109.0,
			'Stock')

		inv2 = SharedInvestment(
			'2020-09-15',
			'Toyota Class A Shares',
			'TYTA',
			25,
			225.0,
			'Stock')

		invs = [inv1, inv2]

		for inv in invs:
			self.new_inv_list.purchase_investment(inv)

		self.new_inv_list.sell_investment(inv2)

		self.assertNotIn(inv2, self.new_inv_list.get_investments())
		self.assertIn(inv1, self.new_inv_list.get_investments())

	def test_sell_investments_invalid_input(self):
		with self.assertRaises(TypeError):
			inv = 'AAPL'
			self.new_inv_list.sell_investment(inv)

	def test_get_investments(self):
		inv1 = SharedInvestment(
			'2020-08-31',
			'Apple Class C Shares',
			'AAPL',
			50,
			109.0,
			'Stock')

		inv2 = SharedInvestment(
			'2020-09-15',
			'Toyota Class A Shares',
			'TYTA',
			25,
			225.0,
			'Stock')

		invs = [inv1, inv2]

		for inv in invs:
			self.new_inv_list.purchase_investment(inv)

		self.assertEqual(len(self.new_inv_list.get_investments()), 2)

	def test_investment_details(self):
		symbol = 'AAPL'

		inv1 = SharedInvestment(
			'2020-08-31',
			'Apple Class C Shares',
			'AAPL',
			50,
			109.0,
			'Stock')

		self.new_inv_list.get_investment_details(symbol)

	def test_investment_details_invalid_inputs(self):
		with self.assertRaises(TypeError):
			symbol = 1001
			self.new_inv_list.get_investment_details(symbol)
		with self.assertRaises(ValueError):
			symbol = 'AAAPL'
			self.new_inv_list.get_investment_details(symbol)
		with self.assertRaises(ValueError):
			symbol = ''
			self.new_inv_list.get_investment_details(symbol)
if __name__ == '__main__':
    unittest.main()
