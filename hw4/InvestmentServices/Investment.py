

class Investment():

	# Overview: Abstract class representing an investment in a customer's portfolio

	# Attributes
	def __init__(self, date, name):
		self.purchase_date = date
		self.name = name

	# Methods
	def get_name(self):
		# Effects: returns the name of this investment
		return self.name


class Bond(Investment):
	# Overview: Represents a government or corporate investment in a customer's portfolio

	def __init__(self, date, name, bond_id, price, bond_yield, bond_type, maturity_date, payment_count):
		super().__init__(date, name)
		self.bond_id = bond_id
		self.purchase_price = price
		self.bond_yield = bond_yield
		self.bond_type = bond_type
		self.maturity_date = maturity_date
		self.number_of_payments = payment_count

	# Methods
	def get_yield(self):
		return self.bond_type

	def get_bond_type(self):
		return self.bond_type

	def get_maturity(self):
		return self.maturity_date

	def __str__(self):
		return str(self.bond_id)

class SharedInvestment(Investment):
	# Overview: A shared investment is a stock, mutual fund, or exchange traded fund (ETF) that is cmprised of a number of shares

	# Attributes
	def __init__(self, date, name, ticker_symbol, initial_shares, price, investment_type):
		super().__init__(date, name)
		self.ticker_sybmol = ticker_sybmol
		self.number_of_shares = initial_shares
		self.purchase_price = price
		self.current_price = price
		self.investment_type = investment_type

	# Methods

	def update_share_price(self, new_price):
		# Effects: updates the current price of this investment based on the market price
		if new_price is not float:
			raise TypeError('Parameter must be an float')
		elif amount < 0:
			raise ValueError('Parameter should be greater than or equal to 0')
		else:
			self.current_price = new_price

	def update_shares(self, share_count):
		# Effects: increases the number of shares purchased (positive integer)
		# or decreases the number of shares purchased (negative integer)

		if share_count is not int:
			raise TypeError('Parameter must be an integer')
		elif amount < 0:
			raise ValueError('Parameter should be greater than or equal to 0')
		else:
			if share_count > 0:
				self.number_of_shares += share_count
			else:
				self.number_of_shares -= share_count

	def __str__(self):
		return str(self.ticker_symbol)
