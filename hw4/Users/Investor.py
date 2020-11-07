import User
from investor_services import Account

class Investor(User):
	# Overview: Represents an investor of the financial services company

	# Attributes
	def __init__(self, fn, ln, ssn, pn, st,):
		super().__init__(fn, ln, ssn, pn, st)
		self.account_number = ''
		self.active = False

	# Methods

	def add_account(self, number):
		# Effects: Opens a new account for this customer
		# number must be a string of length 8
		# corresponding to first four letters of client
		# last name and 4 digits such as the year they became customer
		# i.e. PHIL2014
		if number is not str:
			raise TypeError('Parameter must be an str object')
		elif len(number) != 8:
			raise ValueError('Parameter must be of length 8 and in the format PHIL2014')
		else:
			self.account_number = number # expects a string
			self.active = True

	def close_account(self):
		# Effects: Closes this customer's account
		# Sets active to false
		# No input parameter, so no input domain to specify
		self.active = False