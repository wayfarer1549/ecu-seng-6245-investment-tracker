import unittest
from Investor import Investor

class TestInvestor(unittest.TestCase):

	def setUp(self):
		first_name = 'John'
		last_name = 'Bunyan'
		ssn = '123-45-6789'
		phone_num = '252-989-5555'
		status = False
		self.new_investor = Investor(
			first_name,
			last_name,
			ssn,
			phone_num,
			status)


	def test_investor_constructor(self):
		first_name = 'John'
		last_name = 'Bunyan'
		ssn = '123-45-6789'
		phone_num = '252-989-5555'
		status = False
		
		self.assertEqual(
			self.new_investor.first_name, first_name)
		self.assertEqual(
			self.new_investor.last_name, last_name)
		self.assertEqual(
			self.new_investor.social_security_number, ssn)
		self.assertEqual(
			self.new_investor.phone_number, phone_num)
		self.assertFalse(
			self.new_investor.status)
		self.assertFalse(
			self.new_investor.active)

	def test_add_account(self):
		acct_number = self.new_investor.last_name[:4] + str(2020)
		
		self.new_investor.add_account(acct_number)
		self.assertEqual(
			self.new_investor.account_number, acct_number)
		self.assertTrue(
			self.new_investor.active)

	def test_close_account(self):
		self.new_investor.close_account()
		self.assertFalse(
			self.new_investor.active)