from django.test import TestCase
from .models import Account, SharedInvestment, Bond

# Create your tests here.
class AccountModelTest(TestCase):

	def setUp(self):
		test_acct = Account.objects.create(
			account_number='OWEN2020',
			investment_balance=0.00,
			cash_balance=1250.00,)

	def test_create_account(self):
		number = 'OWEN2020'
		inv_balance = 0.00
		cash_balance = 1250.00

		self.assertEqual(test_acct.account_number, number)
		self.assertEqual(test_acct.investment_balance, inv_balance)
		self.assertEqual(test_acct.cash_balance, cash_balance)
		self.assertTrue(test_acct.active)

	def test_account_balance(self):
		pass

	def test_cash_balance(self):
		pass

	def test_investment_balance(self):
		pass

	def test_acct_number(self):
		pass


class SharedInvestmentTest(TestCase):
	pass

class BondTest(TestCase):
	pass

class TransactionTests(TestCase):
	pass

