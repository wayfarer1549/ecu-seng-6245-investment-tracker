class Account():
	# Overview: Represents a customer's account with the financial brokerage

	# Attributes
	def __init__(
		self,
		account_number,
		advisor_id,):

		self.account_number = account_number
		self.advisor_id = advisor_id
		self.account_balance = 0.0
		self.cash_balance = 0.0

	# Methods
	def get_account_balance(self):
		# Returns the portfolio balance (i.e the sum of cash and investment value)
		# Output domain: should return a floating point value
		# >= 0. Should not have negative balance.
		return self.cash_balance + self.account_balance

	def current_cash(self):
		# Effects: Returns the cash balance in the customer's account
		# Should return a cash balance >= 0; should not have negative cash balance.
		return self.cash_balance

	def portfolio_value(self):
		# Effects: Returns the value of all investments in the customer's account
		# Effects: Returns the cash balance in the customer's account
		# Should return a portfolio balance >= 0; should not have negative investment balance.
		return self.account_balance

	def change_advisor(self, new_advisor_id):
		# Effects: changes the current advisor of this account based on advisor_id
		# Parameter should be a string of length 8 consisting of alphanumeric characters
		# i.e. PHIL2020
		if new_advisor_id is not str:
			raise TypeError('Parameter must be a string')
		elif len(new_advisor_id) != 8:
			raise ValueError('Parameter string should be length of 8')
		else:
			self.advisor_id = new_advisor_id

	def deposit_cash(self, amount):
		# Effects: deposits cash to this account
		# Parameter should be a non-negative float value
		if amount is not float:
			raise TypeError('Parameter must be a float')
		elif amount < 0:
			raise ValueError('Parameter should be greater than or equal to 0')
		else:
			self.cash_balance += amount

	def withdraw_cash(self, amount):
		# Effects: withdraw cash from this account
		# Note: cannot have a negative balance
		# Parameter should be non-negative float.
		'''try:
			self.cash_balance -= amount
			assert(self.cash_balance >= 0)
		except:
			throw NegativeBalanceException'''
		if amount is not float:
			raise TypeError('Parameter must be a float')
		elif amount < 0:
			raise ValueError('Parameter should be greater than or equal to 0')
		else:
			result = cash_balance - amount
			if result >= 0
				self.cash_balance = result
			else:
				difference = abs(result)
				new_withdrawal = amount - difference
				self.cash_balance -= new_withdrawal