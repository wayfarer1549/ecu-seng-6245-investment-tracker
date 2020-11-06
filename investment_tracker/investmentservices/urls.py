from django.urls import path

from .views import SharedInvestmentsListView, BondsListView, TransactionsListView, PurchaseInvestmentView, AccountDetailView, AccountUpdate

urlpatterns = [

	path('shares', SharedInvestmentsListView.as_view(), name='shared-investments-list'),
	path('bonds', BondsListView.as_view(), name='bonds-list'),
	path('transactions', TransactionsListView.as_view(), name='transactions-list'),
	path('account/<int:pk>/', AccountDetailView.as_view(), name='account-detail'),
	path('account/<int:pk>/update', AccountUpdate.as_view(), name='account-update'),
	path('purchase', PurchaseInvestmentView.as_view(), name='purchase-investment'),
]