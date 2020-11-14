from django.contrib.auth.models import AbstractUser
from django.db import models
from investmentservices.models import Account

# Create your models here.
class FinancialUser(AbstractUser):
	'''Overview: Represents a user in the system'''

	#Attributes
	ssn = models.CharField(max_length=11, null=True, blank=False)
	primary_phone_number = models.CharField(max_length=10, null=True, blank=True)

	@property
	def get_full_name(self):
		'''Returns the concatenation of the Abstract User's first & last name attributes'''
		return self.first_name + ' ' + self.last_name


	@property
	def get_ssn(self):
		'''Returns the social security number'''
		return self.ssn

	@property
	def get_phone_number(self):
		return self.primary_phone_number
	
'''
class Investor(BaseUser):
	Overview: Represents an individual investor

	# Attributes
	account = models.OneToOneField(
		Account,
		on_delete=models.CASCADE,
		primary_key=True,
		)

class FinancialAdvisor(BaseUser):
	Overview: Represents a Financial Advisor
	hire_date = models.DateField("date of hire")
'''

