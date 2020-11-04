from django.contrib import admin

# Register your models here.

from .models import SharedInvestment, Bond, InvestmentList, Account, Transaction

admin.site.register(SharedInvestment)
admin.site.register(Bond)
admin.site.register(InvestmentList)
admin.site.register(Account)
admin.site.register(Transaction)
