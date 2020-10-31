from django.contrib import admin

# Register your models here.

from .models import SharedInvestment, Bond, InvestmentList, Account

admin.site.register(SharedInvestment)
admin.site.register(Bond)
admin.site.register(InvestmentList)
admin.site.register(Account)