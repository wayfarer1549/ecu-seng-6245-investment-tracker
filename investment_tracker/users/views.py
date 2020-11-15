from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import FinancialUserCreationForm

class AddInvestorView(CreateView): 
	form_class = FinancialUserCreationForm
	success_url = reverse_lazy('portal') #TODO: Customize form
	template_name = 'add_investor.html'

class AddAdvisorView(CreateView): 
	form_class = FinancialUserCreationForm
	success_url = reverse_lazy('portal') #TODO: Customize form
	template_name = 'add_advisor.html'