from Employee import Employee

class Financial_Advisor(Employee):
	# Overview: A Financial Advisor advises customers on investments & acts as a stock broker
	# for purchases of investments

	# Attributes
	def __init__(self, advisor_id, fn, ln, ssn, pn, st, date):
		super().__init__(date, fn, ln, ssn, pn, st)
		self.advisor_id = advisor_id
		self.client_list = []

	# Methods

	def get_current_clients(self):
		# Effects: returns a list of active clients associated with this advisor
		# A client list is a list of customer account numbers
		# in the following format: first four letters of customer last name
		# concatenated with 4 digits
		return self.client_list

	def update_clients(self, investor_number):
		# Effects: Adds a customer (by customer_number) to this advisor's list of clients
		# Parameter must be a string of length 8 matching format noted in
		# get_current_clients()
		if not isinstance(investor_number, str):
			raise TypeError('Parameter must be an str object')
		elif len(investor_number) != 8:
			raise ValueError('Parameter must be of length 8 and in the format ABCD1234')
		else:
			self.client_list.append(investor_number)