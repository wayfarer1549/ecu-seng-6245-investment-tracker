from Investment import Investment
class Investment_List():
	# Overview: An investment list contains a list of all investments owned by a customer
	# I.E. it represents a customer's portfolio

	# Attributes

	def __init__(self, account_number):
		self.portfolio = []
		self.account_number = account_number

	# Methods

	def get_investments(self):
		# Effects: returns the customer's porfolio as a list data structure
		# The resulting list should contain Investment objects
		return self.portfolio

	def purchase_investment(self, investment):
		# Effects: adds the investment parameter to the customer's
		# portfolio.
		# Parameter should accept an investment object
		if not isinstance(investment, Investment):
			raise TypeError('Parameter must be an Investment object')
		else:
			self.portfolio.append(investment)

	def sell_investment(self, investment):
		# Effects: removes the investment parameter to the customer's
		# portfolio.
		# Parameter should accept a valid investment object
		if not isinstance(investment, Investment):
			raise TypeError('Parameter must be an Investment object')
		else:
			self.portfolio.remove(investment)

	def get_investment_details(self, symbol):
		# Effects returns the investment details for the investment specified
		# by symbol.
		# Symbol should be a string of minimum length 1 and maximum length 4
		# containing only alphabetic characters.
		if not isinstance(symbol, str):
			raise TypeError('Parameter must be a string')
		elif len(symbol) < 1:
			raise ValueError('Parameter length should be greater than 0')
		elif len(symbol) > 4:
			raise ValueError('Parameter length should be less than 5')
		else:
			for i in self.portfolio:
				if str(i) == symbol:
					return str(i)
