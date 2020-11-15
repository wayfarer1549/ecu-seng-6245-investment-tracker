from decimal import Decimal
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
	
	def setUp(self):
		SharedInvestment.objects.create(
			ticker_symbol='AAPL',
			purchase_date = '2020-11-15',
			name='Apple',
			purchase_price=Decimal('119.26'),
			current_price=Decimal('119.26'),
			investment_type='STK',)

		SharedInvestment.objects.create(
			ticker_symbol='QQQ',
			name='QQQ Nasdaq Index',
			purchase_date = '2020-11-15',
			purchase_price=290.93,
			current_price=290.93,
			investment_type='ETF',)

		SharedInvestment.objects.create(
			ticker_symbol='NPFCX',
			name='American Funds New Perspective Funds',
			purchase_date = '2020-11-15',
			purchase_price=54.33,
			current_price=54.33,
			investment_type='MUF',)

	def test_create_stock(self):
		stock = SharedInvestment.objects.get(id=1)

		self.assertEqual(stock.ticker_symbol, 'AAPL')
		self.assertEqual(stock.name, 'Apple')
		self.assertEqual(stock.purchase_price, Decimal('119.26'))
		self.assertEqual(stock.current_price, Decimal('119.26'))
		self.assertEqual(stock.investment_type, 'STK')

	def test_create_ETF(self):
		etf = SharedInvestment.objects.get(id=2)
		self.assertEqual(etf.ticker_symbol, 'QQQ')
		self.assertEqual(etf.name, 'QQQ Nasdaq Index')
		self.assertEqual(etf.purchase_price, Decimal('290.93'))
		self.assertEqual(etf.current_price, Decimal('290.93'))
		self.assertEqual(etf.investment_type, 'ETF')


	def test_create_mutual_fund(self):
		mfund = SharedInvestment.objects.get(id=3)
		self.assertEqual(mfund.ticker_symbol, 'NPFCX')
		self.assertEqual(mfund.name, 'American Funds New Perspective Funds')
		self.assertEqual(mfund.purchase_price, Decimal('54.33'))
		self.assertEqual(mfund.current_price, Decimal('54.33'))
		self.assertEqual(mfund.investment_type, 'MUF')
		pass



class BondTest(TestCase):
	
	def setUp(self):
		pass

	def test_create_treasury_bill(self):
		pass

	def test_create_treasury_note(self):
		pass

	def test_create_treasury_bond(self):
		pass

	def test_create_corporate_bond(self):
		pass

	def test_create_municipal_bond(self):
		pass

	def test_create_international_bond(self):
		pass

class TransactionTests(TestCase):
	pass

