from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Account, SharedInvestment, Bond, Transaction

# Create your views here.

class AccountDetailView(DetailView):
	'''A view for displaying account details for a particular investor'''
	model = Account
	template_name = 'investmentservices/account_details.html'


	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context



class SharedInvestmentsListView(ListView):
	'''A list of all shared investments in the user's portfolio'''

	model = SharedInvestment
	template_name = 'investmentservices/shared_investments_list.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context

class BondsListView(ListView):
	'''A list of all bonds in the user's portfolio'''

	model = Bond
	template_name = 'investmentservices/bonds_list.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context

class TransactionsListView(ListView):
	'''A list of all transactions in the user's purchase history'''

	model = Transaction
	template_name = 'investmentservices/transactions_list.html'
	
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context

