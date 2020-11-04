from django.shortcuts import render
from django.views.generic.list import ListView
from .models import SharedInvestment 

# Create your views here.

class SharedInvestmentsListView(ListView):
	'''A list of all investments in the user's portfolio'''

	model = SharedInvestment
	template_name = 'investmentservices/shared_investments_list.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context

