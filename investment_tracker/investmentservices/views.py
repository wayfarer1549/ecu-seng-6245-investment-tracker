from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Account, SharedInvestment, Bond, Transaction

# Create your views here.

class CreateAccountView(LoginRequiredMixin, CreateView):
	'''A view for creating a new customer account'''
	model = Account
	template_name = 'investmentservices/create_account.html'
	fields = ['account_number', 'advisor', 'cash_balance']
	success_url = reverse_lazy('shared-investments-list', ) #TODO: change this

class AccountDetailView(LoginRequiredMixin, DetailView):
	'''A view for displaying account details for a particular investor'''
	model = Account
	template_name = 'investmentservices/account_details.html'


	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context

class AccountUpdate(LoginRequiredMixin, UpdateView):
	'''A view for updating an account'''
	model = Account
	fields = ['advisor', 'active']
	template_name = 'investmentservices/account_update.html'
	success_url = reverse_lazy('shared-investments-list', )

class ListAccounts(LoginRequiredMixin, ListView):
	'''Lists all accounts'''
	#TODO: Filter by advisorID?
	model = Account
	template_name = 'investmentservices/list_accounts.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context


class SharedInvestmentsListView(LoginRequiredMixin, ListView):
	'''A list of all shared investments in the user's portfolio'''

	model = SharedInvestment
	template_name = 'investmentservices/shared_investments_list.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context

class BondsListView(LoginRequiredMixin, ListView):
	'''A list of all bonds in the user's portfolio'''

	model = Bond
	template_name = 'investmentservices/bonds_list.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context

class TransactionsListView(LoginRequiredMixin, ListView):
	'''A list of all transactions in the user's purchase history'''

	model = Transaction
	template_name = 'investmentservices/transactions_list.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context

class PurchaseInvestmentView(LoginRequiredMixin, CreateView):
	'''A view for purchasing an investment'''
	fields = ['ticker_symbol', 'name', 'number_of_shares', 'purchase_price', 'investment_type', 'current_price', 'purchase_date']
	template_name = 'investmentservices/purchase_investment.html'
	success_url = reverse_lazy('shared-investments-list', )
	model = SharedInvestment
	login_url = 'login'

	#TODO: Update Cash Balance & Exception Handling depending on Cash Balance
	def form_valid(self, form):
		acct = Account.objects.get(account_owner__exact=self.request.user)
		form.instance.account = acct
		return super().form_valid(form)
		

class PurchaseAdditionalShares(LoginRequiredMixin, UpdateView):
	'''A view for purchasing more shares of an existing investment'''
	model = SharedInvestment
	fields = ['ticker_symbol', 'number_of_shares', ]
	template_name = 'investmentservices/purchase_add_shares.html'
	success_url = reverse_lazy('shared-investments-list',)
	# def get_object(self):
	# 	obj = super().get_object()
	# 	#print(obj.number_of_shares)
	# 	# update cash balance
	# 	obj.save()
	# 	#print(obj.number_of_shares)
	# 	return obj

class SellInvestmentView(LoginRequiredMixin, UpdateView):
	'''A view for selling an investment'''
	model = SharedInvestment
	fields = ['ticker_symbol', 'number_of_shares', ]
	template_name = 'investmentservices/sell_investment.html'
	success_url = reverse_lazy('shared-investments-list', )
	#TODO: Update Cash Balance & Exception Handling depending on Cash Balance


class MakeDepositView(LoginRequiredMixin, UpdateView):
	'''A view for depositing cash to an account'''
	model = Account
	fields = ['cash_balance']
	template_name = 'investmentservices/make_deposit.html'

	def get_success_url(self):
		return reverse_lazy('account-detail', kwargs={'pk': self.kwargs['pk']})

class WithdrawCashView(LoginRequiredMixin, UpdateView):
	'''A view for withdrawing cash from an account'''
	model = Account
	fields = ['cash_balance']
	template_name = 'investmentservices/withdraw_cash.html'
	success_url = reverse_lazy('account-detail', )

	def get_success_url(self):
		return reverse_lazy('account-detail', kwargs={'pk': self.kwargs['pk']})

class StocksListView(LoginRequiredMixin, ListView):
	'''A view for listing all stocks in the current user's portfolio'''
	template_name = 'investmentservices/stocks_list.html'
	context_object_name = 'stocks'

	def get_queryset(self):
		'''Return a list of shared investments of investment type 'stock' '''
		return SharedInvestment.objects.filter(investment_type__exact='STK')

class ETFListView(LoginRequiredMixin, ListView):
	'''A view for listing all ETFs in the current user's portfolio'''
	template_name = 'investmentservices/ETF_list.html'
	context_object_name = 'ETFs'

	def get_queryset(self):
		'''Return a list of shared investments of investment type 'stock' '''
		return SharedInvestment.objects.filter(investment_type__exact='ETF')

class MutualFundListView(LoginRequiredMixin, ListView):
	'''A view for listing all Mutual Funds in the current user's portfolio'''
	template_name = 'investmentservices/mutual_fund_list.html'
	context_object_name = 'mutual_funds'

	def get_queryset(self):
		'''Return a list of shared investments of investment type 'stock' '''
		return SharedInvestment.objects.filter(investment_type__exact='MUF')

class InvestmentDetailView(LoginRequiredMixin, DetailView):
	'''A Detail view for a particular investment in the current user's portfolio'''
	pass
