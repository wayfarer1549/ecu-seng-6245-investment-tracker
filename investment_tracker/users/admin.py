from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import FinancialUserCreationForm, FinancialUserChangeForm
from .models import FinancialUser

# Register your models here.

class FinancialUserAdmin(UserAdmin):
	add_form = FinancialUserCreationForm
	form = FinancialUserChangeForm
	model = FinancialUser


admin.site.register(FinancialUser)