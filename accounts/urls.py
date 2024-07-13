from django.urls import path
from . import views


urlpatterns = [
    path('accounts/', views.AccountsAPIView.as_view(), name='accounts'),
    path('transactions/', views.TransactionAPIView.as_view(), name='transactions'),
]
