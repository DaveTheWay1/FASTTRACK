from django.forms import ModelForm
from .models import Current_Balance, Monthly_Costs, Monthly_Payments

class CurrentBalanceForm(ModelForm):
    class Meta:
        model = Current_Balance
        fields = ['amount']

class MonthlyCostsForm(ModelForm):
    class Meta:
        model = Monthly_Costs
        fields = ['name', 'amount']

class MonthlyPaymentsForm(ModelForm):
    class Meta:
        model = Monthly_Payments
        fields = ['name', 'amount']