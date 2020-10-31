from django.db import models

# Create your models here.
class Account(models.Model):
	'''Overview: Represents a customer's account with the financial brokerage.'''

	# Attributes
	account_number = models.IntegerField()
	#account_owner = models.ForeignKey()
	#advisor = models.ForeignKey()
	#portfolio
	cash_balance = models.DecimalField(max_digits=22, decimal_laces=2)
