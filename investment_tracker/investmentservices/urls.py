from django.urls import path

from .views import SharedInvestmentsListView, BondsListView

urlpatterns = [

	path('shares', SharedInvestmentsListView.as_view(), name='shared-investments-list'),
	path('bonds', BondsListView.as_view(), name='bonds-list'),
]