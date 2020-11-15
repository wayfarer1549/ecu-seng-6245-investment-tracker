from django.urls import path
from django.views.generic import TemplateView
from .views import AddInvestorView, AddAdvisorView


urlpatterns = [
    path('investor/new', AddInvestorView.as_view(), name='addinvestor'),
    path('advisor/new', AddAdvisorView.as_view(), name='addinvestor'),
    path('', TemplateView.as_view(template_name='portal.html'), name='portal'),

]