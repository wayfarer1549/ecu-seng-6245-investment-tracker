import unittest
import Account

class TestAccount(unittest.TestCase):

	def setUp(self):
		acct_number = 'BUNY1689'
		advisor_id = 'LUTH1517'
		self.new_account = Account(
			acct_number,
			advisor_id)

	def tearDown(self):
		self.new_account.dispose()

	def test_account_constructor(self):
		acct_number = 'BUNY1689'
		advisor_id = 'LUTH1517'

		self.assertEqual(
			self.new_account.acct_number,
			acct_number)
		self.assertEqual(
			self.new_account.advisor_id,
			advisor_id)

	def test_change_advisor_valid_input(self):
		old_advisor = 'LUTH1517'
		new_advisor = 'CRAN1549'

		self.new_account.change_advisor(new_advisor)
		self.assertNotEqual(
			self.new_account.advisor_id,
			old_advisor)
		self.assertEqual(
			self.new_account.advisor_id,
			new_advisor)

	def test_change_advisor_invalid_inputs(self):
		new_advisor = '100'

		with self.assertRaises(TypeError):
			self.new_account.change_advisor(new_advisor)
		new_advisor = 'CRANMER'
		with self.assertRaises(ValueError):
			self.new_account.change_advisor(new_advisor)
		

	def test_deposit_cash_valid_input(self):
		deposit_amt = 500.0
		self.new_account.deposit_cash(deposit_amt)

		self.assertEqual(
			self.new_account.cash_balance,
			deposit_amt)

	def test_deposit_cash_invalid_inputs(self):
		deposit_amt = 500
		with self.assertRaises(TypeError):
			self.new_account.deposit_cash(deposit_amt)
		deposit_amt = -100.0
		with self.assertRaises(ValueError):
			self.new_account.deposit_cash(deposit_amt)

	def test_withdraw_cash_valid_input(self):
		withdrawal_amt = 250.0
		self.new_account.withdraw_cash(withdrawal_amt)

		self.assertEqual(
			self.new_account.cash_balance,
			withdrawal_amt)

	def test_withdraw_cash_invalid_inputs(self):
		withdrawal_amt = 250
		with self.assertRaises(TypeError):
			self.new_account.withdraw_cash(withdrawal_amt)
		withdrawal_amt = -100.0
		with self.assertRaises(ValueError):
			self.new_account.withdraw_cash(withdrawal_amt)


	def test_current_cash(self):
		deposit_amt = 500.0
		self.new_account.deposit_cash(deposit_amt)

		self.assertEqual(
			self.new_account.current_cash(),
			deposit_amt)

	def test_portfolio_value(self):
		investment_value = 7500.0

		self.new_account.account_balance = investment_value

		self.assertEqual(
			self.new_account.portfolio_value(),
			investment_value)

	def test_account_balance(self):
		investment_value = 7500.0
		cash_balance = 1500.0

		self.new_account.deposit_cash(cash_balance)
		self.new_account.account_balance = investment_value

		self.assertEqual(
			self.new_account.get_account_balance(),
			investment_value + cash_balance)



