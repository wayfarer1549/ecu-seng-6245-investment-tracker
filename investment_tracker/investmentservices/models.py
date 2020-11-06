from django.db import models

# Create your models here.
class Account(models.Model):
	'''Overview: Represents a customer's account with the financial brokerage.'''

	# Attributes
	account_number = models.CharField(max_length=20)
	#account_owner = models.ForeignKey()
	advisor = models.CharField(max_length=200)
	investment_balance = models.DecimalField(max_digits=22, decimal_places=2)
	cash_balance = models.DecimalField(max_digits=22, decimal_places=2)

	def get_absolute_url(self):
		return reverse('account-detail', kwargs={'pk': self.pk})

	def get_account_balance(self):
		return self.investment_balance + self.cash_balance

	def get_cash_balance(self):
		return self.cash_balance

	def get_investment_balance(self):
		return self.cash_balance

class Investment(models.Model):
	'''Overview Represents an investment in a customer's portfolio'''

	# Attributes
	purchase_date = models.DateField('date purchased')
	name = models.CharField(max_length=200)

	class Meta:
		abstract = True

class Bond(Investment):
	'''Overview: Represents a government or corporate bond investment in a customer's portfolio'''

	# Attributes
	bond_yield = models.FloatField() # the interest rate of the bond
	bond_type = models.CharField(max_length=200)
	maturity_date = models.DateField('maturity date of the bond')
	number_of_payments = models.IntegerField() # how many payments of interest this bond pays per year

class SharedInvestment(Investment):
	'''Overview: A shared investment is a stock, mutual fund, or Exchange Traded Fund (ETF) comprised
	of a number of shares.'''

	SHARED_INVESTMENT_CHOICES = [
		('STK', 'Stock'),
		('MUF', 'Mutual Fund'),
		('ETF', 'Exchange Traded Fund')

	]

	# Attributes
	ticker_symbol = models.CharField(max_length=6) # investment's ticker symbol
	number_of_shares = models.IntegerField() # possible to have fractional shares
	purchase_price = models.DecimalField(max_digits=12, decimal_places=2) # price per share when purchased
	current_price = models.DecimalField(max_digits=12, decimal_places=2) # current price per share
	investment_type = models.CharField(
		max_length=3,
		choices=SHARED_INVESTMENT_CHOICES,
		)

	def update_share_count(this, share_count):
		'''updates this model with a new share count'''
		if sharecount > 0:
			self.number_of_shares += sharecount
		else:
			self.number_of_shares -= sharecount

		self.save()

	def update_current_price(this, new_price):
		'''updates the current share price of the investment'''
		self.current_price = new_price
		self.save()



class InvestmentList(models.Model):
	'''Overview: An investment list contains a queue of all investments owned by a customer (i.e. their portfolio)
	'''
	account = models.ForeignKey('Account',
		on_delete=models.CASCADE)
	portfolio = models.ManyToManyField('SharedInvestment',)


class Transaction(models.Model):
	'''Overview: Represents an investment transaction'''
	# Attributes
	purchase_date = models.DateField('date purchased')



