from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Account, SharedInvestment, Bond, Transaction

# Create your views here.

class AccountDetailView(DetailView):
	'''A view for displaying account details for a particular investor'''
	model = Account
	template_name = 'investmentservices/account_details.html'


	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context

class AccountUpdate(UpdateView):
	'''A view for updating an account'''
	model = Account
	fields = ['advisor', 'active']
	template_name = 'investmentservices/account_update.html'
	success_url = reverse_lazy('shared-investments-list', )



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

class PurchaseInvestmentView(CreateView):
	'''A view for purchasing an investment'''
	fields = ['ticker_symbol', 'name', 'number_of_shares', 'purchase_price', 'investment_type', 'current_price', 'purchase_date']
	template_name = 'investmentservices/purchase_investment.html'
	success_url = reverse_lazy('shared-investments-list', )
	model = SharedInvestment


class SellInvestmentView():
	'''A view for selling an investment'''
	pass

class MakeDepositView(UpdateView):
	'''A view for depositing cash to an account'''
	pass

class WithdrawCashView(UpdateView):
	'''A view for withdrawing cash from an account'''
	pass

class StocksListView(ListView):
	'''A view for listing all stocks in the current user's portfolio'''
	pass

class ETFListView(ListView):
	'''A view for listing all ETFs in the current user's portfolio'''
	pass

class MutualFundListView(ListView):
	'''A view for listing all Mutual Funds in the current user's portfolio'''
	pass

class InvestmentDetailView(DetailView):
	'''A Detail view for a particular investment in the current user's portfolio'''
	pass
