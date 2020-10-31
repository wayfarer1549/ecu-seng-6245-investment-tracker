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


class Investment(models.Model):
	'''Overview Represents an investment in a customer's portfolio'''

	# Attributes
	purchase_date = models.DateTimeField('date purchased')
	name = models.CharField(max_length=200)

	class Meta:
		abstract = True

