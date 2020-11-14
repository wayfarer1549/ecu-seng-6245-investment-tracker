from django.urls import path

from .views import SharedInvestmentsListView, BondsListView, TransactionsListView, PurchaseInvestmentView, SellInvestmentView, AccountDetailView, AccountUpdate

urlpatterns = [

	path('shares', SharedInvestmentsListView.as_view(), name='shared-investments-list'),
	path('bonds', BondsListView.as_view(), name='bonds-list'),
	path('transactions', TransactionsListView.as_view(), name='transactions-list'),
	path('account/<int:pk>/', AccountDetailView.as_view(), name='account-detail'),
	path('account/<int:pk>/update', AccountUpdate.as_view(), name='account-update'),
	path('purchase', PurchaseInvestmentView.as_view(), name='purchase-investment'),
	path('sell/<int:pk>', SellInvestmentView.as_view(), name='sell-investment'),
	path('deposit/<int:pk>', DepositCashView.as_view(), name='deposit-cash'),
	path('withdraw/<int:pk>', WithdrawCashView.as_view(), name='withdraw-cash'),
]