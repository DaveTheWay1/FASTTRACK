from django.contrib import admin
from .models import Current_Balance, Monthly_Costs, Monthly_Payments

admin.site.register([Current_Balance, Monthly_Costs, Monthly_Payments])
