import unittest
from User import User

class TestUser(unittest.TestCase):

	def setUp(self):
		first_name = 'John'
		last_name = 'Bunyan'
		ssn = '123-45-6789'
		phone_num = '252-989-5555'
		status = False
		self.new_user = User(
			first_name,
			last_name,
			ssn,
			phone_num,
			status)

	def test_base_user_constructor(self):
		first_name = 'John'
		last_name = 'Bunyan'
		ssn = '123-45-6789'
		phone_num = '252-989-5555'
		status = False
		
		self.assertEqual(
			self.new_user.first_name, first_name)
		self.assertEqual(
			self.new_user.last_name, last_name)
		self.assertEqual(
			self.new_user.social_security_number, ssn)
		self.assertEqual(
			self.new_user.phone_number, phone_num)
		self.assertFalse(
			self.new_user.status)

	def test_get_name(self):
		full_name = 'John Bunyan'
		self.assertEqual(
		self.new_user.get_name(), full_name)

	def test_get_ssn(self):
		ssn = '123-45-6789'
		self.assertEqual(
			self.new_user.get_ssn(), ssn)

	def test_is_active(self):
		self.assertFalse(
			self.new_user.is_active())

	def test_set_first_name(self):
		new_first_name = 'Richard'
		
		self.new_user.set_first_name(new_first_name)
		self.assertEqual(
			self.new_user.first_name, new_first_name)

	def test_set_last_name(self):
		new_ln = 'Baxter'
		self.new_user.set_last_name(new_ln)
		self.assertEqual(
			self.new_user.last_name, new_ln)

	def test_update_phone(self):
		new_phone = '919-222-3333'
		self.new_user.update_phone(new_phone)
		self.assertEqual(
			self.new_user.phone_number, new_phone)

	def test_update_user_status(self):
		self.new_user.update_user_status(True)
		self.assertTrue(
			self.new_user.is_active())

if __name__ == '__main__':
    unittest.main()