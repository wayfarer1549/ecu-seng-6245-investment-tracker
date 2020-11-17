from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
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

class ListAccounts(LoginRequiredMixin, UserPassesTestMixin, ListView):
	'''Lists all accounts'''
	
	model = Account
	template_name = 'investmentservices/list_accounts.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context

	def test_func(self):
		return self.request.user.is_advisor


class SharedInvestmentsListView(LoginRequiredMixin, ListView):
	'''A list of all shared investments in the user's portfolio'''

	model = SharedInvestment
	template_name = 'investmentservices/shared_investments_list.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context

class BondsListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
	'''A list of all bonds in the user's portfolio'''

	model = Bond
	template_name = 'investmentservices/bonds_list.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context

	def test_func(self):
		return self.request.user.is_investor

class TransactionsListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
	'''A list of all transactions in the user's purchase history'''

	model = Transaction
	template_name = 'investmentservices/transactions_list.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context

	def test_func(self):
		return self.request.user.is_advisor

class PurchaseInvestmentView(LoginRequiredMixin, CreateView):
	'''A view for purchasing an investment'''
	fields = ['ticker_symbol', 'name', 'number_of_shares', 'purchase_price', 'investment_type', 'current_price', ]
	template_name = 'investmentservices/purchase_investment.html'
	success_url = reverse_lazy('shared-investments-list', )
	model = SharedInvestment
	login_url = 'login'

	#TODO: Update Cash Balance & Exception Handling depending on Cash Balance
	def form_valid(self, form):
		acct = Account.objects.get(account_owner__exact=self.request.user)
		form.instance.account = acct
		# share_price = form.instance.purchase_price
		# share_count = form.instance.number_of_shares
		# get the purchase amt
		# get the number of shares
		# create the transaction
		# inv = SharedInvestment.objects.get(id=self.kwargs['pk'])
		# inv.update_share_count(share_count, share_price)
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
	def form_valid(self, form):
		acct = Account.objects.get(account_owner__exact=self.request.user)
		share_price = form.instance.purchase_price
		share_count = form.instance.number_of_shares
		# get the purchase amt
		# get the number of shares
		# create the transaction
		inv = SharedInvestment.objects.get(id=self.kwargs['pk'])
		current_shares = inv.number_of_shares
		share_difference = share_count - current_shares
		inv.update_share_count(share_difference, share_price)
		return super().form_valid(form)

class SellInvestmentView(LoginRequiredMixin, UpdateView):
	'''A view for selling an investment'''
	model = SharedInvestment
	fields = ['ticker_symbol', 'number_of_shares', ]
	template_name = 'investmentservices/sell_investment.html'
	success_url = reverse_lazy('shared-investments-list', )
	#TODO: Update Cash Balance & Exception Handling depending on Cash Balance
	
	def form_valid(self, form):
		acct = Account.objects.get(account_owner__exact=self.request.user)
		inv = SharedInvestment.objects.get(id=self.kwargs['pk'])
		share_price = form.instance.purchase_price
		share_count = form.instance.number_of_shares
		# get the purchase amt
		# get the number of shares
		# create the transaction
		shares_sold = inv.number_of_shares - share_count
		inv.update_share_count(-shares_sold, share_price)
		return super().form_valid(form)

class MakeDepositView(LoginRequiredMixin, UpdateView):
	'''A view for depositing cash to an account'''
	model = Account
	fields = ['cash_balance', ]
	template_name = 'investmentservices/make_deposit.html'

	def get_success_url(self):
		return reverse_lazy('account-detail', kwargs={'pk': self.kwargs['pk']})

	def form_valid(self, form):
		acct = Account.objects.get(account_owner__exact=self.request.user)
		new_cash_balance = form.instance.cash_balance
		orig_cash_balance = acct.get_cash_balance

		trans_amt = new_cash_balance - orig_cash_balance
		acct.deposit(trans_amt)
		return super().form_valid(form)

class WithdrawCashView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	'''A view for withdrawing cash from an account'''
	model = Account
	fields = ['cash_balance',]
	template_name = 'investmentservices/withdraw_cash.html'
	success_url = reverse_lazy('account-detail', )

	def get_success_url(self):
		return reverse_lazy('account-detail', kwargs={'pk': self.kwargs['pk']})

	def form_valid(self, form):
		acct = Account.objects.get(account_owner__exact=self.request.user)
		
		new_cash_balance = form.instance.cash_balance
		orig_cash_balance = acct.get_cash_balance

		trans_amt = orig_cash_balance - new_cash_balance
		acct.withdraw(trans_amt)

		print(orig_cash_balance, new_cash_balance, trans_amt)


		return super().form_valid(form)

	def test_func(self):
		return self.request.user.is_investor

class StocksListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
	'''A view for listing all stocks in the current user's portfolio'''
	template_name = 'investmentservices/stocks_list.html'
	context_object_name = 'stocks'

	def get_queryset(self):
		'''Return a list of shared investments of investment type 'stock' '''
		return SharedInvestment.objects.filter(investment_type__exact='STK')

	def test_func(self):
		return self.request.user.is_investor

class ETFListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
	'''A view for listing all ETFs in the current user's portfolio'''
	template_name = 'investmentservices/ETF_list.html'
	context_object_name = 'ETFs'

	def get_queryset(self):
		'''Return a list of shared investments of investment type 'stock' '''
		return SharedInvestment.objects.filter(investment_type__exact='ETF')

	def test_func(self):
		return self.request.user.is_investor

class MutualFundListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
	'''A view for listing all Mutual Funds in the current user's portfolio'''
	template_name = 'investmentservices/mutual_fund_list.html'
	context_object_name = 'mutual_funds'

	def get_queryset(self):
		'''Return a list of shared investments of investment type 'stock' '''
		return SharedInvestment.objects.filter(investment_type__exact='MUF')

	def test_func(self):
		return self.request.user.is_investor

class InvestmentDetailView(LoginRequiredMixin, DetailView):
	'''A Detail view for a particular investment in the current user's portfolio'''
	pass
