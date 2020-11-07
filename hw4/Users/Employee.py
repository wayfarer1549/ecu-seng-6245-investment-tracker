import User

class Employee(User):
	# Overview: A class representing an employee in the company

	# Attributes
	def __init__(self, date, fn, ln, ssn, pn, st):
		super().__init__(fn, ln, ssn, pn, st)
		self.hire_date = date

	# Methods
	def set_hire_date(self, date):
		# Effects: Sets this employee's hire date
		# parameter must be a string in format: xxxx-xx-xx i.e. year-month-day
		# Example 2020-01-25

		self.hire_date = date # expects a string in this format: '''2020-01-01'''

	def get_hire_date(self):
		# Effects: Retrieves this employee's hire date
		# must return a string in the format specified for set_hire_date() above
		self.hire_date

	def change_status(self):
		# Effects: Updates this employee's status
		# Since there is no input parameter, there is no input domain to specify
		self.status = False