
class User():
	# Overview: class for a system user

	# Attributes
	def __init__(self, fn, ln, ssn, pn, st):
		self.first_name = fn
		self.last_name = ln
		self.social_security_number = ssn
		self.phone_number = pn
		self.status = st

	# Methods
	def get_name(self):
		# Effects: Returns the concatenation of first_name & last_name as a string
		return self.first_name + " " + self.last_name

	def get_ssn(self):
		# Effects: Returns the Social Security Number of this user
		# as a string in the format xxx-xx-xxxx with length 11

		return self.social_security_number

	def is_active(self):
		# Effects: Returns the user's account status
		# Must return as boolean value
		return self.status

	def set_first_name(name):
		# Effects sets the first name of the user
		# Accepts a non-empty string
		self.first_name = name

	def set_last_name(name):
		# Effects sets the last name of the user
		# Accepts a non-empty string

		self.last_name = name

	def update_phone(phone):
		# Effects updates the user's phone number to format 252-555-1234
		# with length 12
		self.phone_number = phone

	def update_user_status(status):
		# Effects changes the user's account status
		# Accepts boolean parameter
		self.status = status


