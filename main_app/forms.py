from django.forms import ModelForm
from .models import Current_Balance

class CurrentBalanceForm(ModelForm):
    class Meta:
        model = Current_Balance
        fields = ['amount']