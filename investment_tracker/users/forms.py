from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import FinancialUser

class FinancialUserCreationForm(UserCreationForm):

	class Meta(UserCreationForm):
		model = FinancialUser
		fields = UserCreationForm.Meta.fields + ('ssn', 'primary_phone_number', 'is_investor', 'is_advisor')

class FinancialUserChangeForm(UserChangeForm):

	class Meta:
		model = FinancialUser
		fields = UserChangeForm.Meta.fields