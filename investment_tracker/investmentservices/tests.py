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
		test_acct = Account.objects.get(id=1)
		number = 'OWEN2020'
		inv_balance = 0.00
		cash_balance = 1250.00

		self.assertEqual(test_acct.account_number, number)
		self.assertEqual(test_acct.investment_balance, inv_balance)
		self.assertEqual(test_acct.cash_balance, cash_balance)
		self.assertTrue(test_acct.active)

	def test_account_balance(self):
		test_acct = Account.objects.get(account_number__exact='OWEN2020')
		expected_balance = 1250.00

		self.assertEqual(test_acct.get_account_balance, expected_balance)

	def test_cash_balance(self):
		test_acct = Account.objects.get(account_number__exact='OWEN2020')
		expected_balance = 1250.00

		self.assertEqual(test_acct.get_cash_balance, expected_balance)

	def test_investment_balance(self):
		test_acct = Account.objects.get(account_number__exact='OWEN2020')
		expected_balance = 0.00

		self.assertEqual(test_acct.get_investment_balance, expected_balance)

	def test_acct_number(self):
		test_acct = Account.objects.get(id=1)
		self.assertEqual(test_acct.get_acct_number, 'OWEN2020')


class SharedInvestmentTest(TestCase):
	pass

class BondTest(TestCase):
	pass

class TransactionTests(TestCase):
	pass

