import unittest
import SharedInvestment

class TestSharedInvestment(unittest.TestCase):

	def setUp(self):
		symbol = 'AAPL'
		date = '2020-08-31'
		name = 'Apple Class C Shares'
		share_count = 50
		purchase_price = 109.0
		current_price = 109.0
		inv_type = 'Stock'

		self.new_stock = SharedInvestment(
			date,
			name,
			symbol,
			share_count,
			purchase_price,
			inv_type)

	def tearDown(self):
		self.new_stock.dispose()

	def test_shared_investment_constructor(self):
		symbol = 'AAPL'
		date = '2020-08-31'
		name = 'Apple Class C Shares'
		share_count = 50
		purchase_price = 109.0
		current_price = 109.0
		inv_type = 'Stock'

		self.assertEqual(
			self.new_stock.share_count,
			share_count)
		self.assertEqual(
			self.new_stock.purchase_price,
			purchase_price)
		self.assertEqual(
			self.new_stock.current_price,
			current_price)
		self.assertEqual(
			self.new_stock.investment_type,
			inv_type)

	def test_update_share_price(self):
		new_price = 115.0
		self.new_stock.update_share_price(new_price)

		self.assertEqual(
			self.new_stock.current_price,
			new_price)

	def test_update_share_price_invalid_inputs(self):
		with self.assertRaises(TypeError):
			new_price = 115
			self.new_stock.update_share_price(new_price)
		with self.assertRaises(ValueError):
			new_price = -120.50
			self.new_stock.update_share_price(new_price)
		with self.assertRaises(ValueError):
			new_price = -120.50
			self.new_stock.update_share_price(new_price)

	def test_update_shares(self):
		old_shares = 50
		new_shares = 73
		self.new_stock.update_shares(new_shares)

		self.assertEqual(
			self.new_stock.number_of_shares,
			old_shares + new_shares)

	def test_update_shares_invalid_inputs(self):
		with self.assertRaises(TypeError):
			new_shares = 73.0
			self.new_stock.update_shares(new_shares)

	def test_str(self):
		symbol = 'AAPL'
		self.assertEqual(
			str(self.new_stock), symbol)