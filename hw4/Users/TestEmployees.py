import unittest
import Employee

class TestEmployee(unittest.TestCase):

	def setUp(self):
		first_name = 'John'
		last_name = 'Bunyan'
		ssn = '123-45-6789'
		phone_num = '252-989-5555'
		status = True
		date = '2020-10-01'
		self.new_employee = Employee(
			first_name,
			last_name,
			ssn,
			phone_num,
			status,
			date)

	def tearDown(self):
		self.new_employee.dispose()

	def test_employee_constructor(self):
		first_name = 'John'
		last_name = 'Bunyan'
		ssn = '123-45-6789'
		phone_num = '252-989-5555'
		status = True
		date = '2020-10-01'
		
		self.assertEqual(
			self.new_employee.first_name, first_name)
		self.assertEqual(
			self.new_employee.last_name, last_name)
		self.assertEqual(
			self.new_employee.social_security_number, ssn)
		self.assertEqual(
			self.new_employee.phone_number, phone_num)
		self.assertTrue(
			self.new_employee.status)
		self.assertEqual(
			self.new_employee.hire_date, date)

	def test_set_hire_date(self):
		date = '2020-11-01'
		self.new_employee.set_hire_date(date)
		self.assertEqual(
			self.new_employee.hire_date, date)

	def test_set_hire_date_invalid_inputs(self):
		with self.assertRaises(ValueError):
			date = '2020-11-0'
			self.new_employee.set_hire_date(date)
		with self.assertRaises(TypeError):
			date = 20201101
			self.new_employee.set_hire_date(date)
		

	def test_get_hire_date(self):
		date = '2020-10-01'
		self.assertEqual(
			self.new_employee.get_hire_date(), date)

	def test_change_status(self):
		self.new_employee.change_status()
		self.assertFalse(
			self.new_employee)