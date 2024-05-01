from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/logout/', views.user_logout, name='user_logout'),
    path('accounts/signup/', views.signup, name='signup'),
    path('user/<int:user_id>/add_current_balance/', views.add_current_balance, name='add_current_balance'),
    path('current_balance/<int:pk>/update', views.CurrentBalanceUpdate.as_view(), name='current_balance_update'),
    path('user/reset/<int:current_balance>', views.reset, name='reset'),
    path('user/<int:user_id>/add_monthly_cost/', views.add_monthly_costs, name='add_monthly_costs'),
    path('monthly_cost/<int:pk>/update', views.MonthlyCostUpdate.as_view(), name='monthly_cost_update'),
    path('monthly_costs/<int:pk>/delete/', views.MonthlyCostDelete.as_view(), name='monthly_cost_delete'),
    path('monthly_cost/<int:current_balance>/apply/<int:monthly_cost>', views.apply_monthly_costs, name ='apply_monthly_cost'),
    path('user/<int:user_id>/add_monthly_payment/', views.add_monthly_payments, name='add_monthly_payments'),
    path('monthly_payment/<int:pk>/update', views.MonthlyPaymentUpdate.as_view(), name='monthly_payment_update'),
    path('monthly_payment/<int:pk>/delete/', views.MonthlyPaymentDelete.as_view(), name='monthly_payment_delete'),
    path('monthly_payment/<int:current_balance>/apply/<int:monthly_payment>', views.apply_monthly_payment, name ='apply_monthly_payment'),
    path('user/<int:user_id>/add_additional_purchases/', views.add_additional_purchases, name='add_additional_purchase'),
    path('additional_purchase/<int:pk>/update', views.AdditionalPurchaseUpdate.as_view(), name='additional_purchase_update'),
    path('additional_purchase/<int:pk>/delete/', views.AdditionalPurchaseDelete.as_view(), name='additional_purchase_delete'),
    path('additional_purchase/<int:current_balance>/apply/<int:additional_purchase>', views.apply_additional_purchase, name ='apply_additional_purchase'),

]