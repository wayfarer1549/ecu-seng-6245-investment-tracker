from django.urls import path

from .views import SharedInvestmentsListView, BondsListView, TransactionsListView, PurchaseInvestmentView, PurchaseAdditionalShares, SellInvestmentView, AccountDetailView, AccountUpdate, CreateAccountView, ListAccounts, MakeDepositView, WithdrawCashView, StocksListView, ETFListView, MutualFundListView

urlpatterns = [

	path('shares', SharedInvestmentsListView.as_view(), name='shared-investments-list'),
	path('stocks', StocksListView.as_view(), name='stocks-list'),
	path('ETFs', ETFListView.as_view(), name='stocks-list'),
	path('mfunds', MutualFundListView.as_view(), name='stocks-list'),
	path('bonds', BondsListView.as_view(), name='bonds-list'),
	path('transactions', TransactionsListView.as_view(), name='transactions-list'),
	path('account/new', CreateAccountView.as_view(), name='new_account'),
	path('account/<int:pk>/', AccountDetailView.as_view(), name='account-detail'),
	path('account/<int:pk>/update', AccountUpdate.as_view(), name='account-update'),
	path('accounts', ListAccounts.as_view(), name='account-list'),
	path('purchase', PurchaseInvestmentView.as_view(), name='purchase-investment'),
	path('purchase/<int:pk>', PurchaseAdditionalShares.as_view(), name='additional-shares'),
	path('sell/<int:pk>', SellInvestmentView.as_view(), name='sell-investment'),
	path('deposit/<int:pk>', MakeDepositView.as_view(), name='deposit-cash'),
	path('withdraw/<int:pk>', WithdrawCashView.as_view(), name='withdraw-cash'),
]