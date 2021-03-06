import unittest
from Financial_Advisor import Financial_Advisor

class TestFinancialAdvisor(unittest.TestCase):

	def setUp(self):
		first_name = 'John'
		last_name = 'Bunyan'
		ssn = '123-45-6789'
		phone_num = '252-989-5555'
		status = True
		date = '2020-10-01'
		#print(date[:4])
		advisor_id = last_name + date[:4]
		self.new_advisor = Financial_Advisor(
			advisor_id,
			first_name,
			last_name,
			ssn,
			phone_num,
			status,
			date)

	def test_advisor_constructor(self):
		first_name = 'John'
		last_name = 'Bunyan'
		ssn = '123-45-6789'
		phone_num = '252-989-5555'
		status = True
		date = '2020-10-01'
		advisor_id = last_name + date[:4]
		
		self.assertEqual(
			self.new_advisor.first_name, first_name)
		self.assertEqual(
			self.new_advisor.last_name, last_name)
		self.assertEqual(
			self.new_advisor.social_security_number, ssn)
		self.assertEqual(
			self.new_advisor.phone_number, phone_num)
		self.assertTrue(
			self.new_advisor.status)
		self.assertEqual(
			self.new_advisor.hire_date, date)
		self.assertEqual(
			self.new_advisor.advisor_id, advisor_id)

	def test_update_clients(self):

		# create investors
		inv1 = 'CRAN1549'
		inv2 = 'OWEN1689'
		inv3 = 'ANSM1066'

		# append to the client list
		self.new_advisor.update_clients(inv1)
		self.new_advisor.update_clients(inv2)
		self.new_advisor.update_clients(inv3)


		# test
		self.assertIn(inv1, self.new_advisor.client_list)
		self.assertIn(inv2, self.new_advisor.client_list)
		self.assertIn(inv3, self.new_advisor.client_list)

	def test_get_current_clients(self):
		# create a list of investors
		inv1 = 'CRAN1549'
		inv2 = 'OWEN1689'
		investors = [inv1, inv2]
		for investor in investors:
			self.new_advisor.update_clients(investor)
		self.assertEqual(len(self.new_advisor.get_current_clients()), len(investors))

	def test_get_current_clients_invalid_inputs(self):
		with self.assertRaises(ValueError):
			inv1 = 'CRAN15'
			self.new_advisor.update_clients(inv1)
		with self.assertRaises(TypeError):
			inv1 = 15491689
			self.new_advisor.update_clients(inv1)

if __name__ == '__main__':
    unittest.main()