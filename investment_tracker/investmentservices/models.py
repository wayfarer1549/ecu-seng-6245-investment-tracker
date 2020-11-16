from decimal import Decimal
from django.db import models
from users.models import FinancialUser

# Create your models here.
class Account(models.Model):
	'''Overview: Represents a customer's account with the financial brokerage.'''

	# Attributes
	account_number = models.CharField(max_length=20, blank=False, null=False)
	account_owner = models.OneToOneField(FinancialUser, null=True, on_delete=models.CASCADE, related_name='account_owner_set')
	#advisor = models.CharField(max_length=200)
	advisor = models.ForeignKey(FinancialUser, null=True, on_delete=models.CASCADE, related_name='account_advisor_set')
	investment_balance = models.DecimalField(max_digits=22, decimal_places=2)
	cash_balance = models.DecimalField(max_digits=22, decimal_places=2)
	active = models.BooleanField(default=True)

	def get_absolute_url(self):
		return reverse('account-detail', kwargs={'pk': self.pk})

	@property
	def get_account_balance(self):
		return self.investment_balance + self.cash_balance

	@property 
	def get_cash_balance(self):
		return self.cash_balance

	@property 
	def get_investment_balance(self):
		return self.investment_balance

	def __str__(self):
		return self.account_number

	@property
	def get_acct_number(self):
		return self.account_number

	def deposit(self, amount):

		if amount > 0:
			self.cash_balance += Decimal(amount)
			self.save()

			new_transaction = CashTransaction.objects.create(
				transaction_type='DEP',
				transaction_date='2020-11-01', #TODO: Current Date
				transaction_amount=Decimal(amount) )
		

	def withdraw(self, amount):
		if amount > 0:
			self.cash_balance -= amount
			self.save()

			new_transaction = CashTransaction.objects.create(
				transaction_type='WDL',
				transaction_date='2020-11-01', #TODO: Current Date
				transaction_amount=Decimal(amount) )

class Investment(models.Model):
	'''Overview Represents an investment in a customer's portfolio'''

	# Attributes
	#account = models.CharField(max_length=20, blank=True, null=True)
	account = models.OneToOneField(Account, on_delete=models.CASCADE, blank=True, null=True)
	purchase_date = models.DateField('date purchased')
	name = models.CharField(max_length=200, blank=False, null=False)

	class Meta:
		abstract = True

class Bond(Investment):
	'''Overview: Represents a government or corporate bond investment in a customer's portfolio'''

	BOND_TYPE_CHOICES = [

		('USTB', 'U.S. Treasury Bill'),
		('USTN', 'U.S. Treasury Note'),
		('USTBD', 'U.S. Treasury Bond'),
		('CORP', 'Corporate Bond'),
		('MUNC', 'Municipal Bond'),
		('INTL', 'International Bond'),

	]

	# Attributes
	bond_yield = models.FloatField(blank=False) # the interest rate of the bond
	bond_type = models.CharField(max_length=5, choices=BOND_TYPE_CHOICES)
	maturity_date = models.DateField('maturity date of the bond')
	number_of_payments = models.IntegerField(blank=False) # how many payments of interest this bond pays per year
	purchase_price = models.DecimalField(max_digits=12, decimal_places=2, blank=False) # price of the bond when purchased

	@property
	def get_yield(self):
		return self.bond_yield

	@property
	def get_type(self):
		return self.bond_type

	@property
	def get_maturity(self):
		return str(self.maturity_date)

	@property
	def get_yearly_payment_count(self):
		return self.number_of_payments

	@property
	def calculate_remaining_payments(self):
		#TODO: Return the number of remaining payments
		# Calculate time delta and * by number of payments per year
		pass

	def __str__(self):
		return self.bond_type + ' ' + str(self.get_yield) + ' ' + str(self.purchase_date)
	

class SharedInvestment(Investment):
	'''Overview: A shared investment is a stock, mutual fund, or Exchange Traded Fund (ETF) comprised
	of a number of shares.'''

	SHARED_INVESTMENT_CHOICES = [
		('STK', 'Stock'),
		('MUF', 'Mutual Fund'),
		('ETF', 'Exchange Traded Fund'),

	]

	# Attributes
	ticker_symbol = models.CharField(max_length=6, blank=False, null=False) # investment's ticker symbol
	number_of_shares = models.IntegerField(blank=False, default=0) # possible to have fractional shares?
	purchase_price = models.DecimalField(max_digits=12, decimal_places=2, blank=False) # price per share when purchased
	current_price = models.DecimalField(max_digits=12, decimal_places=2, blank=False) # current price per share
	investment_type = models.CharField(
		max_length=3,
		choices=SHARED_INVESTMENT_CHOICES,
		)

	def update_share_count(self, share_count, purchase_price):
		'''updates this model with a new share count'''
		self.number_of_shares += share_count
		self.save()

		if share_count > 0:

			new_transaction = SharedTransaction.objects.create(
				investment=self,
				share_count=share_count,
				transaction_type='BUY',
				transaction_date='2020-11-01', #TODO: Current Date
				transaction_amount=Decimal(share_count)*Decimal(purchase_price) )
		else:
			new_transaction = SharedTransaction.objects.create(
				investment=self,
				share_count=abs(share_count),
				transaction_type='SELL',
				transaction_date='2020-11-01',
				transaction_amount=abs(Decimal(share_count))*Decimal(purchase_price))

	def update_current_price(self, new_price):
		'''updates the current share price of the investment'''
		self.current_price = Decimal(new_price)
		self.save()

	@property 
	def investment_value(self):
		return self.number_of_shares * self.current_price

	def __str__(self):
		return self.ticker_symbol



class InvestmentList(models.Model):
	'''Overview: An investment list contains a queue of all investments owned by a customer (i.e. their portfolio)
	'''
	account = models.ForeignKey('Account',
		on_delete=models.CASCADE)
	portfolio = models.ManyToManyField('SharedInvestment',)


class Transaction(models.Model):
	'''Overview: Represents an investment transaction'''
	# Attributes

	TRANSACTION_TYPES = [
		('BUY', 'Purchased'),
		('SELL', 'Sold'),
		
	]

	#account = models.ForeignKey(Account, on_delete=models.CASCADE, blank=False) #models.CharField(max_length=20)
	transaction_date = models.DateField(blank=False)
	transaction_amount = models.DecimalField(max_digits=22, decimal_places=2)
	transaction_type = models.CharField(max_length=4, choices=TRANSACTION_TYPES)

	class Meta:
		abstract = True

	def __str__(self):
		return self.transaction_date + account.get_acct_number()

class BondTransaction(Transaction):
	'''Represents a transaction involving a bond investment'''
	investment = models.ForeignKey(Bond, on_delete=models.CASCADE)

class SharedTransaction(Transaction):
	'''Represents a transaction involving a shared investment'''
	investment = models.ForeignKey(SharedInvestment, on_delete=models.CASCADE)
	share_count = models.IntegerField(blank=False)

class CashTransaction(Transaction):
	'''Represents a cash transaction'''
	TRANSACTION_TYPES = [
		('DEP', 'Deposit'),
		('WDL', 'Withdrawal'),
	]




