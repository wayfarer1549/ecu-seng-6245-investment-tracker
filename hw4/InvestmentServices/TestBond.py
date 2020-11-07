import unittest

class TestBond(unittest.TestCase):

	def setUp(self):
		date = "2020-11-01"
		bond_id = "UST10YR"
		name = "U.S. Treasury 10 Yr. Note"
		price = 1500.0
		bond_type = "U.S. Treasury Note"
		maturity = "2030"
		payment_count = 20
		bond_yield = 2.25

		self.new_bond = Bond(
			date,
			name,
			bond_id,
			price,
			bond_yield,
			bond_type,
			maturity,
			payment_count)

	def tearDown(self):
		self.new_bond.dispose()

	def test_bond_constructor(self):
		price = 1500.0
		payment_count = 20

		self.assertEqual(
			self.new_bond.price,
			price)
		self.assertEqual(
			self.new_bond.number_of_payments,
			payment_count)

	def test_get_yield(self):
		#bond_type = "U.S. Treasury Note"
		self.assertEqual(
			self.new_bond.get_yield(),
			bond_yield = 2.25)


	def test_get_bond_type(self):
		bond_type = "U.S. Treasury Note"
		self.assertEqual(
			self.new_bond.get_bond_type(),
			bond_type)

	def test_get_maturity(self):
		maturity = "2030"
		self.assertEqual(
			self.new_bond.test_get_maturity(),
			maturity)

	def test_str(self):
		bond_id = "UST10YR"

		self.assertEqual(
			str(self.new_bond),
			bond_id)







